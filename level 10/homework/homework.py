#0-იდან 20-ის ჩათვლით დავპრინტოთ ყველა მთელი რიცხვი

for i in range(21):
    print(i)
    

#დავპრინტოთ პირველი 10 ნატურალური რიცხვი
for i in range(10):
    print(i)


#დავპრინტოთ 0-იდან 100-ის ჩათვლით ლუწი რიცხვები
 
for i in range(100):
     if i % 2 == 0:
         print(i)

#შემოატანინეთ მომხმარებელს რიცხვი და დაადგინეთ არის თუ არა დადებითი უარყოფითი ან ნულის ტოლი 

num1 =int(input("please enter your number: "))
if num1 > 0:
    print("positive")

if num1 < 0:
    print("negative")

if num1 == 0:
    print("is equal to zero")

#შემოვატანინოთ მომხმარებელს მისი ასაკი

nam1 = int(input("pleae enter your age: "))

if nam1 > 18:
    print("you are adult")


if nam1 < 18:
    print("you are virgin")


#დავწეროთ ისეთი პროგრამა რომელიც მომხმარებელს უპრინტავს კვირის დღეს 

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