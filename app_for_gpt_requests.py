import sys
import requests
import json


def main_func():


    while True:
        params = None
        p = list(map(int, input("Введите 3 числовых параметра для GPT: ").split()))
        if len(p)==3:
            params = {"val1": p[0], "val2": p[1], "val3": p[2]}

            resp = requests.get("http://127.0.0.1:8000/values_for_GPT/", params=params)
            result = json.loads(resp.text)

            print(f'GPT суммировал переданные значения и вернул результат: {result['val']}')

        else:
            print('Убедитесь что отправили 3 параметра!')

if __name__ == "__main__":
    main_func()


