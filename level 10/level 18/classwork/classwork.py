 #შევქმნათ პროგრამა რიცხვებზე (1-დან 10-მდე)
numbers = []

for i in range(1,10):
    numbers.append(i)

print(numbers)
print(len(numbers))



#შექმენით ისეთ პროგრამა რომელიც მომხმარებელს შემოატანინებს 2 რიცხვს
start = int(input("enter number: "))
end = int(input("enter number: "))

numbers1 = []

for i in range(start, end):
    numbers.append(i)

print(numbers)


#შექმენით პროგრამა სადაც მომხმარებელი შემოიტანს ორ რიცხვს საწყისი რიცხვი და ბოლო რიცხვი

start = int(input("enter number: "))
end = int(input("enter number: "))


number = []

for i in range(start, end):
    number.append(i)

print(max(number))
print(max(number))
print(sum(number)) 

#შექმენით პროგრამა სადაც მომხმარებელს შეეკითხებით რამდენი რიცხვის 

num1 = int(input("enter number" ))

numbers = []

for i in range(num1):
    num = int(input("please neter number" + str(i + 1) + ": "))
    numbers.append(num)

print(sum(numbers))

#შექმენით სია სადაც შეიტანთ თქვენი საყვარელი მანქანების სახელებს მინიმუმ 5 ელემეტნი.
#cars_names = ["Mersedes", "BMW", "Subaru", "audi", "Rols Roisi"]

#print(cars_names[0:3])
#print(cars_names[-3])
#print(cars_names[-4])


#შექმენით სია სადაც გექნებათ თქვენი სახელი გამეორებული ორჯერ.
