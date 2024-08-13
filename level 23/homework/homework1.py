# შექმენით ფუნქცია რომელსაც გადაეცემა 2 რიცხვი. ფუნქციამ უნდა ჩაატაროს ყველა არითმეტიკული მოქმედება ამ ორ რიცხვს შორის.
def two_num(num, num1):
    print(num + num1)
    print(num - num1)
    print(num * num1)
    print(num / num1)
    print(num // num1)
    print(num % num1)

two_num(5 , 10)




#შექმენით ფუნქცია რომელსაც გადაეცემა ორი რიცხვი. ამ ფუნქციამ პირველ რიცხვს მანამ უნდა დაუმატოს მეორე რიცხვი სანამ ჯამი არ გახდება 100ის ტოლი ან 100ზე მეტი.

def Two_num(num11, num12):

    print(num11 + num12)

    while (num11 + num12) >= 100:
        print(num11 + num12)
        

Two_num(40, 30)




#3) შექმენით ფუნქცია რომელიც ამოწმებს რიცხვი კენტია თუ ლუწი.

def odd_even(number14):
    if number14 % 2 == 0:
      print("even")

    else:
      print("odd")
odd_even(51)



#4) შექმენით ფუნქცია რომელსაც გადაეცემა ლისტი. ფუნქციამ უნდა იპოვოს ლისტში უდიდესი რიცხვი.

def list20(num25, num26, num27, num28, num29, num30):
    num66 = [num25, num26, num27, num28, num29, num30]
    print(max(num66))

list20(2, 5, 7, 34, 56, 9)



#5) შექმენით ფუნქცია რომელსაც გადაეცემა ლისტი. ფუნქციამ უნდა იპოვოს ამ ლისტში შემავალი რიცხვების ჯამი

def list20(num45, num46, num47, num48, num49, num50):
    num77 = [num45, num46, num47, num48, num49, num50]
    print(sum(num77))

list20(12, 20, 5, 10 ,15, 10)



#6) შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგები და ინტეჯერები რაღაც თანმიმდევრობით. 
# ფუნქციამ უნდა შეძლოს და ეს სტრინგების და ინტეჯერების თანმიმდევრობა უნდა გამოიტანოს შებრუნებულად.

def strings_integers(num00, nam00, num44, num43, nam01):
    print(num00, nam00, num44, num43, nam01)
    print(nam01, num43, num44, nam00, num00)


strings_integers(15, 'Giga', 50, 43, 'NIni')




#7) შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგების ლისტი. ამ ფუნქციამ უნდა იპოვოს ყველაზე გრძელი და ყველაზე მოკლე სტრინგები ამ ლისტში.

def longest_shortest_integer(num001, num002, num003, num004, num005):
    num0001 = [num001, num002, num003, num004, num005]
    print(num0001)
    print(max(num0001))
    print(min(num0001))

longest_shortest_integer(45, 245, 321, 12, 324)



#8) შექმენით ფუნქცია რომელსაც გადაეცემა რაიმე სტრინგი. ამ ფუნქციამ უნდა შეძლოს და თითოეული ასო შეცვალოს (პატარა ასო დიდი ასოთ a-A ხოლო დიდი ასო 
# პატარათი A-a).

def uppercase(name):
    print(name.upper())

uppercase('Kochalidze')




#9) შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგი. ამ ფუნქციის მეშვეობით უნდა დაითვალოთ თანხმოვნების რაოდენობა ამ სტრინგში.

def Consonants(name98):
    
    print(name98)
    print('i', 'a')
        

Consonants('giga')



#10) შექმენით ფუნქცია რომელსაც გადაეცემა ინტეჯერი და თუ ლუწია აბრუნებს True-ს ხოლო თუ კი კენტია აბრუნებს False

def odd_evem(number24):
    return number24 % 2 == 0

print(odd_evem(101))



#11)შექმენით ფუნქცია, რომელსაც გადაეცემა მთელი რიცხვების სია. თქვენი დავალებაა, რომ ამ სიის ლუწ ინდექსებზე მყოფი რიცხვების ჯამი დააბრუნოთ. 
# აუცილებლად გამოიყენეთ return ამ და ასევე შემდეგ დავალებებში.

def list_of_integers():

    nume980 = int(input('Enter first number: '))
    nume981 = int(input('Enter second number: '))

    num001 = []
   

    for i in range(nume980, nume981):
        num001.append(i)
    
        if i % 2 ==0 :
            print(i + i)
        else:
            print('nothing')

    print(num001)

list_of_integers()



#12)შექმენით ფუნქცია, რომელსაც გადაეცემა მთელი რიცხვი. თქვენი დავალებაა, რომ დააბრუნოთ ლუწია თუ კენტი ის.

def odd_evem(num003):
    if num003 % 2 == 0:
        print('even')
    else:
        print('Odd')

odd_evem(45)




#13)შექმენით ფუნქცია, რომელიც დააბრუნებს მარტივია თუ არა რიცხვი (მარტივია რიცხვი, თუ მას მარტო ორი გამყოფი აქვს).


def Simple_and_complex_number(num0002):

    if num0002 / 1 and num0002 / num0002:
        print('Simple')
    else:
        print('complex')

Simple_and_complex_number(9)





#14)შექმენით ფუნქცია, რომელსაც გადაეცემა სახელების სია. თქვენი დავალებაა, რომ დააბრუნოთ ამ სიის განახლებული ვერსია, სადაც ყველა სახელი დიდი ასოთი დაიწყება.


def Name_in_capital_letter():

    names00004 = []

    name003 = input('Enter first name: ')
    name004 = input('Enter second name: ')
    name005 = input('Enter Third name: ')
    name006 = input('Enter Fourth name: ')
    
    names00004.append(name003)
    names00004.append(name004)
    names00004.append(name005)
    names00004.append(name006)
    print(names00004)


    names000042 = []

    names000042.append(name003)
    names000042.append(name004)
    names000042.append(name005)
    names000042.append(name006)

    print(names000042)

Name_in_capital_letter()





#15)შექმენით ფუნქცია, რომელსაც გადაეცემა მთელი რიცხვების სია. შემდეგ გამოიყენეთ ციკლი, რათა განიხილოთ ამ სიის ყველა 
# რიცხვი - თუ რიცხვი ლუწია, ახალ სიაში დაამატეთ მისი განაყოფი ორზე, ხოლო თუ კენტია, მაშინ რიცხვის ნამრავლი ორზე. საბოლოოდ დააბრუნეთ განახლებული სია/ 

def numbers_list(num012, num013, num014, num015):
    nums023 = [num012, num013, num014, num015]
    print(nums023)
    nums0023 = []
    for i in range(num012, num013, num014, num015):
        
            
        print(nums0023)

numbers_list(3, 6, 5, 2)



#16)შექმენით ფუნქცია, რომელსაც გადაეცემა სტრინგი და დააბრუნეთ ეს სტრინგდი შებრუნებულ + დიდი ასოებით (reversed / upper). 

def strring(namee1):
    word77 = namee1
    reversed_word = ""

    for i in range(len(word77) - 1, -1, -1):
        reversed_word += word77[i]

    print(reversed_word)
    print(word77.upper())

strring('Giga')

