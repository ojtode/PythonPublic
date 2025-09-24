TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]
#we can use dictionary key_name : value
users = {"bob" : "123","ann" : "pass123","mike" : "password123","liz" : "pass123"}

username = input(str("username: "))
password = input(str("password: "))
print("----------------------------------------")

if username in users and users[username] == password:
    print("Welcome to the app,",username)
    print("We have", len(TEXTS) ,"to be analyzed.")
    print("----------------------------------------")


    text_number = input("Enter a number btw. 1 and 3 to select: ")
#   text = TEXTS[int(text_number) - 1]
    if text_number.isdigit() and int(text_number) >= 1 and int(text_number) < len(TEXTS):
        print("----------------------------------------")
        #do promenne vlozim text ze slovniku z pozice indexu -1 bere se od 0
        text = TEXTS[int(text_number) - 1]
        print("There are ",len(text.split()) ,"words in the selected text.")

        number_title = text.split()
        titlecase = sum(1 for word_title in number_title if word_title.istitle())
        print("There are ",titlecase ,"titlecase words.")

        uppercase = sum(1 for word_upper in number_title if word_upper.isupper())
        print("There are ",uppercase ,"uppercase words.")

        lowercase = sum(1 for word_lower in number_title if word_lower.islower())
        print("There are ",lowercase ,"lowercase words.")

        is_numeric = sum(1 for numeric in number_title if numeric.isnumeric())
        print("There are ",is_numeric," numeric strings.")

        total_number = [int(word_number) for word_number in number_title if word_number.isdigit()]
        number_sum = sum(total_number)
        print("The sum of all the numbers ",number_sum)
        print("----------------------------------------")
        #sloupcovy graf
        #rozdelim na slova
        graf_words = text.split()
        #prazdny slovnik klic (delka slova) hodnota (pocet slov s tou delkou)
        frequency={}
        #Vypocet cyklus for pokud v seznamu neni zapis ho jinak pridej jednicku
        for word in graf_words:
            length = len(word.strip(".,!?")) #odstrani interpukci
            if length in frequency:
                frequency[length] +=1
            else:
                frequency[length] =1

        #print("-" * 40)
        print(f"{'LEN':>3}|{'OCCURRENCES':^15}|{'NR.':>3}")
        print("-" * 40)
        for length in sorted(frequency):
            count = frequency[length]
            print(f"{length:3}|{'*' * count:<15}|{count}")

       # print(text)
    else:
        print("Enter the correct choice")


  #  print(username, "and", password)
else:
    print("Unregistered user, terminating the program..")
