"""
@author Yuto Watanabe
@version 1.0.0

Copyright (c) 2020 Yuto Watanabe
"""
import pyperclip

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
