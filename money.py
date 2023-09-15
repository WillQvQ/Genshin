def no_money_more():
    a, b = (6 + 2*(30+98+198+328+648))*10/160, 6+30+98+198+328+648
    c, d = (6480+1600)/160, 648
    print(round(a), b)
    print(round(c)*2, d*2)

if __name__ == "__main__":
    no_money_more()