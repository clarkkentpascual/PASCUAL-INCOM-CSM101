
while True:
    word = input("ENTER A WORD: ")
    letter = input("ENTER A CHARACTER TO SEARCH FOR: ")

    found = False

    for character in word:
        if character.upper() == letter.upper():
            found = True
            break
    if found:
        print("CHARACTER FOUND CONGRATS!")
    else:
        print("CHARACTER NOT FOUND!!!")
    again = input("Try again? (YES/NO)")
    if again.upper() != "YES":
        print("THANKYOU FOR YOU PRECIOUS TIME!")
        break