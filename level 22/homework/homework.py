# #შექმენით ფუნქცია, რომელიც იღებს რაიმე რიცხვს და აბრუნებს მასზე 5'ით მეტს.

def print_num(num):
    for i in range(num):
        print(i * 5)

print_num(5)



# #შექმენით ფუნქცია, რომელიც იღებს ორ integer'ს და აბრუნებს მათ ნამრავლს

def two_integer(start, end):
        print(start * end)

two_integer(40, 4)   
     


# #შექმენით ფუნქცია, რომელიც იღებს string'ს ამ string'ის სიგრძეს (გამოიყენეთ ფუნქცია len()).

def string(name):
    print(name)

string('Giga')
string(len('Giga'))




# #შექმენით ფუნქცია, რომელიც იღებს string'ების list'ს და აბრუნებს ამ string'ების სიგრძეების list'ს (გამოიყენეთ ფუნქცია len()).

def string_list(name1):
    print(name1)
    print(len(name1))

string_list('Nini')
string_list('Giga')
string_list('Barbare')




# #შექმენით ფუნქცია, რომელიც იღებს string'ს და აბრუნებს True-ს თუ ის არის Palindrome (ანუ იგივენაირად იკითხება მარცნიდანაც და მარჯვნიდანაც მაგალითად: "wow") და სხვა შემთხვევაში False-ს.

def is_palindrom(s):
    return s == s[::-1]

print(is_palindrom('wow'))
print(is_palindrom('hello'))
print(is_palindrom('madam'))
print(is_palindrom('racecar'))



# #შექმენით ფუნქცია, რომელიც პოულობს ყველაზე გრძელ string'ს string'ების სიაში.

def string_list(name):
    print(name)
string_list(max('Giga', 'Kochalidze', 'Nini'))




# #შექმენით ფუნქცია, რომელიც იღებს რიცხვს და აბრუნებს მის factorial'ს (რა არის ფაქტორიალი: https://en.wikipedia.org/wiki/Factorial).

def number(start_num, end_num):
    for i in range(start_num, end_num):
        print(i)


number(4, 9)
    



# #შექმენით ფუნქცია, რომელიც იღებს 2 integer'ების list'ს და აბრუნებს ორივე list'იდან მაქსიმალური რიცხვების ჯამს.

def Two_integer(num11, num22):
    print(max(num11) + max(num22))
    print((num11[-1]) + (num22[-1]))

Two_integer([1, 2, 3, 4, 5], [10, 11, 12, 13, 14])





# #შექმენით ფუნქცია, რომელიც იღებს 2 integer'ების list'ს და აბრუნებს ორივე list'იდან მინიმალური რიცხვების სხვაობას.

def Two_integer(num33, num44):
    print(min(num33) - min(num44))

Two_integer([1, 2, 3, 4, 5], [10, 11, 12, 13, 14])






# #10. შექმენით ფუნქცია, რომელიც იღებს integer'ების list'ს და აბრუნებს ამ სიაში მაქსიმალური და მინიმალური რიცხვების სხვაობას.

def Two_integer(num55, num66):
    print(max(num55) - min(num66))

Two_integer([1, 2, 3, 4, 5], [10, 11, 12, 13, 14])




# #11. შექმენით ფუნქცია, რომელიც იღებს integer'ების list'ს და აბრუნებს ყველა ელემენტის ჯამს.

def Two_integer(num77):
    print(sum(num77))

Two_integer([1, 2, 3, 4, 5, 6, 7, 8])



# #12. შექმენით ფუნქცია, რომელიც იღებს string'ს და აბრუნებს ხმოვანი ასოების რაოდენობას string'ში.
#       dasaweria
def string_vowel(v):
    return v == 'a', 'e', 'i', 'o', 'u'

string_vowel('kochalidze')



#13. შექმენით ფუნქცია, რომელიც იღებს integer'ების list'ს და აბრუნებს ახალ list'ს თითოეული integer'ის კვადრატით. (მაგალითად: input: [2, 4]. output: [4, 16])

def integer_list(num88, num99, num00):
    print(num88, num99, num00)
    print(num88 **2, num99 **2, num00 **2)
    
integer_list(5, 6, 7)




#14. შექმენით ფუნქცია, რომელიც იღებს string's და აბრუნებს მის შებრუნებულს.

def string():
    word = "example"
    reversed_word = ""

    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]

    print(reversed_word)
    
string()



#15. შექმენით ფუნქცია, რომელიც იღებს რაიმე integer'ს და თუ ლუწია აბრუნებს True'ს, თუ კენტი False'ს.
#პირველი ხერხი
def odd_even(number14):
    if number14 % 2 == 0:
      print("True")

    else:
      print("False")
odd_even(100)

#მეორე ხერხი
def odd_evem(number24):
    return number24 % 2 == 0

print(odd_evem(100))



#16. შექმენით ფუნქცია, რომელიც იღებს string'ების სიას და აბრუნებს ყველაზე გრძელ string'ს.

def long_string(num55, num66, num77, num88):
    print([num55, num66, num77, num88])
    print(max(num55, num66, num77, num88))

long_string('Maxaradze', 'Nini', 'Kochalidze', 'Ana')  



#17. შექმენით ფუნქცია, რომელიც იღებს მთელი რიცხვების სიას და აბრუნებს სიაში ყველაზე მცირე რიცხვს.

def little_number(number55, number66, number77, number88):
    print([number55, number66, number77, number88])
    print(min(number55, number66, number77, number88))

little_number(5, 2, 7, 8,)



# #18. შექმენით ფუნქცია, რომელიც იღებს ორ integer'ს და აბრუნებს მათ უდიდეს საერთო გამყოფს (GCD-Greatest common divisor).

def Two_integers(num01010, num02020):
    print(num01010, num02020)

    print((num01010, num02020) / 4)



Two_integers(8,  12)


# #19. შექმენით ფუნქცია, რომელიც იღებს string'ს და აბრუნებს იმავე string'ს uppercase'ში. (მაგალითად: input: "Hello World". output: "HELLO WORLD".

def string_uppercase(name):
    print(name.upper())
string_uppercase('Kochalidze')



#20. შექმენით ფუნქცია, რომელიც იღებს integer'ების სიას და აბრუნებს მათ საშუალო არითმეტიკულს.(მაგალითად: input: [1, 5, 12]. output: (1 + 5 + 12)/3, ანუ 6.) (ელემენტების დასათვლელად გამოიყენეთ ფუნქცია len).

def integer_list11(number34, number35, number36, number37, number38):
    numbers2 = [number34, number35, number36, number37, number38]
    print(sum(numbers2) / len((numbers2)))

integer_list11(5, 8, 9, 23, 56)
