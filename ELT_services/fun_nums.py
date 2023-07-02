import requests


api_link: str = "http://numbersapi.com/{}/{}"

def nums_api(number: str="random", topic: str="trivia") -> str:
    if not number.isdecimal and number != "random":
        raise ValueError("number parameter must be either numerical or \"random\"")
    result = requests.get(api_link.format(number, topic)).text
    return result

