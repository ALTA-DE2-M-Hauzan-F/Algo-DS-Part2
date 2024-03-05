def playing_domino(cards, deck):
    domino=[]
    sum_card=0
    for i in cards:
        if sum(i)>sum_card:
            if deck[1] ==i[0]:
                sum_card = sum(i)
                [domino.append(p) for p in i]
    return domino

if __name__ == "__main__":
    print(playing_domino([[6, 5], [3, 4], [2, 1], [3, 3]], [4, 3]))  # [3, 4]
    print(playing_domino([[6, 5], [3, 3], [3, 4], [2, 1]], [3, 6]))  # [6, 5]
    print(playing_domino([[6, 6], [2, 4], [3, 6]], [5, 1]))         # []