import httpx
from termcolor import colored

from utils import gen_payloads, post_info
from secrets import headers, validate_code_url

VALID = 200
INVALID = 422

if __name__ == "__main__":

    words = gen_payloads()

    with open("data/valid.txt", "r") as file:
        tmp_valid = set(file.read().split())

    with open("data/invalid.txt", "r") as file:
        tmp_invalid = set(file.read().split())

    words = list(set(words) - tmp_valid - tmp_invalid)
    print("Candidate codes:", len(words))

    valids = open("data/valid.txt", "a")
    invalids = open("data/invalid.txt", "a")

    print("Fetching...")
    corrects = int()
    total = len(words)
    for i, code in enumerate(words):
        payload = f'{{"code": "HUNT{code.upper()}"}}'

        preflight = httpx.options(validate_code_url, headers=headers, timeout=None)
        if preflight.status_code == 204:
            response = post_info(validate_code_url, headers, payload)

            if response == VALID:
                corrects += 1
                valids.write(code + "\n")
                msg = colored(str(response), "green")
                print(f"{i/total * 100:.2f}% {code} {msg} ({corrects})")
            elif response == INVALID:
                invalids.write(code + "\n")
                msg = colored(str(response), "red")
                print(f"{i/total * 100:.2f}% {code} {msg}")
            else:
                msg = colored(str(response), "yellow")
                print(f"{i/total * 100:.2f}% {code} {msg}")
        else:
            msg = colored(str(preflight.status_code), "red")
            print(f"{i/total * 100:.2f}% {code} {msg}p")

    valids.close()
    invalids.close()

    print("Done fetching!")
