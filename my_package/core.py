class Document:
    """텍스트 문서를 분석하는 기본 부모 클래스입니다.

    :ivar text: 분석할 원본 텍스트 데이터
    """

    def __init__(self, text):
        self.text = text

    def _tokenize(self):
        """텍스트를 소문자로 변환하고 단어 단위로 분리하는 비공개 메서드입니다. [cite: 69]

        :return: 분리된 단어 리스트
        """
        return self.text.lower().split()

    def word_frequency(self):
        """문서 내 단어들의 출현 빈도를 계산합니다.

        :return: 단어를 키, 빈도를 값으로 가지는 딕셔너리

        >>> doc = Document("apple banana apple")
        >>> doc.word_frequency()
        {'apple': 2, 'banana': 1}
        """  # [cite: 80]
        words = self._tokenize()  # DRY 원칙 적용 [cite: 70]
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
        return freq

    def sentiment_score(self, positive_words, negative_words):
        """간단한 사전을 기반으로 긍정/부정 감정 점수를 계산합니다.

        :param positive_words: 긍정 단어 리스트 또는 튜플
        :param negative_words: 부정 단어 리스트 또는 튜플
        :return: 정수 형태의 감정 점수 (긍정 +1, 부정 -1)
        """  # [cite: 79]
        words = self._tokenize()
        score = 0
        for word in words:
            if word in positive_words:
                score += 1
            elif word in negative_words:
                score -= 1
        return score
