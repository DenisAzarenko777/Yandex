"""This module is responsible for uploading photos"""
import json
import os
import time
import datetime
import requests
from progress.bar import IncrementalBar

# noinspection PyPep8Naming
class Vresponse():
    """Main class for working with photos"""

    def __init__(self, token: str, id: str) -> None:
        self.token = token
        self.id = id

    def response(self):
        """The method that building first json-file-response.json """
        vkontakte = requests.get('https://api.vk.com/method/photos.get',
                                   params={
                                       "owner_id": self.id,
                                       "access_token": self.token,
                                       "count": '1000',
                                       "album_id": "profile",
                                       "photo_sizes": 1,
                                       "v": 5.122,
                                       "extended": 1,
                                   }).json()

        with open('response.json', 'w') as file:
            json.dump(vkontakte, file, indent=2, ensure_ascii=False)

    def get_largest(self, size_dict):
        """The method that finding max size"""
        if size_dict['width'] >= size_dict['height']:
            self.variable_size = size_dict['width']
        else:
            self.variable_size = size_dict['height']
        return self.variable_size

    def check_out(self, name):
        """The method that check name"""
        self.test_name = name
        for element in os.listdir(
                os.path.join(os.path.dirname(__file__), 'Dir')):
            if self.test_name == element:
                self.test_name = self.test_name[:-4] + "1" + self.test_name
        return self.test_name

    def download_photo(self, url, j):
        """The method that write photo"""
        variable_name = self.check_out(j)
        variable_content = requests.get(url)
        out = open(f"Dir/{variable_name}.jpg", "bw")
        out.write(variable_content .content)
        out.close()

    def control_function(self, number_for_save_photos):
        """ This is the main logic of the program"""
        self.number_for_save_photos = number_for_save_photos
        global_count = 0
        photos = json.load(open('response.json'))['response']['items']
        now = datetime.datetime.now()
        test_list = []
        file_dict = {}
        info_file = []
        bar = IncrementalBar('Photo download', max=number_for_save_photos)
        for photo in photos:
            sizes = photo['sizes']
            max_size = max(sizes, key=self.get_largest)['url']
            like = photo['likes']['count']
            if like in test_list:
                like_name = str(like) + str(now)[:-15]
            else:
                like_name = like
            file_dict['file_name'] = like_name
            file_dict['size'] = max(sizes, key=self.get_largest)['type']
            info_file.append(file_dict)
            self.download_photo(max_size, like_name)
            test_list.append(like)
            global_count = global_count + 1
            if global_count == self.number_for_save_photos:
                break
            time.sleep(1)
            file_dict = {}
            bar.next()
        bar.finish()
        with open('data.json', 'w') as file:
            json.dump(info_file, file, indent=2)
