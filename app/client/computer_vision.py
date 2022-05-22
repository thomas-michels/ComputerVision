"""
    Module for ComputerVisionClient
"""

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from app.configs import get_environment

_env = get_environment()


class ComputerVision:
    """
    Class to get ComputerVisionClient
    """

    def __init__(self) -> None:
        self.__client = self.__get_client()

    def __get_client(self) -> ComputerVisionClient:
        """
        Method to get ComputerVisionClient instance

        :return:
            ComputerVisionClient
        """

        credentials = CognitiveServicesCredentials(_env.ACCOUNT_KEY)
        return ComputerVisionClient(endpoint=_env.ENDPOINT, credentials=credentials)

    def analize_image(self, url: str):
        image_analysis = self.__client.analyze_image(
            url, visual_features=[VisualFeatureTypes.tags]
        )

        for tag in image_analysis.tags:
            print(tag)

    def analyze_by_domain(self, url: str):
        domain = "landmarks"
        language = "pt"

        analysis = self.__client.analyze_image_by_domain(domain, url, language)

        for landmark in analysis.result["landmarks"]:
            print(landmark["name"])
            print(landmark["confidence"])
