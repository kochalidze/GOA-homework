#1) https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

def pig_it(text):
    words = []
    
    for word in text.split(' '):
        if word.isalpha():
            words.append(word[1:] + word[0] + 'ay')
        else:
            words.append(word)
            
    return ' '.join(words)


#2) https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python
def duplicate_count(text):
    text = text.lower()
    duflicates = []
    for char in text:
        if text.count(char) > 1 and char not in duflicates:
            duflicates.append(char)
    return len(duflicates)
     