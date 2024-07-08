#თავიდან ბოლომდე გაიარეთ for ციკლები და გაააკეთეთ საავარჯიშოები ვესქულზე
#1 სავარჯიშო

name = ["Giga", "Nini", "Ana"]
for i in name:
  print(i)
  if i == "Nini":
   break


# მე-2 სავარჯიშო
num = int(input("enter number: "))

nums = []

for i in range(num):
 nums.append(i)
print(nums)

# მე-3 სავარჯიშო
for i in range(10, 20):
  print(i)



#თქვენი კრეატიულობით შექმენით პროგრამა სადაც გააერთიანებთ ფორ ციკლებს იფებს და სიებს, 
# გააკეთეთ მსგავსი პროგრამა მინიმუმ 3 ჯერ
#1 პროგრამა
num1 = int(input("entre first number: "))
num2 = int(input("enter second number: "))

for i in range(num1, num2):
   if i % 2 == 0:
       print(i)


while num1 < 25:
   print("Giga")
   num1 = num1 + 2


if num1 > num2:
   print("num1 is greater than num2")

elif num1 < num2:
   print('num2 is greater than num1')


number1 = int(input("enter number: "))
number2 = int(input("enter number: "))


number = []

for i in range(number1, number2):
   number.append(i)

print(len(number))
print(max(number))
print(sum(number)) 
print(len(number) - 1)



#2 პროგრამა

first_number = int(input("Enter pirst number: "))
second_number = int(input("Ente second number: "))

for i in range(first_number, second_number):
   print(i * i)

while second_number < first_number:
   print('first nimber is greater than second number')

for i in range(first_number, second_number):
   print(i)

num = []

for i in range(first_number):
    num.append(i)

print(num)
print(len(num) - 1)
print(num[0])
print(len(num))
print(max(num))
print(min(num))
print(sum(num))

#3 პროგრამა
nam = int(input("Enter pirst number: "))
nam1 = int(input("Ente second number: "))

Nam = []

for i in range(nam1):
    Nam.append(i)

Nam[0] + 12

print(Nam)
print(Nam[0])
print(max(Nam))
print(min(Nam))

while nam < 10:
    print("NINI")

for i in range(nam1):
    print(i)