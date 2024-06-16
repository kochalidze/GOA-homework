#დავბეჭდოთ ჩვენი სახელი 10 ჯერ while ციკლის გამოყენებით
num = 0

while num != 10:
    print("Giga")
    num = num + 1


#0 დან 10 ის ჩათვლით შევკრიბოთ ყველა ლუწი რიცხვი და დავბეჭდოთ ჯამი

num = 0
sum = 0

while num <= 10:
    sum = sum + num
    num = num + 2

print(sum)  

#შევქმნათ პროგრამა რომელსაც ჰქვია guess game,  მომხმარებელს იქამდე შემოატანინოთ რიცხვი სანამ არ გამოიცნობს რიცხვ 5_ს, როცა გამოიცნობს ტერმინალში დავუბეჭდოთ რომ მან მოიგო, სხვა შემთხვევაში დავუბეჭდოთ რომ მან წააგო
#Guess Game
number = 0

while number <= 5:
    num = int(input("please enter your number: "))
    if num == 5:
        print("you won")
    else:
        print("try again")
