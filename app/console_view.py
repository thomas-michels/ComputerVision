"""
    Module for Console View
"""
from app.imgur import UploadImage
from app.client import ComputerVision


class ConsoleView:

    __upload_image: UploadImage
    __computer_vision: ComputerVision

    def __init__(self) -> None:
        self.logged = False
        print("Starting application")
        self.__build()
        print("Application Started!")
        self.run()

    def run(self):
        exit = False

        while not exit:
            print("=" * 50)
            self.__options()
            if self.__input_options():
                exit = True

    def __options(self):
        print("1 - Salvar Imagem no Imgur (Precisa estar logado no Imgur)")
        print("2 - Analizar Imagem")
        print("3 - Analizar Imagem por dominio")
        print("4 - Imagens pre-enviadas")
        print("5 - Sair")

    def __input_options(self) -> bool:
        try:
            entry = int(input("Opção: "))
            if entry == 1:
                if self.logged:
                    url = input("Path da Imagem: ")
                    self.__upload_image.send(url)

                else:
                    print("Voce nao esta logado!")

            elif entry == 2:
                url = input("URL da Imagem: ")
                self.__computer_vision.analize_image(url)

            elif entry == 3:
                url = input("URL da Imagem: ")
                self.__computer_vision.analyze_by_domain(url)

            elif entry == 4:
                self.__print_url_images()

            else:
                print("Saindo...")
                return True

        except Exception as e:
            self.__input_options()

    def __build(self):
        login = input("Voce deseja logar no Imgur? sim/nao: ")

        if login == "sim":
            self.__upload_image = UploadImage()
            self.logged = True

        self.__computer_vision = ComputerVision()

    def __print_url_images(self):
        print("=" * 50)
        print("Headset: https://i.imgur.com/sydfJhZ.jpeg")
        print("Setup: https://i.imgur.com/C3luqIV.jpeg")
        print("Torre de Pisa: https://i.imgur.com/Eysbqjv.jpeg")
        print("Torre Eiffel: https://i.imgur.com/rF74X8p.jpeg")
