import pytest

from my_package import Document, SocialMediaPost


def test_word_frequency_counts_repeated_words():
    doc = Document("apple banana apple")

    assert doc.word_frequency() == {"apple": 2, "banana": 1}


def test_word_frequency_is_case_insensitive():
    doc = Document("Python python PYTHON")

    assert doc.word_frequency() == {"python": 3}


def test_word_frequency_empty_text_returns_empty_dictionary():
    doc = Document("")

    assert doc.word_frequency() == {}


def test_sentiment_score_counts_positive_and_negative_words():
    doc = Document("good bad excellent")

    assert doc.sentiment_score(("good", "excellent"), ("bad",)) == 1


def test_sentiment_score_returns_zero_for_neutral_text():
    doc = Document("plain ordinary text")

    assert doc.sentiment_score(("good",), ("bad",)) == 0


def test_document_rejects_none_text_when_analyzed():
    doc = Document(None)

    with pytest.raises(AttributeError):
        doc.word_frequency()


def test_social_media_post_extracts_hashtags():
    post = SocialMediaPost("Learning Python with #pytest #coding")

    assert post.extract_hashtags() == ["#pytest", "#coding"]


def test_social_media_post_counts_hashtags():
    post = SocialMediaPost("Learning Python with #pytest #coding")

    assert post.count_hashtags() == 2


def test_social_media_post_extracts_mentions():
    post = SocialMediaPost("Thanks @alice and @bob")

    assert post.extract_mentions() == ["@alice", "@bob"]


def test_social_media_post_counts_mentions():
    post = SocialMediaPost("Thanks @alice and @bob")

    assert post.count_mentions() == 2


def test_social_media_post_returns_empty_lists_without_tags_or_mentions():
    post = SocialMediaPost("No social markers here")

    assert post.extract_hashtags() == []
    assert post.extract_mentions() == []
    assert post.count_hashtags() == 0
    assert post.count_mentions() == 0


def test_social_media_post_uses_default_platform():
    post = SocialMediaPost("Hello #world")

    assert post.platform == "Twitter"
