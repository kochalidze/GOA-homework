# 2) შექმენით ფუნქცია რომელსაც გადაეცემა სახელის არგუმენტი და გამოიტანს ამ სახელის მისალმებას (მაგ: "გამარჯობა, ლაშა")
# (ვოიდ ფუნქცია)
def greet(name):
    print("გამარჯობა", name)

greet("გიგა")



# 3) შექმენით ფუნქცია რომელიც აბრუნებს გადაცემულ რიცხვზე ერთით მეტს (მაგ: 55->56)  (ჩვეულებრივი ფუნქცია)
# 
def number(number):
    return number + 1

result = number(55)
print(result)



# 4) შექმენით ფუნქცია რომელიც აბრუნებს არა-ნეგატიური რიცხვის ნეგატიურ ვერსიას და შემდეგ გამოიყენეთ 
# ეს ფუნქცია რომ გამოიტანოთ დაბრუნებულზე ერთით მეტი რიცხვი (მაგ: თუ ფუნქციას გადავეცით 44 
#  საბოლლოდ უნდა გამოვიტანოთ (კონსოლში) -43 ) (ჩვეულებრივი ფუნქცია)

def num(number):
    if number >= 0:
        return -number
    return number

print(num(55 - 1))
