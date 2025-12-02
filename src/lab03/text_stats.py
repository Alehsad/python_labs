import sys
from src.lib.text import normalize, tokenize, count_freq, top_n


def main():
    text = sys.stdin.read().strip()
    if not text:
        text = input()

    text = normalize(text)
    tokens = tokenize(text)
    freqs = count_freq(tokens)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freqs)}")
    print("Топ-5:")
    for word, count in top_n(freqs, n=5):
        print(f"{word}:{count}")


main()
