"""
@author Yuto Watanabe
@version 1.0.0

Copyright (c) 2020 Yuto Watanabe
"""
import pytest
from src import main
from src.exception import TextNotStringError


def test_get_clipboard():
  assert isinstance(main.get_clipboard(), str), 'returned value is not string.'


@pytest.mark.parametrize('text', [
    ('Hello Word'),
    ('Hogehoge'),
    ('1234'),
    ('あいうえお')
])
def test_set_clipboard(text):
  main.set_clipboard(text)

  assert main.get_clipboard() == text, 'The clipboard has not been updated correctly.'


def text_not_string_args():
  with pytest.raises(TextNotStringError):
    main.set_clipboard(1)
