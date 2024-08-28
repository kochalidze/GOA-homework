#5-5 მაგალითი ოპერატორებიდან (>, <, ==, >=, <=, !=)


#პირველი ოპერაცია (>)
#true
print(9 > 8)
print(5 > 3)
print(11 > 10)
#false
print(44 > 55)
print(18 > 35)

#მეორე ოპერსცის (<)
#true
print(11 < 15)
print(7 < 8)
print(43 < 49)
#false
print(88 < 79)
print(12 < 11)

#მესამე ოპერსცის (==)
#true
print(13 == 13)
print(2 == 2)
print(41 == 41)
#false
print(77 == 79)
print(5 == 6)

#მეოთხე ოპერსცის (>=)
#true
print(50 >= 46)
print(33 >= 33)
print(40 >= 35)
#false
print(20 >= 30)
print(22 >= 90)


#მეხუთე ოპერსცის (<=)
#true
print(88 <= 100)
print(44 <= 44)
print(40 <= 35)
#false
print(66 <= 54)
print(64 <= 38)


#მეექვსე ოპერსცის (!=)
#true
print(90 != 10)
print(86 != 43)
print(57 != 35)
#false
print(55 != 55)
print(22 != 22)



#10-10 მაგალითი and და or ოპერატორებზე

#პირველი ოპერაცია (and)
print(7>4 and 1>0)
#true and true = true
print(4<5 and 0<2)
#true and true = true
print(4<3 and 9<8)
#false and false = false
print(6>7 and 8==7)
#false and false = false
print(7<8 and 6!=6)
#false and false = false
print(4==4 and 5!=5)
#true and false = false
print(6>3 and 6<4)
#true and false = false
print(5<3 and 5>4)
#false and true = false
print(5<=4 and 6<=6)
#false and true = false
print(4<=3 and 2>=1)
#false and true = false


#მეორე ოპერაცია (or)
print(8>7 or 1>0)
##true or true = true
print(9==9 or 8!=6)
#true or true = true
print(6<5 or 5==6)
#false or false = false
print(4<=3 or 8!=8)
#false or false = false
print(6>7 or 6!=6)
#false or false = false
print(5!=4 or 3==2)
#true or false = true
print(4>=3 or 6<=4)
#true or false = true
print(5<3 or 9<10)
#false or true = true
print(4!=4 or 9<=10)
#false or true = true
print(0>=1 or 9<15)
#false or true = true