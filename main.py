"""This is the main entry point"""
import datetime
import json
import time
from progress.bar import IncrementalBar
from photo import Vresponse
from yandex import Yandex

if __name__ == '__main__':
    KEY_FOR_YANDEX = str(input('Введите ваш токен для Яндекс диска: '))
    TOKEN_VK = str(input("Введите ваш ключ для ВК: "))
    NUMBER_FOR_SAVE_PHOTO = int(input("Введите какое количество фотографий вы хотите сохранить: " ))
    User = Vresponse(token=TOKEN_VK)
    User.response()
    User.control_function(NUMBER_FOR_SAVE_PHOTO)
    Yan = Yandex(token=KEY_FOR_YANDEX)
    Yan.load()

