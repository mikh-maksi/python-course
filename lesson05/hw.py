import re


CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = (
    "a",
    "b",
    "v",
    "g",
    "d",
    "e",
    "e",
    "j",
    "z",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "r",
    "s",
    "t",
    "u",
    "f",
    "h",
    "ts",
    "ch",
    "sh",
    "sch",
    "",
    "i",
    "",
    "y",
    "e",
    "u",
    "ja",
    "je",
    "ji",
    "g",
)
assert len(CYRILLIC_SYMBOLS) == len(
    TRANSLATION
), f"{len(CYRILLIC_SYMBOLS)} != {len(TRANSLATION)}"
TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def normalize(name: str) -> str:
    t_name = name.translate(TRANS)
    t_name = re.sub(r"\W", "_", t_name)
    return t_name


if __name__ == "__main__":
    import sys

    print(normalize(" ".join(sys.argv[1:])))
