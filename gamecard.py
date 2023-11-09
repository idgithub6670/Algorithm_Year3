


f = open("C:\cards.txt", "r")
cards = f.read()
def drawcard():
    hand = []
    f = open("C:\cards.txt", "r")
    for line in f.readlines():
        hand.append([line])

    print(hand)


def playcard():
    
drawcard()
