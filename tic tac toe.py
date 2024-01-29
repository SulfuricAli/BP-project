from LCG_random import *

n = int(input("choose your option: \n1.PvP , player vs player \n2.PvE , player vs computer\nchoice:"))

board = "|1|2|3|\n|4|5|6|\n|7|8|9|"
print(board)

winning_scenarios = [["1","4","7"],["1","2","3"],["1","5","9"],["2","5","8"],["4","5","6"],["3","5","7"],["3","6","9"],["7","8","9"]]

is_tie = True
p1 = []

def contains(small, big):
    is_contain = True
    for item in small:
        if item not in big:
            is_contain = False
            break
    return is_contain

if n == 1:

    p2 = []

    i = 0
    while (i < 9) and (is_tie):
        player1_choice = input("player one: ")
        board = board.replace(player1_choice , "x")
        print(board)
        p1.append(player1_choice)



        for sequence in winning_scenarios:
            cnt = 0
            for squeare in sequence:
                if squeare in p1:
                    cnt += 1
            if cnt == 3:
                print("player one won !")
                is_tie = False
                break

        if i == 8:
            break
        if is_tie:
            player2_choice = input("player two: ")
            board = board.replace(player2_choice, "O")
            print(board)
            p2.append(player2_choice)


            for sequence in winning_scenarios:
                cnt = 0
                for squeare in sequence:
                    if squeare in p2:
                        cnt += 1
                if cnt == 3:
                    print("player two won !")
                    is_tie = False
                    break
        i += 2

else:
    computer_choises = []
    i = 0
    while (i < 9) and (is_tie):

        player1_choice = input("player one: ")
        board = board.replace(player1_choice, "x")
        print(board)
        p1.append(player1_choice)


        for sequence in winning_scenarios:
            cnt = 0
            for squeare in sequence:
                if squeare in p1:
                    cnt += 1
            if cnt == 3:
                print("player one won !")
                is_tie = False
                break

        if i == 8:
            break

        cond_list = []
        cond_list.extend(p1)
        cond_list.extend(computer_choises)

        if is_tie:
            s = LCG()
            computer = str(s.int_generator([1,10]))

            while computer in cond_list:
                computer = str(s.int_generator([1,10]))

            board = board.replace(computer, "O")
            print(f"computer choosed {computer}")
            print(board)
            computer_choises.append(computer)


            for sequence in winning_scenarios:
                cnt = 0
                for squeare in sequence:
                    if squeare in computer_choises:
                        cnt += 1
                if cnt == 3:
                    print("computer won !")
                    is_tie = False
                    break
        i += 2

if is_tie:
    print("GG , it's a tie!")