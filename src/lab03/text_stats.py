import sys
from src.lib.text import normalize, tokenize, count_freq, top_n


def main():
    text = sys.stdin.read().strip()
    if not text:
        text = input("Введите текст: ")

    print(f"Входной текст: {text}")


    text = normalize(text)
    print(f"Нормализованный текст: {text}")

    tokens = tokenize(text)
    print(f"Токены: {tokens}")

    freqs = count_freq(tokens)
    print(f"Частоты: {freqs}")

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freqs)}")
    print("Топ-5:")
    for word, count in top_n(freqs, n=5):
        print(f"{word}:{count}")

main()

