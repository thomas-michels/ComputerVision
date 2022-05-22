"""
    Module for Upload image
"""

from datetime import datetime
from imgurpython import ImgurClient
from app.configs import get_environment

_env = get_environment()


class UploadImage:
    """
    Class to Upload image in Imgur
    """

    __client: ImgurClient

    def __init__(self) -> None:
        self.__authenticate()

    def send(self, image_path):
        """
        Method to send image to Imgur
        """
        image = self.__client.upload_from_path(
            image_path, config=self.__generate_headers(), anon=False
        )
        print(f"Link: {image['link']}")

    def __authenticate(self):
        """
        Method to authenticate Imgur API
        """
        self.__client = ImgurClient(_env.IMGUR_ID, _env.IMGUR_SECRET)
        authorization_url = self.__client.get_auth_url("pin")

        print("Go to the following URL: {0}".format(authorization_url))

        pin = input("Enter pin code: ")
        credentials = self.__client.authorize(pin, "pin")

        self.__client.set_user_auth(
            credentials["access_token"], credentials["refresh_token"]
        )
        print("Authentication successful!")

    def __generate_headers(self, name=f"image-{datetime.now()}"):
        """
        Method to generate headers of image
        """
        return {
            "album": None,
            "name": name,
            "title": "image",
            "description": "image on {0}".format(datetime.now()),
        }
