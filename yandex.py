""" This module is responsible for uploading photos to Yandex disk """
import os
import yadisk

class Yandex:
    """ This class load photo"""
    def __init__(self, token: str) -> None:
        self.token = token

    def load(self):
        """ Main method for load """
        my_yadisk = yadisk.YaDisk(token=self.token)
        my_yadisk.mkdir("/Photo_Vk")
        dir_tupe = os.walk((os.path.join(os.path.dirname(__file__), 'Dir')))
        dir_list = list(dir_tupe)
        for element in dir_list:
            for half_element in element:
                for half_cell in half_element:
                    if len(half_cell) > 1:
                        with open(f"Dir/{half_cell}", "rb") as file:
                            my_yadisk.upload(file, f"/Photo_Vk/{half_cell}")
