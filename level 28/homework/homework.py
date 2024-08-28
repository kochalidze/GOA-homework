#1) https://www.codewars.com/kata/5583090cbe83f4fd8c000051
def digitize(n):
    n = str(n)
    list1 = []
    for i in n:
        list1.append(int(i))
    return list(reversed(list1))



#2)   https://www.codewars.com/kata/53af2b8861023f1d88000832
def are_you_playing_banjo(name):
	if name[0] == 'R' or name[0] == 'r':
		return name + " plays banjo"
	else:
		return name + " does not play banjo"


#3)   https://www.codewars.com/kata/5672a98bdbdd995fad00000f

def rps(p1, p2):
    if p1 == 'scissors' and p2 == 'paper':
        return 'Player 1 won!'
    elif p1 == 'rock' and p2 == 'scissors':
        return 'Player 1 won!'
    elif p1 == 'paper' and p2 =='rock':
        return 'Player 1 won!'
    elif p1 == p2:
        return 'Draw!'
    else:
        return 'Player 2 won!'
    

#4)   https://www.codewars.com/kata/5ce9c1000bab0b001134f5af

def quarter_of(month):
        if month<=3:
            return 1
        elif month>=4 and  month<=6:
            return 2
        elif month<=9:
            return 3
        else:
            return 4
        

#5)   https://www.codewars.com/kata/5b077ebdaf15be5c7f000077

def count_sheep(n):
    ret = ""
    for i in range(1, n + 1):
        ret = ret + str(i) + " sheep..."
    return ret


#6)   https://www.codewars.com/kata/5772da22b89313a4d50012f7
def greet(name, owner):
    if (name == owner):
        return 'Hello boss'
    else:
        return 'Hello guest'
    

#7) https://www.codewars.com/kata/568d0dd208ee69389d000016
def rental_car_cost(d):
    if d == 1 or d == 2:
        return d * 40
    elif d >=3 and d <=6:
        return d * 40 - 20
    else:
        return d * 40 - 50
    

#8) https://www.codewars.com/kata/57a0885cbb9944e24c00008e
def remove_exclamation_marks(s):
    return s.replace('!', '')
