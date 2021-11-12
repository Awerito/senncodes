import httpx
from termcolor import colored

from utils import gen_payloads, post_info
from secrets import headers, validate_code_url


VALID = 200
INVALID = 422


if __name__ == "__main__":

    payloads = gen_payloads()

    with open("data/valid.txt", "r") as file:
        tmp_valid = set(file.read().split())

    with open("data/invalid.txt", "r") as file:
        tmp_invalid = set(file.read().split())

    payloads = list(set(payloads) - tmp_valid - tmp_invalid)
    print("Candidate codes:", len(payloads))

    valids = open("data/valid.txt", "a")
    invalids = open("data/invalid.txt", "a")

    print("Fetching...")
    corrects = int()
    total = len(payloads)
    for i, payload in enumerate(payloads):
        code = payload[14:-2]
        response = post_info(validate_code_url, headers, payload)

        if response == VALID:
            corrects += 1
            valids.write(code + "\n")
            msg = colored("Valid!", "green")
            print(f"{i/total * 100:.2f}% {code} {msg} ({corrects})")
        elif response == INVALID:
            invalids.write(code + "\n")
            msg = colored("Wrong", "red")
            print(f"{i/total * 100:.2f}% {code} {msg}")
        else:
            msg = colored("Error", "yellow")
            print(f"{i/total * 100:.2f}% {code} {msg}")

    valids.close()
    invalids.close()

    print("Done fetching!")
