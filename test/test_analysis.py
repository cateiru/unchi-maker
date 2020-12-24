"""
@author Yuto Watanabe
@version 1.0.0

Copyright (c) 2020 Yuto Watanabe
"""
from typing import List

import pytest
from src import analysis

WORD_SEPARATION = analysis.Analysis()


@pytest.mark.parametrize('text, formated_text', [
    ('本日は晴天なり', ['本日', 'は', '晴天', 'なり']),
    ('すもももももももものうち', ['すもも', 'も', 'もも', 'も', 'もも', 'の', 'うち'])
])
def test_analysis(text: str, formated_text: List[str]):
  for index, token in enumerate(WORD_SEPARATION.word_separation(text)):
    assert token.surface == formated_text[index], f'{token.surface} is not fit.'
