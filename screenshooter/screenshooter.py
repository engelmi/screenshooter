import keyboard
from mss import mss
from PIL import Image

from screenshooter import listener as li


class Screenshooter(object):
    """
    Simple class for taking screenshots.
    """

    DEFAULT_CONFIG_SCREENSHOOTER = {
        "shortcut" : "ctrl+shift",
        "monitor" : {
            "monitor_number" : 1,
            "offset_x" : "*",
            "offset_y" : "*",
            "width" : "*",
            "height": "*"
        }
    }

    def __init__(self, grab_screen_observer, config_dict=DEFAULT_CONFIG_SCREENSHOOTER):
        """
        Constructor.
        :param grab_screen_observer: The observer that is being notified for processing a grabbed image.
        """
        if not isinstance(grab_screen_observer, li.ScreenGrabListener):
            raise Exception("Observer needs to be instance of " + str(li.ScreenGrabListener))
        self.grab_screen_observer = grab_screen_observer

        self.shortcut = ""
        self.monitor_dict = {}

        self.parse_config(config_dict)
        self.set_grab_screen_hook()

    def parse_config(self, config_dict):
        """
        Parses the read config.
        :param config_dict: The read config as python dict.
        :return:
        """
        self.shortcut = config_dict["shortcut"]
        self.monitor_dict["monitor_number"] = config_dict["monitor"]["monitor_number"]
        with mss() as sct:
            mon = sct.monitors[self.monitor_dict["monitor_number"]]
            self.monitor_dict["offset_x"] = mon["left"] if (config_dict["monitor"]["offset_x"] == "*") else min(max(config_dict["monitor"]["offset_x"], mon["left"]), mon["width"])
            self.monitor_dict["width"] = mon["width"] if (config_dict["monitor"]["width"] == "*") else  min(max(config_dict["monitor"]["width"], mon["left"]), mon["width"])
            self.monitor_dict["width"] = min(self.monitor_dict["offset_x"] + self.monitor_dict["width"], mon["width"] - self.monitor_dict["offset_x"])
            self.monitor_dict["offset_y"] = mon["top"] if (config_dict["monitor"]["offset_y"] == "*") else min(max(config_dict["monitor"]["offset_y"], mon["top"]), mon["height"])
            self.monitor_dict["height"] = mon["height"] if (config_dict["monitor"]["height"] == "*") else min(max(config_dict["monitor"]["height"], mon["top"]), mon["height"])
            self.monitor_dict["height"] = min(self.monitor_dict["offset_y"] + self.monitor_dict["height"], mon["height"] - self.monitor_dict["offset_y"])

    def set_grab_screen_hook(self):
        """
        Sets the configured shortcut as global keyboard hook for grabbing screenshots.
        """
        self.remove_grab_screen_hook()
        keyboard.add_hotkey(self.shortcut, self.grab_screen)

    def remove_grab_screen_hook(self):
        """
        Removes the configured shortcut from the global keyboard hooks.
        """
        keyboard.release(self.shortcut)

    def grab_screen(self):
        """
        Event method. Called when the keyboard shortcut is being pressed.
        """
        with mss() as sct:
            monitor = {
                "top": self.monitor_dict["offset_y"],
                "left": self.monitor_dict["offset_x"],
                "width": self.monitor_dict["width"],
                "height": self.monitor_dict["height"],
                "mon": self.monitor_dict["monitor_number"],
            }
            # Grab the data
            sct_img = sct.grab(monitor)
            self.grab_screen_observer.process(Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX"))


if __name__ == "__main__":
    from imagesaver import ImageSaver
    s = Screenshooter(ImageSaver())
    input("grabbing images...\n")
