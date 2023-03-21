from typing import Optional
import requests

class MakeApiCall:
    def __init__(self, api):
        self.resp = self.get_data(api)
        

    def get_data(self, api) -> Optional[str]:
        response = requests.get(api)
        if response.status_code == 200:
            print(f"{response.json()}")
            return response.json()
        else:
            print(
                f"{response.status_code} error with request")

    def get_response(self):
        return self.resp

