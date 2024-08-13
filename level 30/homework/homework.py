#შექმენიტ ფუნქცია სახელად odd_index_sum რომელსაც გადაეცემა რიცხვების სია, თქვენი დავალებაა შეკრიბოთ ყვლა ის რიცხვი რომელიც დგას 
# !!!!კენტ ინდექსზე!!!!, მიღებული ჯამი დააბრუნეთ ფუნქციიდან

def odd_index_sum(num, num1, num2, num3, num4, num5, num6, num7, num8):

    numbers_list = [num, num1, num2, num3, num4, num5, num6, num7, num8]

    print(numbers_list[0] + numbers_list[2] + numbers_list[4] + numbers_list[6] + numbers_list[8])
    

odd_index_sum(3, 6, 9, 7, 11, 56, 23, 15, 17)

