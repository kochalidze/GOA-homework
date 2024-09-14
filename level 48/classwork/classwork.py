# 1) https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/python

def even_or_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


# 2) https://www.codewars.com/kata/54da5a58ea159efa38000836/solutions/python

def finf_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i


# 3) ჩვენზე მოცემული დავალება - https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python

def accum(st):
    index = 1
    world= []
    for i in st:
        i *= index
        i = i.capitalize()
        index += 1
        world.append(i)
    return '-'.join(world)


# 4) 

def solution(number):
    sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


# 5) ჩვენ - https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

def duplicate_encode(word):
    word = word.lower()
    result = ''
    
    for char in word:
        if word.count(char) > 1:
            result = result + ")"
        else:
            result = result + "("
    
    return result