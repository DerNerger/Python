from palindrom import isPalindrom

while True:
    try:
        n = raw_input("Eingabe= ")
    except KeyboardInterrupt:
        if raw_input("beenden? ")=="y" :
	    break
    except EOFError:
        if raw_input("beenden? ")=="y" :
            break

    print isPalindrom(n)
