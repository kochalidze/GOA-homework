#0) დაასრულეთ codewars ამოცანები:
#1) https://www.codewars.com/kata/53dbd5315a3c69eed20002dd                 
def filter_list(l):
    result = []
    for character in l:
        if type(character) != str:
            result.append(character)
    return result


#2) https://www.codewars.com/kata/558fc85d8fd1938afb000014
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return sum(numbers[:2])



#3) https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d


#4) https://www.codewars.com/kata/57f609022f4d534f05000024
def stray(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i

        

#5) https://www.codewars.com/kata/57ea5b0b75ae11d1e800006c
def sort_by_length(arr):
#     arr.sort(key = len)
#     return arr
    return sorted(arr, key=len)



#1) classwork-ში შესრულებული ამოცანებიდან 5-ვე კარგად განიხილეთ, ეცადეთ გააუმჯობესოთ კოდი - დაწეროთ უფრო მოკლე ვარიანტი თუ შესაძლებელი იქნება:

#1

def is_divisible(n,x,y):
    if  n  % x == 0 and n % y == 0:
        return True

    return False

is_divisible(3, 5, 7)


# #მოკლე ვერსია 1:
def is_divisible(n,x,y):
    return  n  % x == 0 and n % y == 0

is_divisible(3, 5, 7)



# 2
# მოკლე ვერსიაა
def array_plus_array(arr1,arr2):
    return sum(arr1) + sum(arr2)

array_plus_array()

#3
def feast(beast, dish):
    beast_first_and_last = beast[0] + beast[-1]
    dish_first_and_last = dish[0] + dish[-1]
    return beast_first_and_last == dish_first_and_last       

feast('Kochalidze', 'Giga')



#4
def say_hello(name, city, state):
    name1 = ""
    for i in name:
        name1 += i + " "
    name1 = name1[:-1]
    return f"Hello, {name1}! Welcome to {city}, {state}!"



#5
def points(games):
    score=0
    for i in games:
        i= i.split(":")
        if i[0] > i[1]:
            score += 3
        elif i[0] == i[1]:
            score += 1
    return score


