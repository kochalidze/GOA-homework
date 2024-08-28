#გატესტეთ join და replace ფუნქციები, კომენტარებით ახსენით თუ როგორ მუშაობენ

#join
def join_list(list):
    return ' '.join(list)

print(join_list(['GOA', 'IS', 'BEST']))
#ჯერ ვუწერთ join ფუნქციას ბრჭყალებში იმ სიმბოლოს რომლითაც გვინდა ელემენტების გაერთიანება ანუ რა გვინდა რომ ჩავსვათ მათ შორის 



#replace
def replase_r(nam):
    return nam.replace('banana', 'Giga')

print(replase_r('me name is banana'))
#სანამ replace ფუნქციის სახლეს დავწერთ მანამდე უნდა დავწეროთ იმ კოლექციის სახლეი რომელზეც მოქმედებს, შემდეგ წერტილი და reflace, შემდეგ ფრჩხილები და 
# და მას ფრჩხილეში გადავცემთ ორ არგუმენტს. პირველი არის ის რისი ჩანაცვლებაც გვინდა შემდეგ მძიმით გამოვყოთ და მეორე არგუმენტი არის რითიც ვანაცვლებთ.



#3) შეასრულეთ codewars:
#1) https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python
def to_jaden_case(string):
    nam = string.split()
    new_nam = [i.capitalize() for i in nam]
    print(new_nam)
    return ' '.join(new_nam)


#2) https://www.codewars.com/kata/57f609022f4d534f05000024/train/python
def stray(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x
        

#3) https://www.codewars.com/kata/59f08f89a5e129c543000069/train/python
