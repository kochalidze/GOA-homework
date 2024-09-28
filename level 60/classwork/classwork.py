#https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python

def get_sum(a,b):
    min_number = min(a,b)
    max_number = max(a,b)
    
    sum = 0
    
    for num in range(min_number, max_number + 1):
        sum = sum + num
    
    return sum


# https://www.codewars.com/kata/55f2b110f61eb01779000053
def number(lines):
    result = []
    
    for index in range(len(lines)):
        word = str(index + 1) + ": " + lines[index]
        result.append(word)
    
    return result


# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
def is_pangram(st):
    
    st = st.lower()
    
    letters = set()
    
    for i in st:
        if i.isalpha():
            letters.add(i)
            
    return len(letters) == 26


# https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/train/python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
