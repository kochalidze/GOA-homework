#თითო სექციაზე გავაკეთოთ 5-5 მაგალითი
#(1 სექცია) Allow Duplicates
#1
cars = ["Mersedes", "Bmw", "porshe", "formula 1", "Alfa Romeo", "Subaru"]
print(cars)

#2
songs = ["გურული ბიჭები", "რა მოგელანდა", "აბიტურიენტს", " Gym songs"]
print(songs)

#3
Football_player = ["Kvaracxelia", "Messi", "Ronaldo", "Mbape", "Neimar jr", "Vinicius jr"]
print(Football_player)

#4
Old_football_player = ["Maradona", "Pele", "carlos", "Ronaldinio", "Ronaldo", "ROMÁRIO", "Xavi"]
print(Old_football_player)

#5
countries = ["Poland", "Norway", "Czechia", "Georgia"]
print(countries)



#(2 სექცია) List Length
cars = ["Mersedes", "Bmw", "porshe", "formula 1"]
print(len(cars))

#2
songs = ["გურული ბიჭები", "რა მოგელანდა", "აბიტურიენტს", " Gym songs"]
print(len[songs])

#3
Old_football_player = ["Maradona", "Pele", "carlos", "Ronaldinio", "Ronaldo", "ROMÁRIO", "Xavi"]
print(len[Old_football_player])

#4
countries = ["Poland", "Norway", "Czechia", "Georgia"]
print(len[countries])

#5
Football_player = ["Kvaracxelia", "Messi", "Ronaldo", "Mbape", "Neimar jr", "Vinicius jr"]
print(len[Football_player])



#(3 სექცია)  Combine the lists
#1
cars = ["Mersedes", "Bmw", "porshe", "formula 1"]
cars2 = ["Alfa Romeo", "Audi", "Rolls-Royce", "Subaru"]
cars3 = cars + cars2
print(cars3)

#2
Football_player = ["Kvaracxelia", "Messi", "Ronaldo", "Mbape", "Neimar jr", "Vinicius jr"]
Old_football_player = ["Maradona", "Pele", "carlos", "Ronaldinio", "Ronaldo", "ROMÁRIO", "Xavi"]
players = Football_player + Old_football_player
print(players)

#3
cars = ["Mersedes", "Bmw", "porshe", "formula 1"]
songs = ["გურული ბიჭები", "რა მოგელანდა", "აბიტურიენტს", " Gym songs"]
both_together = cars + songs
print(both_together)

#4
countries = ["Poland", "Norway", "Czechia", "Georgia"]
cities = ["ვარშავა", "პრაღა", "ბრატისლავა", "ათენი"]
both_together2 = countries + cities
print(both_together2)

#5
dance = ["Georgia dance", "Polandian dance", "Czechian dance"]
Anthem = ["Anthem of Georgia", "German national anthem", "Anthem of Poland"]
both_together3 = dance + Anthem
print(both_together3)



#(4 სექცია) List Items - Data Types
#1
cars2 = ["Alfa Romeo", "Audi", "Rolls-Royce", "Subaru"]
print(type(cars2))

#2
Football_player = ["Kvaracxelia", "Messi", "Ronaldo", "Mbape", "Neimar jr", "Vinicius jr"]
print(type(Football_player))

#3
countries = ["Poland", "Norway", "Czechia", "Georgia"]
print(type(countries))

#4
Old_football_player = ["Maradona", "Pele", "carlos", "Ronaldinio", "Ronaldo", "ROMÁRIO", "Xavi"]
print(type(Old_football_player))

#5
songs = ["გურული ბიჭები", "რა მოგელანდა", "აბიტურიენტს", " Gym songs"]
print(type(songs))
 


#(5 სექცია) Write the last data from the list
#1
cars = ["Mersedes", "Bmw", "porshe", "formula 1"]
print(cars[3])

#2
Football_player = ["Kvaracxelia", "Messi", "Ronaldo", "Mbape", "Neimar jr", "Vinicius jr"]
print(Football_player[5])

#3
Old_football_player = ["Maradona", "Pele", "carlos", "Ronaldinio", "Ronaldo", "ROMÁRIO", "Xavi"]
print(Old_football_player[6])

#4
songs = ["გურული ბიჭები", "რა მოგელანდა", "აბიტურიენტს", " Gym songs"]
print(songs[3])

5
countries = ["Poland", "Norway", "Czechia", "Georgia"]
print(countries[3])



# შექმენით სია, სადაც შეიტანთ თქვენი ოჯახის წევრების სახელებს.
names = ["Giga", "Nini", "Naira", "Zviadi"]

print(names[0])
print(names[1])
print(names[2])
print(names[3])



#ექმენით სია, სადაც გექნებათ 1-იდან 10-ის ჩათვლით რიცხვები.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers[0])
print(len(numbers) - 1)




#შექმენით სია, სადაც გექნებათ 10-იდან 20-ის ჩათვლით რიცხვები
nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

nums[0] = 1
nums[2] = 1
nums[4] = 1
nums[6] = 1
nums[8] = 1
nums[10] = 1

print(nums)



#მომხმარებელს შეეკითხეთ სახელი, გვარი, ასაკი, საცხოვრებელი ადგილი და მეილი.
name = input("please neter your name: ")
last_name = input("please enter your last name: ")
age = input("please enter your age: ")
adress = input("please enter your adress: ")
email = input("please enter your email: ")

name = []

for i in range(name, last_name, age, adress, email):
      name.append(i)

print(name)




#ცვლადში შეინახეთ თქვენი გვარი. გამოიყენეთ indexing და მისი თითოეული ასო დაბეჭდეთ.
me_last_name = "Kochalidze"

print(me_last_name[0])
print(me_last_name[1])
print(me_last_name[2])
print(me_last_name[3])
print(me_last_name[4])
print(me_last_name[5])
print(me_last_name[6])
print(me_last_name[7])
print(me_last_name[8])
print(me_last_name[9])