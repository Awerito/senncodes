import httpx
from random import shuffle
from termcolor import colored

from utils import post_info
from secrets import headers, submit_info, subscribe_url


VALID = 200
INVALID = 422


if __name__ == "__main__":

    with open("data/valid.txt", "r") as file:
        codes = file.read().split()
    shuffle(codes)

    total = len(codes)
    print("Submitting...")
    for i, code in enumerate(codes):
        payload = '{{"first_name":"{}","last_name":"{}","email":"{}","terms":true,"terms2":null,"code":"{}","lang":"en"}}'.format(
            submit_info["first_name"],
            submit_info["last_name"],
            submit_info["email"],
            "hunt" + code,
        )
        response = post_info(subscribe_url, headers, payload)

        if response == VALID:
            msg = colored("Submitted!", "green")
            print(f"{i/total * 100:.2f}% {code} {msg}")
        elif response == INVALID:
            msg = colored("Already used", "red")
            print(f"{i/total * 100:.2f}% {code} {msg}")
        else:
            msg = colored("Error submitting", "yellow")
            print(f"{i/total * 100:.2f}% {code} {msg}")

    print("Done submitting")
