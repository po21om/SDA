import json
import time

import requests
from typing import Dict, Union
from singleton_metaclass import SingletonMeta


class JokeAPIConnector(metaclass=SingletonMeta):
    def __init__(self):
        self.BASE_URL: str = 'https://v2.jokeapi.dev'
        self.headers: Dict[str, str] = {'Accept': 'application/json'}
        self._response: Union[requests.Request, None] = None
        self._delay: int = 1

    def _build_path(self, *args: str) -> str:
        return f'{self.BASE_URL}/{"/".join(args)}?type=single'

    @staticmethod
    def _build_error_message(status_code: int, message: str) -> Dict[str, str]:
        return {'Error': f'{status_code}: {message}'}

    def get_joke(self, category: str = 'Any') -> Union[Dict, str]:
        time.sleep(self._delay)
        # w python 3.10 wprowadzono '|' jako union i wtedy 'Dict | str'
        self._response = requests.request('GET', self._build_path('joke', category), headers=self.headers)
        if self._response.ok:
            return json.loads(self._response.text).get('joke')
        else:
            error = json.loads(self._response.text)
            return self._build_error_message(self._response.status_code, error.get('message'))


if __name__ == '__main__':
    joke = JokeAPIConnector()
    print(joke)
    print(joke.get_joke())
    d = {'a': 1, 'b': 2}
    joke2 = JokeAPIConnector()
    print(joke2)
    print(joke2.get_joke())
    print()
