from .core import Document


class SocialMediaPost(Document):
    """소셜 미디어 포스트(트윗 등) 분석을 위한 자식 클래스입니다. [cite: 31, 66]
    Document 클래스를 상속받습니다. [cite: 66]
    """

    def __init__(self, text, platform="Twitter"):
        """
        :param text: 소셜 미디어 원본 텍스트
        :param platform: 소셜 미디어 플랫폼 이름 (기본값: Twitter)
        """  # [cite: 79]
        super().__init__(text)  # 부모 클래스 초기화 호출 [cite: 67]
        self.platform = platform

    def extract_hashtags(self):
        """텍스트에서 해시태그(#)를 추출합니다.

        :return: 해시태그 문자열 리스트

        >>> post = SocialMediaPost("Hello #world #python")
        >>> post.extract_hashtags()
        ['#world', '#python']
        """  # [cite: 80]
        words = self.text.split()
        return [word for word in words if word.startswith('#')]

    def extract_mentions(self):
        """텍스트에서 사용자 멘션(@)을 추출합니다.

        :return: 멘션 문자열 리스트
        """  # [cite: 79]
        words = self.text.split()
        return [word for word in words if word.startswith('@')]

    def count_hashtags(self):
        """텍스트에 포함된 해시태그 개수를 반환합니다.

        :return: 해시태그 개수

        >>> post = SocialMediaPost("Hello #world #python")
        >>> post.count_hashtags()
        2
        """
        return len(self.extract_hashtags())

    def count_mentions(self):
        """텍스트에 포함된 사용자 멘션 개수를 반환합니다.

        :return: 멘션 개수

        >>> post = SocialMediaPost("Thanks @alice and @bob")
        >>> post.count_mentions()
        2
        """
        return len(self.extract_mentions())
