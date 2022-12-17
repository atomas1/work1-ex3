def find_random():
    print("Pomyśl liczbę od 0 do 1000 a ja ją zgadnę w max. 10 próbach")
    max = 1000
    min = 0
    i = 0
    while True:
        try:
            guess = int((max - min) / 2) + min
            i += 1
            print(f"""Próba {i}:
                   Zgaduję: {guess}""")
            answer = input("""Wybierz odpowiedź:
                   1-za mało
                   2-za dużo
                   3-zgadłeś
                   """)
            answer = int(answer)
            if answer == 3:
                print("Wygrałem!")
                break
            elif answer == 2:
                max = guess
            elif answer != 2:
                if answer == 1:
                    min = guess
                else:
                    print("Nie oszukuj!")
        except:
            print('To nie jest poprawna odpowiedź')
            i-=1


if __name__ == '__main__':
    find_random()
