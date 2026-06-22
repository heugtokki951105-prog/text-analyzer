from my_package.utils import load_default_dictionaries


def test_load_default_dictionaries_returns_positive_and_negative_words():
    positive_words, negative_words = load_default_dictionaries()

    assert "good" in positive_words
    assert "bad" in negative_words


def test_load_default_dictionaries_returns_tuples():
    positive_words, negative_words = load_default_dictionaries()

    assert isinstance(positive_words, tuple)
    assert isinstance(negative_words, tuple)
