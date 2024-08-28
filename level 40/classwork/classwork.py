#1) https://www.codewars.com/kata/5966e33c4e686b508700002d   
def sum_str(a, b):

    if a == '':
        a = 0
    
    if b == '':
        b =0
    
    return str(int(a) + int(b))

#2) https://www.codewars.com/kata/64fbfe2618692c2018ebbddb
#3) https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa
def open_or_senior(data):
    num = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            num.append('Senior')
        else:
            num.append('Open')
    return num

#4) https://www.codewars.com/kata/529eef7a9194e0cbc1000255
#5) https://www.codewars.com/kata/54ba84be607a92aa900000f1   
#6) https://www.codewars.com/kata/56747fd5cb988479af000028  
#7) https://www.codewars.com/kata/55908aad6620c066bc00002a