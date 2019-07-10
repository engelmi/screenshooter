import shutil
import threading
from os import makedirs
from os.path import join
from datetime import datetime

from config.config import read_json_config
from observer import ScreenGrabObserver


class ImageSaver(ScreenGrabObserver):
    """

    """

    process_lock = threading.Lock()

    def __init__(self):
        """

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

        :return:
        """
        return read_json_config(join("config", "imagesaver.json"))

    def parse_config(self, config_json):
        """

        :param config_json:
        :return:
        """
        self.output_dir_parts = config_json['output_dir_parts']
        self.image_extension = config_json['image_extension']
        self.curr_image_index = config_json['image_start_index']

    def process(self, image):
        """

        :param image:
        :return:
        """
        image.save(join(self.output_dir_assembled, self.generate_next_image_name()))


    def generate_next_image_name(self):
        """

        :return:
        """
        return datetime.today().strftime("%Y-%m-%d") + "-screenshot-" + self.generate_next_image_index() + self.image_extension

    def generate_next_image_index(self):
        """

        :return:
        """
        index = str(self.curr_image_index)
        self.curr_image_index = self.curr_image_index + 1
        return index

    def create_output_dir(self):
        """

        :return:
        """
        try:
            makedirs(self.output_dir_assembled)
        except Exception:
            # some error handling...
            pass

    def delete_output_dir(self):
        """

        :return:
        """
        try:
            shutil.rmtree(self.output_dir_assembled)
        except Exception:
            # some error handling...
            pass
