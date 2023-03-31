from token_ya import token
import requests


class YaFolder:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {"Authorization": self.token}

    def folder_creation(self, name_folder):
        url = f"https://cloud-api.yandex.net/v1/disk/resources/"
        headers = self.get_headers()
        params = {"path": name_folder}
        response = requests.put(url=url, headers=headers, params=params).status_code
        print(f"Статус код = {response}")
        return response


ya_folder = YaFolder(token)
name_folder = "test"