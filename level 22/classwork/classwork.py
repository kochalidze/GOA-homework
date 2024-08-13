#1) შექმენით ფუნქცია რომელსაც დაარქმევთ Calculate_average სადაც იქნება ერთი სია შექმნილი სახელად numbers 
#  თქვენი დავალება არის გამოთვალოთ ამ რიცხვების საშუალო არითმეტიკული გამოიყენეთ  sum და len ფუნქციები

def Calculate_average():

    num = int(input('Enter first number: '))
    num1 = int(input('Enter second number: '))

    numbers = []
    
    for i in range(num, num1):
        numbers.append(i)

    print(numbers)
    print(sum(numbers) / len(numbers))

Calculate_average()



#2)შექმენით ფუნქცია manual_sum ჩვენი ფუნქცია მიირესბს ერთ მნიშვნელბას სიას. თქვენი დავალება არის გაიგოთ ამ სიის რიცხვთა ჯამი გაიგოთ for ციკლის მეშვეობით

def manual_sum():

    num01 = int(input('Enter first number: '))
    num02 = int(input('Enter second number: '))

    numbers01 = []

    for i in range(num01, num02):
        numbers01.append(i)

    print(numbers01)
    print(sum(numbers01))
    

manual_sum()




#3) შექმენით  მისალმების ფუნქცია სახელად greet რომელიც მიესალმება მომხმარებელს და default მნიშვნელობად იქნება hello guest

def greet(nam = 'Guest'):
    print('hello', nam)

greet('Giga')
greet()
    


#4) შექმენით ფუნქცია რომელსაც გადაეცემა ორი მნიშვნელობა firstnum და secondnum და თქვენი დავალებაა იპოვოთ ამ რიცხვებს შორის ყველა რიცხვის ჯამი

def firstnum_secondnum(firstnum, secondnum):
    for i in range(firstnum, secondnum):
        print(i + i)

firstnum_secondnum(2, 8)




#5) შექმენით ფუნქცია რომელსაც გადაეცემა ლისტი. თქვენი დავალებაა ამ ლისტიდან ამოიღიოთ ყველა ციფრი და დაახარისხოთ ისინი კენტებად და ლუწებად

def odd_even2(num010, num020, num030, num040):
    number03 = [num010, num020, num030, num040]
    print(number03)
    print(number03[0])
    print(number03[1])
    print(number03[2])
    print(number03[3])

    print(number03[0] % 2  == 0)
    print(number03[1] % 2  == 0)
    print(number03[2] % 2  == 0)
    print(number03[3] % 2  == 0)

        
odd_even2(45, 12, 99, 11)




#6) შექმენით ფუნქცია print_numbers რომელიც მიიღებს n მნიშვნელობას და გამოიტანს 1 დან ამ n რიცხვამდე ყველა რიცხვს for loop ის გამოყენებით 

def print_numbers(n):

    for i in range(1, n):
        print(i)

print_numbers(9)



# 7) შექმენით ფუნქცია  print_even_numbers რომელიც მიიღებს ერთ პარამეტრს n შემდეგ გამოიტანს 2 დან ამ რიცხვამდე ყველა ლუწ რიცხვს გამოიყენეთ for loop 
def print_even_numbers(n):

    print(n)

    for i in range(2, n):
        print(i % 2 == 0)
    
print_even_numbers(9)




# 8) შექმენით ფუნქცია რომელსაც დაარქმევთ sum(ჯამი) ეგ ფუნქცია მიიღებს ორ რიცხვს პარაამეტრებს გაუწერეთ num1 და num2 თქვენი დავალებაა ამ ორი რიცხვის ჯამი დაბეჭდეთ
def sum(num1, num2):

    print(num1 + num2)

sum(3, 8)



# 9) შექმენით ფუნქცია რომელსაც დაარქმევთ sum(ჯამი) ეგ ფუნქცია მიიღებს ორ რიცხვს პარაამეტრებს გაუწერეთ num1 და num2 თქვენი დავალებაა ამ ორი რიცხვის ჯამი დააბრუნოთ

def sum1(num11, num12):

    return num11 + num12

sum1(3, 8)




#10) შექმენით ფუნქცია რომელიც დაბეჭდავს ორი სტრინგის გაერთიანებას მაგალითად str1  და str2 და დაბეჭდეთ მათი შეერთება ფუნქციას დაარქვით joined_string

def joined_string():

    nam = input('Enter name: ')
    last_nam = input('Enter last name: ')

    print(nam, last_nam)

joined_string()


#2)შექმენით ფუნქცია manual_sum ჩვენი ფუნქცია მიირესბს ერთ მნიშვნელბას სიას. თქვენი დავალება არის გაიგოთ ამ სიის რიცხვთა ჯამი გაიგოთ for ციკლის მეშვეობით

def manual_sum():

    num13 = int(input('Enter first number: '))
    num14 = int(input('Enter first number: '))

    numbers101 = []
    for i in range(num13, num14):
        numbers101.append(i)

    print(numbers101)

    for i in range(1):
        print(sum(numbers101))

manual_sum()



#3) შექმენით  მისალმების ფუნქცია სახელად greet რომელიც მიესალმება მომხმარებელს და default მნიშვნელობად იქნება hello guest

def greet(name = 'Guest'):
    print('hello', name)

greet('Giga')
greet()



#4) შექმენით ფუნქცია რომელსაც გადაეცემა ორი მნიშვნელობა firstnum და secondnum და თქვენი დავალებაა იპოვოთ ამ რიცხვებს შორის ყველა რიცხვის ჯამი

def firstnum_secondnum(firstnum, secondnum):
    for i in range(firstnum, secondnum):
        print(i + i)

firstnum_secondnum(2, 8)


#5) შექმენით ფუნქცია რომელსაც გადაეცემა ლისტი. თქვენი დავალებაა ამ ლისტიდან ამოიღიოთ ყველა ციფრი და დაახარისხოთ ისინი კენტებად და ლუწად
def odd_even(num010, num020, num030, num040):
    number03 = [num010, num020, num030, num040]
    print(number03)
    print(number03[0])
    print(number03[1])
    print(number03[2])
    print(number03[3])

    print(number03[0] % 2  == 0)
    print(number03[1] % 2  == 0)
    print(number03[2] % 2  == 0)
    print(number03[3] % 2  == 0)

        
odd_even(4, 66, 77, 33)



#6) შექმენით ფუნქცია print_numbers რომელიც მიიღებს n მნიშვნელობას და გამოიტანს 1 დან ამ n რიცხვამდე ყველა რიცხვს for loop ის გამოყენებით 

def print_numbers(n):

    for i in range(1, n):
        print(i)

print_numbers(10)



#7) შექმენით ფუნქცია  print_even_numbers რომელიც მიიღებს ერთ პარამეტრს n შემდეგ გამოიტანს 2 დან ამ რიცხვამდე ყველა ლუწ რიცხვს გამოიყენეთ for loop

def print_even_numbers(n):

    print(n)

    for i in range(2, n):
        print(i % 2 == 0)
    
print_even_numbers(9)



#8) შექმენით ფუნქცია რომელსაც დაარქმევთ sum(ჯამი) ეგ ფუნქცია მიიღებს ორ რიცხვს პარაამეტრებს გაუწერეთ num1 და num2 თქვენი დავალებაა ამ ორი რიცხვის ჯამი დაბეჭდეთ

def sum(num1, num2):

    print(num1 + num2)

sum(3, 8)




#9) შექმენით ფუნქცია რომელსაც დაარქმევთ sum(ჯამი) ეგ ფუნქცია მიიღებს ორ რიცხვს პარაამეტრებს გაუწერეთ num1 და num2 თქვენი დავალებაა ამ ორი რიცხვის ჯამი დააბრუნოთ

def sum1(num11, num12):

    return num11 + num12

sum1(3, 8)



#10) შექმენით ფუნქცია რომელიც დაბე#ჭდავს ორი სტრინგის გაერთიანებას მაგალითად str1  და str2 და დაბეჭდეთ მათი შეერთება ფუნქციას დაარქვით joined_string

def joined_string():

    nam = input('Enter name: ')
    last_nam = input('Enter last name: ')

    print(nam, last_nam)

joined_string()



#11) შექმენით ფუნქცია find_maximum რომელსაც გადაასცემთ ორ მნიშვნელობას მაგალიტად num1 და num2 შემდეგ დააბრუნეთ აქედან რომელიც უფრო მეტია

def find_maximum():
    number1 = int(input('Enter first number: '))
    number2 = int(input('Enter second number: '))

    if number1 > number2:
        print(number1)
    else:
        print(number2)

find_maximum()



#12)შექმენით ფუნქცია reverse_string და მიიღებს ერთ მნიშვნელობას str მაგალითად შემდეგ დააბრუნეთ ეს სტრინგი შებრუნებულად

def string():
    word = "kochalidze"
    reversed_word = ""

    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]

    print(reversed_word)
    
string()
    
    


# 13. დაწერეთ პითონის ფუნქცია, რომელიც ითვლის მართკუთხედის ფართობს მისი სიგრძისა და სიგანის პარამეტრების მიხედვით.

def Rectangle_area():

    Length = int(input('Enter Length: '))
    Width = int(input('Enter Width: '))

    print(Length * Width)

Rectangle_area()

   

# 14. შექმენით ფუნქცია, რომელიც ამოწმებს არის თუ არა მოცემული რიცხვი მარტივი.

def simple_number():

    number001 = int(input('Enter number: '))

    if number001 / 2 and number001:
        print('Simple number')
    else:
        print('Compound number')

simple_number()




# 15. შექმენით ფუნქცია, რომელიც შეყვანის სახით იღებს რიცხვების სიას და აბრუნებს სიაში ყველა რიცხვის ჯამს.

def list():

    number_list = int(input('Enter number: '))
    number_list2 = int(input('Enter number: '))
    
    number_list3 = []

    for i in range(number_list, number_list2):
        number_list3.append(i)

    print(number_list3)
    print(sum(number_list3))
        
list()



# 16. დაწერეთ ფუნქცია, რომელიც იღებს სტრიქონს და ითვლის ხმოვანთა რაოდენობას (a, e, i, o, u) სტრიქონში.

def string05(strl_nam):
    Voices = 'a', 'e','i', 'o', 'u'
    if strl_nam == Voices:
       return len(Voices)
string05('Giga')



# 17. განსაზღვრეთ ფუნქცია, რომელიც იღებს სტრიქონების ჩამონათვალს და აბრუნებს ახალ სიას ყველა სტრიქონის დიდი ასოებით.

def string2(name0101, nqme0202, name0303, name0404):

    strings_list = [name0101, nqme0202, name0303, name0404]
    print(strings_list)

    strings_list2 = [name0101, nqme0202, name0303, name0404]
    print(strings_list2)

    strings_list2.lower()
                    
    

string2('giga', 'nini', 'naira', 'ana')




