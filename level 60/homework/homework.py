#1)https://www.codewars.com/kata/587731fda577b3d1b0001196/train/python
def Camel_case(string):
    word_list = string.split()
    return ''.join([(word[0].upper() + word[1:]) for word in word_list])