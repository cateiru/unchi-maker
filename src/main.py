"""
@author Yuto Watanabe
@version 1.0.0

Copyright (c) 2020 Yuto Watanabe
"""
import time

import pyperclip

from src.analysis import Analysis
from src.exception import TextNotStringError


def get_clipboard() -> str:
  """
  Get to clipboard.

  Returns:
      str: get string from clipboard.
  """
  return pyperclip.paste()


def set_clipboard(text: str) -> None:
  """
  update clipboard.

  Args:
      text (str): string to update.

  Raises:
      TextNotStringError: The string is of a type other than String.
  """
  if not isinstance(text, str):
    raise TextNotStringError('The string is of a type other than String.')
  pyperclip.copy(text)


def main():
  """
  main operation.
  """
  tokenize = Analysis()

  formated_text = ''
  text = ''

  while True:
    text = get_clipboard()
    if text != formated_text and isinstance(text, str):
      formated_text = tokenize.change_noun(text, 'うんち')
      set_clipboard(''.join(formated_text))
    time.sleep(1)
