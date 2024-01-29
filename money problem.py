from LCG_random import *

players_money = []
kicked_players = []

i =0 # creating a list of all player whivh each has 25 dollars
while i <20:
    players_money.append(25)
    i+=1

num = LCG()

i = 0
while i < 5000:

    k = 0
    while k < len(players_money):
        if players_money[k]==0:#removing players with no money left
            kicked_players.append(k+1)
            players_money.pop(k)
        k += 1

    players_money[i%len(players_money)] -=1
    players_money[num.int_generator([0,len(players_money)])] += 1#randomly chossing a player to give them 1$
    i += 1

    print(players_money)

print(len(players_money))