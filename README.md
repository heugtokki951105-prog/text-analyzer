# Text Analyzer

## 1. 프로젝트 개요

Text Analyzer는 사용자가 입력한 텍스트를 분석하는 간단한 Python 패키지입니다. 문서의 단어 빈도를 계산하고, 기본 감정 단어 사전을 이용해 감정 점수를 구하며, 소셜 미디어 글에서 해시태그와 멘션을 추출할 수 있습니다.

## 2. 설치 방법

가상환경을 만든 뒤 프로젝트 루트에서 다음 명령을 실행합니다.

```bash
pip install -r requirements.txt
pip install .
```

## 3. 빠른 시작

```python
from my_package import Document, SocialMediaPost
from my_package.utils import load_default_dictionaries

doc = Document("good python good bad")
print(doc.word_frequency())

positive_words, negative_words = load_default_dictionaries()
print(doc.sentiment_score(positive_words, negative_words))

post = SocialMediaPost("Learning Python with @friend #python #pytest")
print(post.extract_mentions())
print(post.extract_hashtags())
print(post.count_mentions())
print(post.count_hashtags())
```

## 4. 주요 기능

- `Document.word_frequency()`: 텍스트의 단어별 출현 빈도를 딕셔너리로 반환합니다.
- `Document.sentiment_score()`: 긍정 단어는 +1, 부정 단어는 -1로 계산하여 감정 점수를 반환합니다.
- `SocialMediaPost.extract_hashtags()`: `#`으로 시작하는 해시태그를 추출합니다.
- `SocialMediaPost.extract_mentions()`: `@`으로 시작하는 멘션을 추출합니다.
- `SocialMediaPost.count_hashtags()`: 텍스트에 포함된 해시태그 개수를 반환합니다.
- `SocialMediaPost.count_mentions()`: 텍스트에 포함된 멘션 개수를 반환합니다.
- `load_default_dictionaries()`: 기본 긍정/부정 단어 사전을 반환합니다.

## 5. 테스트 실행 방법

아래 명령으로 코드 스타일과 단위 테스트를 확인할 수 있습니다.

```bash
pycodestyle my_package tests setup.py
pytest
```

## 6. 작성자 정보

- 작성자: 박윤준
- 과목: Python 프로그래밍
- 프로젝트: 기말 프로젝트 Python 패키지 만들기
- GitHub URL: https://github.com/heugtokki951105-prog/text-analyzer
