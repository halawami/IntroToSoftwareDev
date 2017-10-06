def main():
    Fin = 7.37
    toFind = 60
    counter = 0  # pllpre
    counter2 = 0  # plldiv
    counter3 = 0  # pllpost
    print(counter)
    while((Fin / (counter + 2)) <= 8 and (Fin / (counter + 2)) >= 0.8):
        while(((Fin * (counter2 + 2)) / (counter + 2)) <= 340 and ((Fin * (counter2 + 2)) / (counter + 2)) >= 120):
            while(True):
                Fosc = ((Fin * (counter2 + 2)) / ((counter + 2) * 2 * (counter3 + 2)))
                if(Fosc == toFind):
                    print(counter)
                    print(counter2)
                    print(counter3)
                    break;
                counter3 += 1
            counter2 += 1
        counter += 1
