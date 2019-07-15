[![PyPI version](https://badge.fury.io/py/ScreenShooter.svg)](https://badge.fury.io/py/screenshooter)
[![Python Support](https://img.shields.io/pypi/pyversions/screenshooter.svg)](https://pypi.org/project/screenshooter/)

# ScreenShooter
ScreenShooter provides a simple way of generating a screen shots via customizable keyboard shortcuts. 

## Installation
```bash
$ pip install screenshooter
```

## Usage
The ScreenShooter is easy to use:
```python
from screenshooter import Screenshooter, ImageSaver
s = Screenshooter(ImageSaver())
```
This creates a ScreenShooter that sends grabbed images to the default ImageSaver. The images are saved in ``./screenshots*.png``. 

It is possible to customize the ScreenShooter as well as the ImageSaver: 
```python
from screenshooter import Screenshooter, ImageSaver

custom_saver_config = {
        "output_dir_parts" : ["screenshots"],
        "image_extension" : ".png",
        "image_start_index" : 1
    }
custom_shooter_config = {
        "shortcut" : "ctrl+shift",
        "monitor" : {
            "monitor_number" : 1,
            "offset_x" : "*",
            "offset_y" : 200,
            "width" : "*",
            "height": "*"
        }
    }

s = Screenshooter(ImageSaver(config_dict=custom_saver_config), config_dict=custom_shooter_config)
```