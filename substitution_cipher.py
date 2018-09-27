#!/usr/bin/env python
import string, random

CIPHER_DICT = {'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 'c', 'm': 'w', 'o': 'y', 'g': 'f', 'a': 'm', 'x': 'j', 'l': 'n', 's': 'o', 'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 'f': 'p', ' ': 'b', 'q': 'r', 'z': 'e', 'p': 'v', 'v': 'l', 'h': 'h', 'd': 'd', 'n': 'a', 't': ' ', 'w': 't'}

def cipher(phrase, cipher_dict):
  """
  that takes a string 'phrase' and a dictionary 'cipher_dict' and
  returns the results of replacing each character in 'phrase' by its corresponding value in 'cipher_dict'
  """
  output = ""
  for i in phrase:
    output += cipher_dict[i]

  return output

def make_decipher_dict(cipher_dict):
  """
  takes a cipher dictionary 'cipher_dict' and returns a new dictionary 'decipher_dict' with the property that applying
  'decipher_dict' to a phrase encrypted using 'cipher_dict' returns the original phrase
  """
  decipher_dict = {}
  for k,v in cipher_dict.items():
    decipher_dict[v] = k

  return decipher_dict

DECIPHER_DICT = make_decipher_dict(CIPHER_DICT)
print cipher('pig', CIPHER_DICT) # prints 'vif'
print cipher('vif', DECIPHER_DICT) # prints 'pig'


def make_cipher_dict(alphabet):
  """
  that takes a string of unique characters and returns a randomly-generated cipher dictionary for the characters in 'alphabet'
  """
  L = list(string.ascii_lowercase)
  new_cipher_dict = {}
  for i in alphabet:
    random.shuffle(L)
    new_cipher_dict[i] = L[0]
    L.pop(0)
  return new_cipher_dict

print make_cipher_dict('abcd')
