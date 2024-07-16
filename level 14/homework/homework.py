#გავაკეთოთ 5 მაგალითი while ციკლზე

#მაგ: 1
num = 0

while num != 9:
   print("Giga")
   num = num + 1

#მაგ: 2
num1 = 1
while num1 < 6:
  print(num1)
  num1 = num1 + 1

#მაგ: 3
num2 = 0
while num2 <= 11:
   num2 = int(input("please enter your number: "))
   if num2 == 11:
       print("you won")
   else: 
       print("You lost")

#მაგ: 4

i = 1
while i < 6:
 print(i)
 if i == 6:
   break
 i = i + 1

#მაგ: 5
i = 0
while i < 6:
  i += 1
  if i == 3:
   continue
  print(i)

#გავაკეთოთ 5 მაგალითი for ციკლებზე
#მაგ: 1
for i in range(10):
    print(i)

#მაგ: 2
num3 = int(input("enter number: "))
num4 = int(input("enter second number: "))
for i in range(num3,num4):
    if num3 > num4:
        print("num3 is greater than num4")
    if num3 < num4:
        print("num3 is less than num4")

#მაგ: 3
for i in range(40):
   if i % 2 == 0:
        print(i)

#მაგ: 4
for i in range(20,40):
    print(i + i)

#მაგ: 5
for i in range(100):
    if i % 5 == 0:
        print(i)

#გავაკეთოთ 5 მაგალითი if-else
#მაგ: 1
num = int(input("enter your number: "))
if num % 2 == 0:
    print("number is even")

else:
   print("number is odd")

#მაგ: 2
num1 = int(input("enter a first number: "))
num2 = int(input("enter a second number:"))

if num1 > num2:
    print("Num1 is greater than num2 ")

if num1 < num2:
    print("Num2 is greater than num1")

#მაგ: 3
num1 =int(input("please enter your number: "))
if num1 > 0:
    print("positive")

if num1 < 0:
    print("negative")

if num1 == 0:
    print("is equal to zero")

#მაგ: 4
num1 = int(input("enter your number: "))

if num1 == 1:
    print("manday") 

if num1 == 2:
    print("tusday")

if num1 == 3:
    print("Wednesday")

if num1 == 4:
    print("Thursday")

if num1 == 5:
    print("Friday")

if num1 == 6:
    print("Saturday")

if num1 == 7:
    print("Sunday")

#მაგ: 5
num1 =int(input("please enter your number: "))
if num1 > 0:
    print("positive")

if num1 < 0:
    print("negative")

if num1 == 0:
    print("is equal to zero")