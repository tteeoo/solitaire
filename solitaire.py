import random
import time
import os
import shutil
import time

w = 0

#Card init
suits = ["s","h","c","d"]
nums = ["a","2","3","4","5","6","7","8","9","t","j","q","k"]
cards = []
for s in suits:
    for n in nums:
        cards.append(s + n)

#(a)Col init
cols = []
acols = []
for i in ["col1","col2","col3","col4","col5","col6","col7","acols","acolh","acolc","acold"]:
    if i[0] == "a":
        i = []
        acols.append(i)
    else:
        i = []
        cols.append(i)

#Populate
for c in range(len(cols)):
    for i in range(c + 1):
        if i == c:
            card = random.choice(cards)
            cols[c].append(card + "u")
        else:
            card = random.choice(cards)
            cols[c].append(card + "d")
        cards.remove(card)

#Shuffle
random.shuffle(cards)

#Render
def render():
    os.system("clear")
    global cols, cards, acols, w
    #Check win
    try:
        for a in range(len(acols)):
            if acols[a][-1][1] == "k":
                w += 1
    except IndexError:
        pass
    if w >= 4:
        win()

    #Flip over
    for c in range(len(cols)):
        if cols[c] != []:
            if cols[c][-1][2] == "d":
                card = list(cols[c][-1])
                cols[c].remove(cols[c][-1])
                card[2] = "u"
                "".join(card)
                cols[c].append(card)

    #Output cols init
    olen = []
    for i in range(len(cols)):
        olen.append(len(cols[i]))
    for c in range(len(cols)):
        for i in range(max(olen)):
            if len(cols[c]) < max(olen):
                cols[c].append("eee")
    orows = []
    for i in range(max(olen)):
        i = ""
        orows.append(i)
    for c in range(len(cols)):
        for i in range(len(cols[c])):
            if cols[c][i][2] == "u":
                if color(cols[c][i]) == "red":
                    orows[i] += f"[\033[41m\033[30m{cols[c][i][0]}{cols[c][i][1]}\033[0m]"
                if color(cols[c][i]) == "black":
                    orows[i] += f"[\033[40m\033[39m{cols[c][i][0]}{cols[c][i][1]}\033[0m]"
            elif cols[c][i][2] == "d":
                orows[i] += "[--]"
            else:
                orows[i] += "    "
    for c in range(len(cols)):
        for i in range(len(cols[c])):
            try:
                cols[c].remove("eee")
            except ValueError:
                pass

    #Output acols init
    oacols = ""
    for c in range(len(acols)):
        try:
            if color(acols[c][-1]) == "red":
                oacols += f"[\033[41m\033[30m{acols[c][-1][0]}{acols[c][-1][1]}\033[0m]"
            if color(acols[c][-1]) == "black":
                oacols += f"[\033[40m\033[39m{acols[c][-1][0]}{acols[c][-1][1]}\033[0m]"
        except IndexError:
            oacols += "[  ]"
    
    #Output cards init
    if cards == []:
        ocards = "[  ]"
    elif color(cards[0]) == "red":
        ocards = f"[\033[41m\033[30m{cards[0][0]}{cards[0][1]}\033[0m]"
    elif color(cards[0]) == "black":
        ocards = f"[\033[40m\033[39m{cards[0][0]}{cards[0][1]}\033[0m]"
    else:
        pass

    #Print
    for i in orows:
        print(i.rjust(28))
    print(f"\n{oacols}")
    print(f"{ocards}\n")

#Prompt
def prompt():
    global cols, w
    command = input("solitaire> ")
    command += " "
    if command[0] == "m":
        try:
            m(command)
        except:
            print("Invalid move parameters")
    elif command == " ":
        d()
    elif command == "r ":
        render()
    else:
        print("Invalid command")
    prompt()

#Move
def m(command):
    global cols, acols, nums, suits
    if command[1] != "0" and command[1] != "a":
        scol = int(command[1]) - 1 
        srow = int(command[2]) - 1
        dcol = int(command[3]) - 1
        card = cols[scol][srow]
        if card[1] != "k":
            if card[2] == "d":
                print("You cannot moved face-down cards")
            elif color(card) == color(cols[dcol][-1]):
                print("Colors of stacked cards must alternate")
            elif nums[nums.index(card[1]) + 1] != nums[nums.index(cols[dcol][-1][1])]:
                print("Stacked cards must be in descending order")
            else:
                r = len(cols[scol]) - srow
                for i in range(r):
                    card = cols[scol][srow]
                    cols[scol].remove(card)
                    cols[dcol].append(card)
                render()
        else:
            if card[2] == "d":
                print("You cannot moved face-down cards")
            elif cols[dcol] != []:
                print("Kings can only be stacked on an empty column")
            else:
                r = len(cols[scol]) - srow
                for i in range(r):
                    card = cols[scol][srow]
                    cols[scol].remove(card)
                    cols[dcol].append(card)
                render()
    elif command[1] == "0":
        card = cards[0]
        dcol = int(command[2]) - 1
        if card[1] != "k":
            if color(card) == color(cols[dcol][-1]):
                print("Colors of stacked cards must alternate")
            elif nums[nums.index(card[1]) + 1] != nums[nums.index(cols[dcol][-1][1])]:
                print("Stacked cards must be in descending order")
            else:
                cards.remove(card)
                cols[dcol].append(card + "u")
                render()
        else:
            if cols[dcol] != []:
                print("Kings can only be stacked on an empty column")
            else:
                cards.remove(card)
                cols[dcol].append(card + "u")
                render()
    elif command[1] == "a":
        if command[2] != "0":
            scol = int(command[2]) - 1
            card = cols[scol][-1]
            for i in range(len(suits)):
                if card[0] == suits[i]:
                    suit = i
            if card[1] != "a":
                if acols[suit] == []:
                    print("Only aces can be stacked on empty ace piles")
                elif nums[nums.index(card[1]) - 1] != nums[nums.index(acols[suit][-1][1])]:
                    print("Stacked cards in the ace pile must be in increasing order")
                else:
                    cols[scol].remove(card)
                    acols[suit].append(card)
                    render()
            else:
                if acols[suit] != []:
                    print("Aces can only be stacked on an empty ace pile")
                else:
                    cols[scol].remove(card)
                    acols[suit].append(card)
                    render()
        else:
            card = cards[0]
            for i in range(len(suits)):
                if card[0] == suits[i]:
                    suit = i
            if card[1] != "a":
                if acols[suit] == []:
                    print("Only aces can be stacked on empty ace piles")
                elif nums[nums.index(card[1]) - 1] != nums[nums.index(acols[suit][-1][1])]:
                    print("Stacked cards in the ace pile must be in increasing order")
                else:
                    cards.remove(card)
                    acols[suit].append(card)
                    render()
            else:
                if acols[suit] != []:
                    print("Aces can only be stacked on an empty ace pile")
                else:
                    cards.remove(card)
                    acols[suit].append(card)
                    render()
    else:
        print("Invalid parameters")

#Draw
def d():
    global cards
    card = cards[0]
    cards.remove(card)
    cards.append(card)
    render()

#Color
def color(card):
    if card[0] == "s" or card[0] == "c":
        return "black"
    if card[0] == "h" or card[0] == "d":
        return "red"

#Win
def win():
    c = 0
    while 1:
        size = shutil.get_terminal_size((80, 20))
        if c % 2 == 0:
            c += 1
            print("\033[40m\033[31m You Win \033[0m" * size[0])
        else:
            c += 1
            print("\033[41m\033[30m You Win \033[0m" * size[0])
        time.sleep(0.5)

render()
prompt()
