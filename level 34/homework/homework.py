#2) განიხილეთ და კომენტარებით ახსენით როგორ მუშაობს გაკვეთილზე დაწერილი კოდი:

def find_short(s):
    list1 = s.split(" ")

    word_len = len(list1[0])
    for i in list1:
        if len(i) < word_len:
            word_len = len(i)
    
    # word_len = 3
    return word_len

print(find_short("bitcoin take over the world maybe who knows perhaps"))

#შევქმენით ფუნქცია სახელად find_short და ამ ფუნქციას და გავეცით s 
# შემდეგ .split(" ")-ის გამოყენებით s-ში ჩაწერილ წინადადებას დავწობთ სიტყვებად და ჩაიწერე




#3) იმუშავეთ split-ის გამოყენებაზე: შექმენით 10 string და თითოეულზე გამოიყენეთ split ბრძანება, მოახდინეთ გახლეჩვა ნებისმიერი სიმბოლოთი

def split(nam1, nam2, nam3, nam4, nam5, nam6, nam7):

    list = nam1.split('i')
    list1 = nam2.split('i')
    list2 = nam3.split('i')
    list3 = nam4.split('i')
    list4 = nam5.split('i')
    list5 = nam6.split('i')
    list6 = nam7.split('i')

    print(list)
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    print(list5)
    print(list6)


split('Giga', 'Nini', 'Naira', 'Ana', 'Rezi', 'Zviadi', 'Kochalidze')




#4) codewars-იდან გექნებათ 2 7კიუიანი ამოცანა:
#1) https://www.codewars.com/kata/5259b20d6021e9e14c0010d4
def reverse_words(text):
    words = text.split(' ')
    reversed_words = []
    for word in words:
        reversed_words.append(word[len(word):: -1])
    return ' '.join(reversed_words)


#2) https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc
def factorial(n):
    word = 1
    if n < 0 or n > 12:
        return Valuerror
    else:
        for i in range(1, n+1):
            word *= i
    return word
