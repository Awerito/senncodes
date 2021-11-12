import httpx
from random import shuffle


def post_info(url, headers, data):
    req = httpx.post(url, headers=headers, data=data, timeout=None)
    return req.status_code


def gen_payloads():
    words = list()
    # vowels = "aeiou"
    vowels = "aeu"
    consonants = "bcdfghjklmnpqrstvwxyz"
    for a in vowels:
        for b in consonants:
            for c in vowels:
                for d in consonants:
                    for e in vowels:
                        words.append("".join([a, b, c, d, e]))
    shuffle(words)
    return [f'{{"code": "hunt{word}"}}' for word in words]


if __name__ == "__main__":
    payloads = gen_payloads()
    print(len(payloads))
    with open("data/words.txt", "w") as file:
        file.write("\n".join(payloads))
