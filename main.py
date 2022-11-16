class Algorytm:
    slowo = input("podaj slowo\n")
    tab = ["b", "c", "d", "f", "g", "j", "k", "l", "m", "p", "r", "s", "t", "w", "z", "n"]
    spolgloski = ""
    slowo2 = ""
    for i in range (len(slowo)):
        for j in range (len(tab)):
            if slowo[i] == tab[j]:
                spolgloski += slowo[i]
    k = 0

    for i in slowo:
        if i in spolgloski:
            if k == len(spolgloski):
                slowo2 += spolgloski[0]
            else:
                slowo2 += spolgloski[k-1]
                k += 1
        else:
            slowo2 += i
    print(slowo2)

test = Algorytm()