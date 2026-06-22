def load_default_dictionaries():
    """기본 감정 분석용 긍정/부정 단어 사전(튜플)을 반환합니다.

    :return: (긍정 단어 튜플, 부정 단어 튜플)
    """  # [cite: 79]
    return (
        ("good", "great", "excellent", "happy"),
        ("bad", "sad", "terrible", "worst")
    )
