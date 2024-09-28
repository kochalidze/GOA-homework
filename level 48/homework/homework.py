
# 3) https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python
def order(sentence):
    result = ''
    sentence = sentence.split()
    for integer in range(1, len(sentence)+1):
        for word in sentence:
            if str(integer) in word:
                result += ' ' + word
    return result.strip()