# https://www.codewars.com/kata/57ed30dde7728215300005fa
def bumps(road):
    # result = 0
    # for character in road:
    #     if character == 'n':
    #    result += 1
    # return 'Woohoo!' if result <= 15 else 'Car Dead'
    
    result = len([character for character in road if character == 'n'])
    return 'Woohoo!' if result <= 15 else 'Car Dead'


# https://www.codewars.com/kata/535474308bb336c9980006f2

# https://www.codewars.com/kata/586beb5ba44cfc44ed0006c3
def sum_even_numbers(seq): 
    return sum(i for i in seq if i %2 == 0)


# https://www.codewars.com/kata/5413759479ba273f8100003d
def reverse(lst):
    empty_list = list(lst)             # use this!
    for value in lst:
        empty_list.insert(0,value)
        empty_list.pop(-1)
    return empty_list


# https://www.codewars.com/kata/57d2807295497e652b000139

# https://www.codewars.com/kata/5effa412233ac3002a9e471d

# https://www.codewars.com/kata/609eee71109f860006c377d1
def last_survivor(letters, coords): 
    # your code here
    for i in coords:
        letters = letters[:i] + letters[i +1:]
    return letters


# https://www.codewars.com/kata/5768a693a3205e1cc100071f



# https://www.codewars.com/kata/5701e43f86306a615c001868


# https://www.codewars.com/kata/57f7b8271e3d9283300000b4

