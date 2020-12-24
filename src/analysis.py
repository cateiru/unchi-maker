"""
@author Yuto Watanabe
@version 1.0.0

Copyright (c) 2020 Yuto Watanabe
"""
from typing import Iterator, Union

from janome.tokenizer import Tokenizer, Token

from src.exception import TextNotStringError


class Analysis():
  """
  Performs morphological analysis.
  """

  def __init__(self) -> None:
    self.tokenizer = Tokenizer()

  def word_separation(self, text: str) -> Union[Token, str]:
    """
    Execute the word-separation by morphological analysis.

    Args:
        text (str): A sentence for morphological analysis.

    Raises:
        TextNotStringError: The string is of a type other than String.

    Returns:
        Union[Token, str]: divided sentences.
    """
    if not isinstance(text, str):
      raise TextNotStringError('The string is of a type other than String.')

    return self.tokenizer.tokenize(text)
