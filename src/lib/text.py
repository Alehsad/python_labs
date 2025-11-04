def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")

    if casefold:
        text = text.casefold()

    text = text.replace("\n", " ").replace("\r", " ").replace("\t", " ")

    text = " ".join(text.split())

    return text

print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))


def tokenize(text: str) -> list[str]:
    result = []
    word = ""

    for ch in text:
        if ch.isalnum() or ch == "_" or (ch == "-" and word):
            word += ch
        else:
            if word and word[-1] != "-":
                result.append(word)
            word = ""


    if word and word[-1] != "-":
        result.append(word)

    return result


print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))

def count_freq(tokens: list[str]) -> dict[str, int]:
    freqs = {}
    for token in tokens:
        freqs[token] = freqs.get(token, 0) + 1
    return freqs


def sort_key(item):
    word, count = item
    return (-count, word)


def top_n(freqs: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freqs.items(), key=sort_key)
    return sorted_items[:n]

tokens1 = ["a", "b", "a", "c", "b", "a"]
freqs1 = count_freq(tokens1)
print("Частоты:", freqs1)
print("Top-2:", top_n(freqs1, n=2))
print()

tokens2 = ["bb", "aa", "bb", "aa", "cc"]
freqs2 = count_freq(tokens2)
print("Частоты:", freqs2)
print("Top-2:", top_n(freqs2, n=2))