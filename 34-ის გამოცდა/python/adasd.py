# ფუნქცია რომელდაც გადაეცემა სამი არგუმენტი 
# (რიცხვი , მეორე რიცხვი, მათემატიკური სიმბოლო 
# (მიმატება, გამრავლება, გამოკლება, გაყოფა) და აბრუნებს შესაბამის შედეგს
# თუ არ იყოფა ორი რიცხხვი ან არ არის შესაბამისი არგუმენტები გადმოცემული გამოიტანოს ერორი

def operation(num1, num2, symbol):

    if symbol == '+':
        return num1 + num2
    elif symbol == '-':
        return num1 - num2
    elif symbol == '*':
        return num1 * num2
    elif symbol == '/':
        return num1 / num2
    else:
        return "Error: Invalid symbol"
    

print(operation(100, 50, '+'))
print(operation(100, 50, '-'))
print(operation(100, 50, '*'))
print(operation(100, 50, '/'))