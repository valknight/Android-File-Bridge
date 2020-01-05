import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="android-file-bridge",
    version="0.0.1",
    author="Vallerie Knight",
    author_email="val@valknight.xyz",
    description="Provides easy to use file browser, over ADB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/valknight/androidfilebridge",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux"
    ],
    python_requires='>=3.6',
)