#https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python
def find_it(seq):
    result = 0
    for x in seq:
        result ^= x
    return result




#  2) https://www.codewars.com/kata/523f5d21c841566fde000009
def array_diff(a, b):
    c = []
    
    for e in a:
        for e2 in b:
            if e == e2:
                break
        else:
            c.append(e)
        
    return c