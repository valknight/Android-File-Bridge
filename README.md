#  Android File Bridge

File browser library to interact with Android devices, using ADB. 

## Requirements

- Python 3.6+
- ADB binary available on path

## Setup

Install `android-file-bridge` from PyPi using `pip install android-file-bridge`

## Usage

### Creating a device object

#### USB

Before using this, make sure the device is connected and available through `adb devices`.

```python3
from android_file_bridge import Device
connection = Device()
```

#### Network

```python3
from android_file_bridge import Device
connection = Device(ip_address="0.0.0.0") # obviously change this!
```

### List a directory

```python3
connection.list_path("/sdcard/Download")
```

### Download a file from your phone

```python3
connection.pull("/sdcard/important_file.pdf", "file.pdf")
```

### Upload a file to your phone

```python3
connection.push("image.png", "/sdcard/cool_photo.png")
```

