import shutil
import threading
from os import makedirs
from os.path import join
from datetime import datetime

from config.config import read_json_config
from observer import ScreenGrabObserver


class ImageSaver(ScreenGrabObserver):
    """
    Simple class for saving grabbed screenshots to file.
    """

    def __init__(self):
        """
        Constructor.
        """
        self.output_dir_parts = ""
        self.output_dir_assembled = ""
        self.image_extension = ""
        self.curr_image_index = 1

        self.parse_config(self.read_config())
        self.output_dir_assembled = join(*self.output_dir_parts)
        self.delete_output_dir()
        self.create_output_dir()

    def read_config(self):
        """
        Reads the config file for the ImageSaver.
        :return: A python dict representation of the config.
        """
        return read_json_config(join("config", "imagesaver.json"))

    def parse_config(self, config_json):
        """
        Parses the read config.
        :param config_json: The read config as python dict.
        """
        self.output_dir_parts = config_json['output_dir_parts']
        self.image_extension = config_json['image_extension']
        self.curr_image_index = config_json['image_start_index']

    def process(self, image):
        """
        Saves a given PIL image to disk.
        :param image: The image as PIL.Image object.
        """
        image.save(join(self.output_dir_assembled, self.generate_next_image_name()))


    def generate_next_image_name(self):
        """
        Helper function to generate the next name for an image.
        :return: The generated image name.
        """
        return datetime.today().strftime("%Y-%m-%d") + "-screenshot-" + self.generate_next_image_index() + self.image_extension

    def generate_next_image_index(self):
        """
        Helper function to generate the next index for an image.
        :return: The generated image index.
        """
        index = str(self.curr_image_index)
        self.curr_image_index = self.curr_image_index + 1
        return index

    def create_output_dir(self):
        """
        Helper function to create the specified output directory. Creates also the path to the directory based on the
        configured directory parts.
        :return: True if successful, else False.
        """
        try:
            makedirs(self.output_dir_assembled)
            return True
        except Exception:
            # some error handling...
            pass
        return False

    def delete_output_dir(self):
        """
        Helper function to completely delete the specified output directory.
        :return: True if successful, else False.
        """
        try:
            shutil.rmtree(self.output_dir_assembled)
            return True
        except Exception:
            # some error handling...
            pass
        return False
