# 실행 결과 요약

## 1. pycodestyle 실행 결과

실행 명령:

```bash
python -m pycodestyle my_package tests setup.py
```

실행 결과:

```text
출력 없음
```

해석: PEP 8 스타일 경고 0건입니다.

## 2. pytest 실행 결과

실행 명령:

```bash
python -m pytest -q
```

실행 결과:

```text
..............                                                           [100%]
14 passed, 1 warning in 0.03s
```

참고: 경고는 테스트 실패가 아니라 pytest 캐시 디렉터리 생성 권한과 관련된 `PytestCacheWarning`입니다.

## 3. pip install 실행 결과

실행 명령:

```bash
python -m pip install . --no-build-isolation
```

실행 결과:

```text
Processing c:\users\shakecarrot\desktop\pypy\my_project
Preparing metadata (pyproject.toml): finished with status 'done'
Building wheels for collected packages: text_analyzer
Building wheel for text_analyzer (pyproject.toml): finished with status 'done'
Successfully built text_analyzer
Successfully installed text_analyzer-0.1.0
```

참고: 현재 실습 환경에서는 네트워크 접근이 제한되어 기본 `pip install .` 실행 시 빌드 의존성 다운로드 단계에서 실패했습니다. 로컬 가상환경에 이미 설치된 빌드 도구를 사용하기 위해 `--no-build-isolation` 옵션으로 설치 검증을 진행했습니다.
