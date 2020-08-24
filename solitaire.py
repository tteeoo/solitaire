import readline
import random
import time
import os
import time

w = 0

# Card init
suits = ("s","h","c","d")
nums = ("a","2","3","4","5","6","7","8","9","t","j","q","k")
cards = []
for s in suits:
    for n in nums:
        cards.append(s + n)

# Initialize columns and foundations
cols = []
fcols = []
for i in range(7):
    cols.append([])
for i in range(4):
    fcols.append([])


# Populate
for c in range(len(cols)):
    for i in range(c + 1):
        card = random.choice(cards)
        if i == c: cols[c].append(card + "u")
        else: cols[c].append(card + "d")
        cards.remove(card)

# Shuffle
random.shuffle(cards)

# Render
def render():
    global cols, cards, fcols, w

    # Clear terminal
    os.system("clear")

    # Check win
    try:
        for i in range(len(fcols)):
            if fcols[i][-1][1] == "k":
                w += 1
    except IndexError: pass
    if w >= 4: win()

    # Flip over end cards
    for c in range(len(cols)):
        if cols[c] != []:
            if cols[c][-1][2] == "d":
                card = list(cols[c][-1])
                cols[c].remove(cols[c][-1])
                card[2] = "u"
                "".join(card)
                cols[c].append(card)

    # Initialize output columns
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
                    orows[i] += "[\033[41m\033[30m{}{}\033[0m]".format(cols[c][i][0], cols[c][i][1])
                if color(cols[c][i]) == "black":
                    orows[i] += "[\033[40m\033[39m{}{}\033[0m]".format(cols[c][i][0], cols[c][i][1])
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

    # Initialize output foundation columns
    ofcols = ""
    for c in range(len(fcols)):
        try:
            if color(fcols[c][-1]) == "red":
                ofcols += "[\033[41m\033[30m{}{}\033[0m]".format(fcols[c][-1][0], fcols[c][-1][1])
            if color(fcols[c][-1]) == "black":
                ofcols += "[\033[40m\033[39m{}{}\033[0m]".format(fcols[c][-1][0], fcols[c][-1][1])
        except IndexError:
            ofcols += "[  ]"
    
    # Initialize output deck
    if cards == []:
        ocards = "[  ]"
    elif color(cards[0]) == "red":
        ocards = "[\033[41m\033[30m{}{}\033[0m]".format(cards[0][0], cards[0][1])
    elif color(cards[0]) == "black":
        ocards = "[\033[40m\033[39m{}{}\033[0m]".format(cards[0][0], cards[0][1])
    else:
        pass

    # Print board
    print("-01--02--03--04--05--06--07-") 
    for i in range(len(orows)):
        print(orows[i].rjust(28), end="")
        if len(str(i+1)) == 1:
            print(" -0"+str(i+1)+"-")
        else:
            print(" -"+str(i+1)+"-")
    print(ofcols)
    print(ocards)
    print("")

# Prompt
def prompt():
    global cols, w
    command = input("solitaire> ")
    if command != "":
        command = command.split()
    if command == "":
        d()
    else:
        try:
            m(command)
        except:
            print("Invalid move arguments")
    prompt()

# Move
def m(command):
    global cols, acols, nums, suits
    if command[0] != "0" and command[0] != "a":
        scol = int(command[0]) - 1 
        srow = int(command[1]) - 1
        dcol = int(command[2]) - 1
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
    elif command[0] == "0":
        card = cards[0]
        dcol = int(command[1]) - 1
        if card[1] != "k":
            if color(card) == color(cols[dcol][-1]):
                print("Colors of stacked cards must alternate")
            elif nums[nums.index(card[1]) + 1] != nums[nums.index(cols[dcol][-1][1])]:
                print("Stacked cards must be in descending order")
            elif cols[dcol] == []:
                print("Only kings can be stacked on empty columns")
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
    elif command[0] == "a":
        if command[1] != "0":
            scol = int(command[1]) - 1
            card = cols[scol][-1]
            for i in range(len(suits)):
                if card[0] == suits[i]:
                    suit = i
            if card[1] != "a":
                if fcols[suit] == []:
                    print("Only aces can be stacked on empty foundations")
                elif nums[nums.index(card[1]) - 1] != nums[nums.index(fcols[suit][-1][1])]:
                    print("Cards stacked on the foundation must be in increasing order")
                else:
                    cols[scol].remove(card)
                    fcols[suit].append(card)
                    render()
            else:
                if fcols[suit] != []:
                    print("Aces can only be stacked on an empty foundation")
                else:
                    cols[scol].remove(card)
                    fcols[suit].append(card)
                    render()
        else:
            card = cards[0]
            for i in range(len(suits)):
                if card[0] == suits[i]:
                    suit = i
            if card[1] != "a":
                if fcols[suit] == []:
                    print("Only aces can be stacked on empty foundations")
                elif nums[nums.index(card[1]) - 1] != nums[nums.index(fcols[suit][-1][1])]:
                    print("Cards stacked on the foundation must be in increasing order")
                else:
                    cards.remove(card)
                    fcols[suit].append(card)
                    render()
            else:
                if fcols[suit] != []:
                    print("Aces can only be stacked on an empty foundation")
                else:
                    cards.remove(card)
                    fcols[suit].append(card)
                    render()
    else:
        print("Invalid parameters")

# Draw
def d():
    global cards
    try:
        card = cards[0] 
        cards.remove(card)
        cards.append(card)
    except:
        pass
    render()

# Color
def color(card):
    if card[0] == "s" or card[0] == "c":
        return "black"
    if card[0] == "h" or card[0] == "d":
        return "red"

# Win
def win():
    print("You win!")

render()
prompt()
