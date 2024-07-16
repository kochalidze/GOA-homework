#1. Print numbers from 1 to 5 using a for loop.

for i in range(1, 5):
    print(i)


#2. Print numbers from 1 to 5 using a while loop.
num1 = 0

while num1 != 5:
    num1 = num1 + 1
    print(num1)




#3. Print each character in the string "hello" using a for loop

word = "hello"
index = 0

for i in range(index, len(word)):
    print(word[index])
    index += 1



#4. Print each character in the string "hello" using a while loop.

word = "hello"
index = 0

while index < len(word):
    print(word[index])
    index += 1


#5. Print the numbers 1, 2, 3 using a for loop.
for i in range(1, 4):
    print(i)



#6. Print the numbers 1, 2, 3 using a while loop.
num = 0
while num != 3:
    print(1)
    print(2)
    print(3)

    break




#7. Print "Python is fun" 3 times using a for loop.

for i in range(3):
    print("Python is fun")


#8. Print "Python is fun" 3 times using a while loop.
num = 0

while num != 3:
    print("Python is fun")
    num = num + 1



# 9. Print the elements of a list [1, 2, 3] using a for loop.

num1 = [1, 2, 3]

for i in range(1):
    print(num1[0])
    print(num1[1])
    print(num1[2])



# 10. Print the elements of a list [1, 2, 3] using a while loop.

num2 = [1, 2, 3]

while num2 != 3:
   print(num2[0])
   print(num2[1])
   print(num2[2])

   break



# 11. Print "hi" for each element in a list [1, 2, 3] using a for loop.

num4 = [1, 2, 3]
for i in range(1):
    print('hi ',  num4[0])
    print('hi ',  num4[1])
    print('hi ', num4[2])



# 12. Print "hi" for each element in a list [1, 2, 3] using a while loop.

num5 = [1, 2, 3]

while num5 != 3:
    print('hi', num5[0])
    print('hi ', num5[1])
    print('hi ',num5[2])

    break



# 13. Print the first 3 positive integers using a for loop.

for i in range(1, 4):
    print(i)




# 14. Print the first 3 positive integers using a while loop.
num10 = 0
while num10 != 3:
    num10 = num10 + 1
    print(num10)




# 15. Print the numbers from 1 to 3 in reverse using a for loop.

word = 9

for i in range(word - 1, -1, -1):
    print(i)
    


#16. Print the numbers from 1 to 3 in reverse using a while loop

word = 9

while word != 0:
    print(word - 1)
    print(word - 2)
    print(word - 3)
    print(word - 4)
    print(word - 5)
    print(word - 6)
    print(word - 7)
    print(word - 8)
    print(word - 9)

    break




# 17. Print the first 4 letters of the alphabet using a for loop.

num11 = 'a', 'b', 'g', 'd'
for i in range(1):
    print(num11)


#18. Print the first 4 letters of the alphabet using a while loop.
num11 = 'a', 'b', 'g', 'd'
while num11 != 4:
    print(num11)
    break


#19. Print the message "looping" 4 times using a for loop.

for i in range(4):
    print('looping')



#20. Print the message "looping" 4 times using a while loop

num = 0

while num != 4:
    print('looping')
    num = num + 1




#21. Print the elements of a tuple (1, 2, 3) using a for loop.

for i in range(1,4):
    print(i)



#22. Print the elements of a tuple (1, 2, 3) using a while loop.
num44 = 0
while num44 != 3 :
    num44 = num44 + 1
    print(num44)



# 23. Print the numbers 5, 4, 3, 2, 1 using a for loop.
def numbers0110(n):
    for i in range(n):
        if n < 0:
            n = n* -1
            return int(str(n)[::-1]) * -1
        return int(str(n)[::-1]) * -1
    
numbers0110(8)


#24. Print the numbers 5, 4, 3, 2, 1 using a while loop.

word = 9

while word -1  :
    print(i)
    
    break



# 25. Print the elements of the list ["apple", "banana", "cherry"] using a for loop.

for i in range(1):
    fruit = ["apple", "banana", "cherry"]
    print(fruit)



# 26. Print the elements of the list ["apple", "banana", "cherry"] using a while loop.

fruit2 = ["apple", "banana", "cherry"]

while fruit2 != 3:
    print(fruit2)
    break



# 27. Print the first 3 numbers starting from 0 using a for loop.

for i in range(3):
    print(i)




# 28. Print the first 3 numbers starting from 0 using a while loop.
num001 = 0
while num001 != 3:
    print(num001)
    num001 = num001 + 1



# 29. Print the word "loop" for each number in a list [1, 2, 3, 4] using a for loop.

list = [1, 2, 3, 4]

for i in range(1):
    print('loop', list[0])
    print('loop', list[1])
    print('loop', list[2])
    print('loop', list[3])



# 30. Print the word "loop" for each number in a list [1, 2, 3, 4] using a while loop.

list2 = [1, 2, 3, 4]

while list2 != 3:
    print('loop', list2[0])
    print('loop', list2[1])
    print('loop', list2[2])
    print('loop', list2[3])

    break



# 31. Print the characters of the string "abc" using a for loop.

word12 = "abc"
index = 0

for i in range(index, len(word12)):
    print(word12[index])
    index += 1



# 32. Print the characters of the string "abc" using a while loop.

word89 = "abc"
index = 0

while index < len(word89):
    print(word89[index])
    index += 1



# 33. Print the first 2 elements of a list ["x", "y", "z"] using a for loop.

list5 = ["x", "y", "z"]

for i in range(1):
    print(list5[0:2])



# 34. Print the first 2 elements of a list ["x", "y", "z"] using a while loop.

list6 = ["x", "y", "z"]

while list6 != 2:
    print(list6[0:2])
    break


# 35. Print the message "Hello World" 2 times using a for loop.

for i in range(2):
    print("Hello World")


# 36. Print the message "Hello World" 2 times using a while loop.

num0101 = 0
while num0101 != 2:
    print("Hello World")
    num0101 = num0101 + 1



# 37. Print the elements of a set {1, 2, 3} using a for loop.

for i in range(1):
    numbers001 = [1, 2, 3]
    print(numbers001)
    print(numbers001[0])
    print(numbers001[1])
    print(numbers001[2])



# 38. Print the elements of a set {1, 2, 3} using a while loop.

numbers00100 = [1, 2, 3]
while numbers00100 != 3:
    print(numbers00100)
    print(numbers00100[0])
    print(numbers00100[1])
    print(numbers00100[2])
    break



# 39. Print the elements of the dictionary {"a": 1, "b": 2} using a for loop.

for i in range(1):
    print("a :", 1)
    print("b :", 2)



# 40. Print the elements of the dictionary {"a": 1, "b": 2} using a while loop.

num01010 = 0
while num01010 != 2:
    print("a :", 1)
    print("b :", 2)
    break



# 41. Print the numbers 10, 20, 30 using a for loop.

for i in range(1,31):
    if i % 10 == 0:
        print(i)



# 42. Print the numbers 10, 20, 30 using a while loop.

num020 = 1
while num020 != 31:
    if num020 % 10 == 0:
         print(num020)
    num020 = num020 +1



# 43. Print "Done" after completing a for loop.

for i in range(2):
    print('Done')



# 44. Print "Done" after completing a while loop.

nam030 = 0
while nam030 != 2:
    print('Done') 
    nam030 = nam030 + 1



# 45. Print the elements of a nested list [[1, 2], [3, 4]] using a for loop.

for i in range(1):
    list0404 = [[1, 2], [3, 4]]
    print(list0404[0])
    print(list0404[1])



# 46. Print the elements of a nested list [[1, 2], [3, 4]] using a while loop.

list07077 = [[1, 2], [3, 4]]
num0223 = 0
while num0223 != 2:
    print(list07077[0])
    print(list07077[1])
    num0223 = num0223 + 1



# 47. Print the first 5 positive integers using a for loop.

for i in range(1, 6):
    print(i)



# 48. Print the first 5 positive integers using a while loop.
num011011 = 1
while num011011 != 6:
    print(num011011)
    num011011 = num011011 + 1



# 49. Print each character of the string "loop" using a for loop.

word1234 = "loop"
index = 0

for i in range(index, len(word1234)):
    print(word1234[index])
    index += 1




# 50. Print each character of the string "loop" using a while loop.

word890 = "loop"
index = 0

while index < len(word890):
    print(word890[index])
    index += 1