#გამოვიტანოთ რიცხვები-0 დან 20-ის ჩათვლით

for i in range(21):
    print(i)

#მომხმარებელს შემოვატანინოთ რიცხვი და დაპრინტეთ შემოტანილი რიცხვი ლუწია თუ არა

num = int(input("enter your number: "))
if num % 2 == 0:
    print("number is even")

else:
   print("number is odd")


#დავპრინტოთ 20 მდე ლუწი რიცხვები

for i in range(21):
   if i % 2 == 0:
        print(i)


#50-დან 100-ის ჩათვლით არსებული ყველა რიცხვი დავაჯამოთ
for i in range(50,100):
    print(i + i)


#დაწერეთ ალგორითმი რომელიც ბეჭდავს 5-ის ჯერად რიცხვებს (რიცხვები რომლებიც იყოფა 5-ზე) 1-დან 50-ის ჩათვლით
for i in range(51):
    if i % 5 == 0:
        print(i)


#მომხმარებლეს შემოვატანინოთ ორი რიცხვი და დავწეროთ რომელია მათგან უდუდესი და რომელი უმცირესი

num1 = int(input("enter a first number: "))
num2 = int(input("enter a second number:"))

if num1 > num2:
    print("Num1 is greater than num2 ")

if num1 < num2:
    print("Num2 is greater than num1")

for i in range(num1,num2):
    print(i)


# გადავიმეოროთ განვლილი მასალა და გაავაკეთოთ მაგალითები
#True end folse

print(5 > 6 and 5 < 6)

print(5 > 6 or 5 < 6)

#for ციკლი (10-მდე ყველა ნატურალური რიცხვი)
for i in range(10):
    print(i)

#for ციკლი (50-დან 100-მდე)
for i in range(50,100):
    print(i)

#float (სტრინგის გარდაქმნა ათწილადად)
print(float("5"))

#float (ინტეჯერის გარდაქმნა ათწილადად)
print(float(5))




# ალგორითმი, რომელიც დაბეჭდავს 5-იდან ათის ჩათვლით რიცხვების ნამრავლს
for i in range(5,11):
    print(i * i)
















