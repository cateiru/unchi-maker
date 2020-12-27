"""
@author Yuto Watanabe
@version 1.0.0

Copyright (c) 2020 Yuto Watanabe
"""
from typing import List

from janome.tokenizer import Tokenizer, Token

from .exception import TextNotStringError


class Analysis():
  """
  Performs morphological analysis.
  """

  def __init__(self) -> None:
    self.tokenizer = Tokenizer()

  def word_separation(self, text: str) -> Token:
    """
    Execute the word-separation by morphological analysis.

    Args:
        text (str): A sentence for morphological analysis.

    Raises:
        TextNotStringError: The string is of a type other than String.

    Returns:
        Token: divided sentences.
    """
    if not isinstance(text, str):
      raise TextNotStringError('The string is of a type other than String.')

    return self.tokenizer.tokenize(text)

  def change_noun(self, text: str, change_text: str) -> List[str]:
    """
    Change the noun to a different letter.

    Args:
        text (str): Original text
        change_text (str): The character to replace.

    Returns:
        List[str]: A word-by-word list of converted characters.
    """
    formated_text: List[str] = []

    for element in self.word_separation(text):
      part_of_speech = element.part_of_speech
      if '名詞' in part_of_speech:
        formated_text.append(change_text)
      else:
        surface = element.surface
        formated_text.append(surface)

    return formated_text
