
class ScreenGrabObserver(object):
    """
    Basic observer class to process a grabbed image via the screenshooter.
    """

    def process(self, grabbed_image):
        """
        Abstract method. Processes a grabbed image.
        :param grabbed_image: The grabbed image as PIL.Image.
        """
        raise NotImplementedError("")
