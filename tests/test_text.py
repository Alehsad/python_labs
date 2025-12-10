import pytest

from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
        ("   \n\t   ", ""),
    ],
)
def test_normalize_basic_and_edges(source: str, expected: str) -> None:
    assert normalize(source) == expected


@pytest.mark.parametrize(
    "source, expected_tokens",
    [
        ("Привет, мир!", ["привет", "мир"]),
        ("ёжик, Ёлка", ["ежик", "елка"]),
        ("Hello, world!!!", ["hello", "world"]),
        ("  пробелы   и\tпереносы\n", ["пробелы", "и", "переносы"]),
        ("", []),
    ],
)
def test_tokenize_basic(source: str, expected_tokens):
    assert tokenize(source) == expected_tokens


def test_count_freq_basic():
    tokens = ["кот", "пес", "кот", "кот", "пес"]
    freq = count_freq(tokens)

    assert freq["кот"] == 3
    assert freq["пес"] == 2
    assert set(freq.keys()) == {"кот", "пес"}


def test_top_n_basic():
    tokens = ["python", "java", "python", "c", "java", "python"]
    freq = count_freq(tokens)

    result = top_n(freq, 2)

    assert result == [("python", 3), ("java", 2)]


def test_top_n_tie_breaker_alphabetical():
    freq = {"python": 2, "java": 2, "c++": 2}
    result = top_n(freq, 3)

    assert result == [("c++", 2), ("java", 2), ("python", 2)]


def test_top_n_n_bigger_than_dict():
    freq = {"a": 1, "b": 2}
    result = top_n(freq, 10)

    assert result == [("b", 2), ("a", 1)]


def test_top_n_zero_or_negative():
    freq = {"a": 1, "b": 2}
    assert top_n(freq, 0) == []
    assert top_n(freq, -5) == []


def test_pipeline_normalize_tokenize_count_freq_top_n():
    text = "Привет, привет, мир! Мир, мир, мир..."
    tokens = tokenize(text)
    freq = count_freq(tokens)
    top = top_n(freq, 2)

    assert top == [("мир", 4), ("привет", 2)]
