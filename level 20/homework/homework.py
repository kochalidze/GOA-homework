#შექმენით ფუნქცია hello() სადაც print ფუნქციის გამოყენებით გამოიტანთ  "GOA Best!"
def hello():
    print("GOA Best!")
hello()    



#შექმენით ფუნქცია sum რომელიც მიიღებს ორ არგუმენთ მაგ: a , b  და შემდეგ print-ის გამოყენებით გამოიტანთ მათ ჯამს
def sum(a, b):
    print(a , b)

sum( 5 + 6 )
   



# შექმენით ფუნქცია to_string რომელიც მიიღებს ერთ არგუმენტს მაგალითად value  რომელსაც დაბეჭდავთ სტრინგად str-ის გამოყენებით
def to_string(vallue):
    print(vallue)

to_string("vallue")





#შექმენით ფუნქცია print_type რომელიც მიიღებს ერთ არგუმენტს და შემდეგ built-in function  type() გამოყებით შეამოწმებთ მის მონაცემთა ტიპს და გამოიტანთ ეკრანზე
def print_type(name):
      print(name)         
                 
print_type(type("Giga"))




#შექმენთ ფუნქცია to_integer რომელიც მიიღებს ერტ არგუმენტს მაგალითად value ისევ და შემდეგ print-ის გამოყენებით გამოიტანეთ ინტეჯერად int ფუნქციით
def to_integer(value):
    print(value)
    
to_integer(int("10"))
