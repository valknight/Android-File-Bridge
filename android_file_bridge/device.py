import os.path
import os
import sys
from adbutils.errors import AdbError
from adbutils import adb
from android_file_bridge.error import AdbConnectionError, AdbPushError, AdbPullError


def fileInfoToDict(fileInfoObj):
    return {'mode': fileInfoObj.mode, 'mtime': fileInfoObj.mtime, 'name': fileInfoObj.name}


class Device:
    def __init__(self, ip_address=None, serial=None):
        if ip_address is None:
            device_count = len(adb.devices())
            if device_count == 0:
                raise AdbConnectionError("No devices found")
            elif device_count == 1:
                self.adb = adb.device()
            elif device_count > 1:
                raise AdbConnectionError("Todo: Too many devices")
        else:
            output = adb.connect(ip_address)
            if "failed to" in output:
                raise AdbConnectionError(output)
            self.adb = adb.device(serial=ip_address)
        self.current_path = "/"
        pass

    def change_path(self, path):
        self.current_path = path
        if not(self.current_path.endswith('/')):
            self.current_path = "{}/".format(self.current_path)

    def list_path(self):
        files = []
        for file in self.adb.sync.list(path=self.current_path):
            file_dict = fileInfoToDict(file)
            file_dict['path'] = "{}{}".format(self.current_path, file_dict['name'])
            files.append(file_dict)
        return files
    
    def pull(self, remote_file, local_path):
        reason = None
        def generate_error():
            return "Could not pull {} to {} - {}".format(remote_file, local_path, reason)
        
        try:
            self.adb.sync.pull(remote_file, local_path)
            return
        except AdbError:
            type, reason, traceback = sys.exc_info()
        if reason is None:
            reason = "unknown error"
        raise AdbPullError(generate_error())
    
    def push(self, local_file, remote_file):
        def generate_error(reason):
            return "Could not push {} to {} - {}".format(local_file, remote_file, reason)
        split_path = remote_file.split("/")
        del split_path[-1]
        path = '/'.join(split_path)
        if len(self.adb.sync.list(path)) == 0:
            # if len is 0, path does not exist
            # paths that exist have at least a "." and ".." entry
            raise AdbPushError(generate_error("path {} does not exist".format(path)))
        try:
            self.adb.sync.push(local_file, remote_file)
        except AssertionError:
            raise AdbPushError(generate_error("unknown error"))