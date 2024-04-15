import time
import mysql.connector
import random
from datetime import date
connection = mysql.connector.connect(user = 'root', database = 'bankingappdata', password = 'SurgeIsCool!2020')
currentuser = ""
currentpass = ""
currentfirst = ""
currentlast = ""
dateofbirth = 1112012
currentbalance = 0
greetings = ["Hello", "Hola", "Guten Tag", "Bonjour", "Ni Hao", "Salaam", "Konnichiwa", "Ciao"]

def display_menu():
    print("1. Create Account")
    print("2. Log In")
    option = input("Select an option by typing in a number... ")
    if option == "1":
        print("-------------------------------------------------------------")
        print("CREATE AN ACCOUNT")
        time.sleep(3)
        userchoice = input("Type in your username here... ")
        userpass = input("Type in your password here... ")
        cursor = connection.cursor()
        cursor.execute("SELECT Username, COUNT(*) FROM details WHERE Username = %s GROUP BY Username",(userchoice,))
        cursor.fetchall()
        row_count = cursor.rowcount
        if row_count == 0:
            credit1 = str(random.randint(100, 999))
            credit2 = str(random.randint(100, 999))
            credit3 = str(random.randint(100, 999))
            randomcredit = f"{credit1}-{credit2}-{credit3}"
            cursor.execute("INSERT INTO details (Username, Passkey, CreditCard) VALUES (%s, %s, %s)", (userchoice, userpass, randomcredit))
            connection.commit()
            cursor.close()
            print("Congrats! Your account has been created! Log in and go to the settings to add more.")
            time.sleep(3)
            display_menu()
        else:
            print("This account already exists! Try again.")
            time.sleep(2)
            cursor.close()
            display_menu()
    elif option == '2':
        print("-------------------------------------------------------------")
        print("LOG IN")
        time.sleep(3)
        userchoice2 = input("Type in your username here... ")
        userpass2 = input("Type in your password here... ")
        cursor = connection.cursor()
        cursor.execute("SELECT Username FROM details WHERE Username = %s AND Passkey = %s LIMIT 0, 1",(userchoice2, userpass2))
        cursor.fetchall()
        row_count2 = cursor.rowcount
        if row_count2 == 1:
            global currentuser
            global currentpass
            currentpass = userpass2
            currentuser = userchoice2
            greeting = random.choice(greetings)
            print(f"Successfully logged in! {greeting}, {currentuser}!")
            time.sleep(2)
            today = date.today()
            currentday = today.strftime("%B %d, %Y")
            print("-------------------------------------------------------------")
            print(f"Today is {currentday}...")
            print("-------------------------------------------------------------")
            time.sleep(1)
            display_mainmenu()
            cursor.close()
        else:
            print("We could not find that account! Make sure everything is typed correctly.")
            time.sleep(1)
            display_menu()
            cursor.close()
    else:
        print("Your choice didn't go through. Please make sure you typed correctly.")
        time.sleep(1)
        display_menu()
        
def display_mainmenu():
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Send")
    print("4. Account")
    print("5. Balance")
    print("6. Exit Banking App")
    option = input("Select an option by typing in a number... ")
    if option == "4":
        print("-------------------------------------------------------------")
        print("ACCOUNT")
        time.sleep(3)
        global currentuser
        global currentpass
        print(f"Username: {currentuser}")
        cursor = connection.cursor()
        cursor.execute("SELECT FirstName FROM details WHERE Username = %s", (currentuser,))
        findfirst = cursor.fetchall()
        for x in findfirst:
            currentfirst = x[0]
        print(f"First Name: {currentfirst}")
        cursor.execute("SELECT LastName FROM details WHERE Username = %s", (currentuser,))
        findlast = cursor.fetchall()
        for x in findlast:
            currentlast = x[0]
        print(f"Last Name: {currentlast}")
        cursor.execute("SELECT DateOfBirth FROM details WHERE Username = %s", (currentuser,))
        findbirth = cursor.fetchall()
        for x in findbirth:
            dateofbirth = x[0]
        print(f"Birthday: {dateofbirth}")
        time.sleep(1)
        print("1. Edit Account")
        print("2. See Credit Card Information")
        print("3. Delete Account")
        print("4. Exit")
        option2 = input("Select an option by typing in a number... ")
        if option2 == "1":
            print("1. Username")
            print("2. Password")
            print("3. First Name")
            print("4. Last Name")
            print("5. Birthday")
            eoption = input("Select an option by typing in a number... ")
            if eoption == "1":
                newuser = input("Enter a new username here... ")
                cursor.execute("SELECT Username, COUNT(*) FROM details WHERE Username = %s GROUP BY Username",(newuser,))
                cursor.fetchall()
                row_count = cursor.rowcount
                if row_count == 0:
                    cursor.execute("UPDATE details SET Username = %s WHERE Username = %s", (newuser, currentuser))
                    connection.commit()
                    currentuser = newuser
                    print("Username updated! Make sure to memorize it!")
                    time.sleep(2)
                    print("-------------------------------------------------------------")
                    display_mainmenu()
                else:
                    print("This username is already taken! Please choose a different one.")
                    time.sleep(2)
                    print("-------------------------------------------------------------")
                    display_mainmenu()
            elif eoption == "2":
                newpass = input("Enter a new password here... ")
                cursor.execute("UPDATE details SET Passkey = %s WHERE Passkey = %s AND Username = %s", (newpass, currentpass, currentuser))
                connection.commit()
                currentpass = newpass
                print("Password updated! Make sure to memorize it!")
                time.sleep(2)
                print("-------------------------------------------------------------")
                display_mainmenu()
            elif eoption == "3":
                currentfirst = input("Enter your current first name here... ")
                newfirst = input("Enter a new first name here... ")
                cursor.execute("UPDATE details SET FirstName = %s WHERE FirstName = %s AND Username = %s", (newfirst, currentfirst, currentuser))
                connection.commit()
                currentfirst = newfirst
                print("First name updated!")
                time.sleep(2)
                print("-------------------------------------------------------------")
                display_mainmenu()
            elif eoption == "4":
                currentlast = input("Enter your current last name here... ")
                newlast = input("Enter a new last name here... ")
                cursor.execute("UPDATE details SET LastName = %s WHERE LastName = %s AND Username = %s", (newlast, currentlast, currentuser))
                connection.commit()
                currentlast = newlast
                print("Last name updated!")
                time.sleep(2)
                print("-------------------------------------------------------------")
                display_mainmenu()
            elif eoption == "5":
                dateofbirth = input("Enter your current date of birth(in this format: X-XX-XXXX)... ")
                newdob1 = input("Enter a new month here... ")
                newdob2 = input("Enter a new day here... ")
                newdob3 = input("Enter a new year here... ")
                newdob = f"{newdob1}-{newdob2}-{newdob3}"
                cursor.execute("UPDATE details SET DateOfBirth = %s WHERE DateOfBirth = %s AND Username = %s", (newdob, dateofbirth, currentuser))
                connection.commit()
                dateofbirth = newdob
                print("Date of birth updated!")
                time.sleep(2)
                print("-------------------------------------------------------------")
                display_mainmenu()
            else:
                print("Your choice didn't go through. Please make sure you typed correctly.")
                time.sleep(1)
                display_mainmenu()
        elif option2 == "2":
            cursor.execute("SELECT CreditCard FROM details WHERE Username = %s", (currentuser,))
            result1 = cursor.fetchall()
            for x in result1:
                currentcredit = x[0]
            print("-------------------------------------------------------------")
            print(f"Your credit card number is {currentcredit}. Don't forget it!")
            time.sleep(2)
            print("-------------------------------------------------------------")
            display_mainmenu()
        elif option2 == "3":
            print("-------------------------------------------------------------")
            firstchance = input("Are you sure you want to delete your account? Y/N ")
            if firstchance == "Y":
                secondchance = input("Are you REALLY SURE you want to delete your account? Y/N ")
                if secondchance == "Y":
                    lastchance = input("Once this is done, you will NOT be able to get your account back. Last chance! Y/N ")
                    if lastchance == "Y":
                        cursor.execute("DELETE FROM details WHERE Username = %s", (currentuser,))
                        connection.commit()
                        print("Your account is now deleted.")
                        time.sleep(2)
                        print("-------------------------------------------------------------")
                        display_menu()
                    else:
                        print("-------------------------------------------------------------")
                        display_mainmenu()
                else:
                    print("-------------------------------------------------------------")
                    display_mainmenu()
            else:
                print("-------------------------------------------------------------")
                display_mainmenu()
        elif option2 == "4":
            print("-------------------------------------------------------------")
            display_mainmenu()
        else:
            print("Your choice didn't go through. Please make sure you typed correctly.")
            time.sleep(1)
            display_mainmenu()
    elif option == "5":
        print("-------------------------------------------------------------")
        cursor = connection.cursor()
        cursor.execute("SELECT Balance FROM details WHERE Username = %s", (currentuser,))
        balancefind = cursor.fetchall()
        for x in balancefind:
            currentbalance = x[0]
        print(f"Your current balance is ${currentbalance}.")
        time.sleep(2)
        print("-------------------------------------------------------------")
        display_mainmenu()
    elif option == "6":
        print("See you later!")
        time.sleep(2)
    elif option == "3":
        cursor = connection.cursor()
        cursor.execute("SELECT Balance FROM details WHERE Username = %s", (currentuser,))
        balancefind = cursor.fetchall()
        for x in balancefind:
            currentbalance = x[0]
        print("-------------------------------------------------------------")
        print("SEND")
        time.sleep(3)
        receiver = input("Type the username of the person receiving the money... ")
        try:
            amounttosend = int(input("Type the amount of money to send... "))
        except ValueError:
            print("That is not a number. Try again.")
            time.sleep(2)
            display_mainmenu()
        else:
            confirm = input(f"{receiver} is going to receive ${amounttosend}. Is this okay? Y/N ")
            if confirm == "Y":
                cursor = connection.cursor()
                cursor.execute("SELECT Username, COUNT(*) FROM details WHERE Username = %s AND Username != %s GROUP BY Username", (receiver, currentuser,))
                cursor.fetchall()
                row = cursor.rowcount
                if row != 0:
                    cursor.execute("SELECT Balance FROM details WHERE Username = %s", (receiver,))
                    receiverbalfind = cursor.fetchall()
                    for x in receiverbalfind:
                        receiverbal = x[0]
                    originalbalance = currentbalance
                    currentbalance = currentbalance - amounttosend
                    if currentbalance > 0:
                        receiverbal = receiverbal + amounttosend
                        cursor.execute("UPDATE details SET Balance = %s WHERE Username = %s", (receiverbal, receiver,))
                        cursor.execute("UPDATE details SET Balance = %s WHERE Username = %s", (currentbalance, currentuser,))
                        cursor.execute("SELECT FirstName FROM details WHERE Username = %s", (currentuser,))
                        findfirst = cursor.fetchall()
                        for x in findfirst:
                            currentfirst = x[0]
                        cursor.execute("SELECT LastName FROM details WHERE Username = %s", (currentuser,))
                        findlast = cursor.fetchall()
                        for x in findlast:
                            currentlast = x[0]
                        cursor.execute("INSERT INTO transactions (FirstName, LastName, Transaction, Amount, Receipent) VALUES (%s, %s, %s, %s, %s)", (currentfirst, currentlast, "Sending", amounttosend, receiver))
                        connection.commit()
                        print("Your money has been sent to your person of choice! Make sure to tell them!")
                        time.sleep(2)
                        print("-------------------------------------------------------------")
                        display_mainmenu()
                    else:
                        currentbalance = originalbalance
                        print("You don't have the money to send.")
                        time.sleep(2)
                        print("-------------------------------------------------------------")
                        display_mainmenu()
                else:
                    print("We couldn't find that user! Make sure you typed their name correctly.")
                    time.sleep(2)
                    print("-------------------------------------------------------------")
                    display_mainmenu()
            else:
                print("-------------------------------------------------------------")
                display_mainmenu()
    elif option == "1":
        cursor = connection.cursor()
        print("-------------------------------------------------------------")
        print("WITHDRAW")
        time.sleep(3)
        try:
            credit1 = int(input("Enter in the first three digits of your credit card... "))
        except ValueError:
            print("That isn't valid! Try again.")
            time.sleep(2)
            time.sleep(2)
            print("-------------------------------------------------------------")
            display_mainmenu()
        try:
            credit2 = int(input("Enter in the middle three digits of your credit card... "))
        except ValueError:
            print("That isn't valid! Try again.")
            time.sleep(2)
            time.sleep(2)
            print("-------------------------------------------------------------")
            display_mainmenu()
        try:
            credit3 = int(input("Enter in the last three digits of your credit card... "))
        except ValueError:
            print("That isn't valid! Try again.")
            time.sleep(2)
            print("-------------------------------------------------------------")
            display_mainmenu()
        creditcard = f"{credit1}-{credit2}-{credit3}"
        cursor.execute("SELECT CreditCard FROM details WHERE CreditCard = %s AND Username = %s", (creditcard, currentuser,))
        cursor.fetchall()
        roww = cursor.rowcount
        if roww == 1:
            try:
                amounttotake = int(input("How much money would you like to take out? "))
            except ValueError:
                print("That isn't valid! Try again.")
                time.sleep(2)
                print("-------------------------------------------------------------")
                display_mainmenu()
            confirmtakeout = input(f"You will take out ${amounttotake}. Is this okay? Y/N ")
            if confirmtakeout == "Y":
                cursor.execute("SELECT Balance FROM details WHERE Username = %s", (currentuser,))
                balancefind = cursor.fetchall()
                for x in balancefind:
                    currentbalance = x[0]
                originalbalance = currentbalance
                currentbalance = currentbalance - amounttotake
                if currentbalance > 0:
                    cursor.execute("UPDATE details SET Balance = %s WHERE Username = %s", (currentbalance, currentuser,))
                    cursor.execute("SELECT FirstName FROM details WHERE Username = %s", (currentuser,))
                    findfirst = cursor.fetchall()
                    for x in findfirst:
                        currentfirst = x[0]
                    cursor.execute("SELECT LastName FROM details WHERE Username = %s", (currentuser,))
                    findlast = cursor.fetchall()
                    for x in findlast:
                        currentlast = x[0]
                    cursor.execute("INSERT INTO transactions (FirstName, LastName, Transaction, Amount, Receipent) VALUES (%s, %s, %s, %s, %s)", (currentfirst, currentlast, "Withdrawal", amounttotake, currentuser))
                    connection.commit()
                    print(f"You took out ${amounttotake} from your account!")
                    time.sleep(2)
                    print("-------------------------------------------------------------")
                    display_mainmenu()
                else:
                    print("You don't have that money in your account.")
                    time.sleep(2)
                    print("-------------------------------------------------------------")
                    display_mainmenu()
            else:
                print("-------------------------------------------------------------")
                display_mainmenu()
        else:
            print("We couldn't find that credit card! Make sure you typed the numbers correctly.")
            time.sleep(2)
            print("-------------------------------------------------------------")
            display_mainmenu()
    elif option == "2":
        cursor = connection.cursor()
        print("-------------------------------------------------------------")
        print("DEPOSIT")
        time.sleep(3)
        try:
            credit1 = int(input("Enter in the first three digits of your credit card... "))
        except ValueError:
            print("That isn't valid! Try again.")
            time.sleep(2)
            time.sleep(2)
            print("-------------------------------------------------------------")
            display_mainmenu()
        try:
            credit2 = int(input("Enter in the middle three digits of your credit card... "))
        except ValueError:
            print("That isn't valid! Try again.")
            time.sleep(2)
            time.sleep(2)
            print("-------------------------------------------------------------")
            display_mainmenu()
        try:
            credit3 = int(input("Enter in the last three digits of your credit card... "))
        except ValueError:
            print("That isn't valid! Try again.")
            time.sleep(2)
            print("-------------------------------------------------------------")
            display_mainmenu()
        creditcard = f"{credit1}-{credit2}-{credit3}"
        cursor.execute("SELECT CreditCard FROM details WHERE CreditCard = %s AND Username = %s", (creditcard, currentuser,))
        cursor.fetchall()
        roww = cursor.rowcount
        if roww == 1:
            try:
                amounttoadd = int(input("How much money would you like to add(limit of $1000 per deposit)? "))
            except ValueError:
                print("That isn't valid! Try again.")
                time.sleep(2)
                print("-------------------------------------------------------------")
                display_mainmenu()
            if amounttoadd > 0 and amounttoadd < 1000:
                confirmadding = input(f"You will add ${amounttoadd} to your account. Is this okay? Y/N ")
                if confirmadding == "Y":
                    cursor.execute("SELECT Balance FROM details WHERE Username = %s", (currentuser,))
                    balancefind = cursor.fetchall()
                    for x in balancefind:
                        currentbalance = x[0]
                    originalbalance = currentbalance
                    currentbalance = currentbalance + amounttoadd
                    if currentbalance > 0:
                        cursor.execute("UPDATE details SET Balance = %s WHERE Username = %s", (currentbalance, currentuser,))
                        cursor.execute("SELECT FirstName FROM details WHERE Username = %s", (currentuser,))
                        findfirst = cursor.fetchall()
                        for x in findfirst:
                            currentfirst = x[0]
                        cursor.execute("SELECT LastName FROM details WHERE Username = %s", (currentuser,))
                        findlast = cursor.fetchall()
                        for x in findlast:
                            currentlast = x[0]
                        cursor.execute("INSERT INTO transactions (FirstName, LastName, Transaction, Amount, Receipent) VALUES (%s, %s, %s, %s, %s)", (currentfirst, currentlast, "Deposit", amounttoadd, currentuser))
                        connection.commit()
                        print(f"You added ${amounttoadd} to your account!")
                        time.sleep(2)
                        print("-------------------------------------------------------------")
                        display_mainmenu()
                    else:
                        print("You don't have that money in your account.")
                        time.sleep(2)
                        print("-------------------------------------------------------------")
                        display_mainmenu()
                else:
                    print("-------------------------------------------------------------")
                    display_mainmenu()
            else:
                print("Too much money! Try adding less(or more).")
                time.sleep(2)
                print("-------------------------------------------------------------")
                display_mainmenu()
        else:
            print("We couldn't find that credit card! Make sure you typed the numbers correctly.")
            time.sleep(2)
            print("-------------------------------------------------------------")
            display_mainmenu()


            


print(r""" ______ _______ _______ __  __ _______ _______ _______ 
|   __ \   _   |    |  |  |/  |_     _|    |  |     __|
|   __ <       |       |     < _|   |_|       |    |  |
|______/___|___|__|____|__|\__|_______|__|____|_______|
                                                       
 _______ ______ ______                                 
|   _   |   __ \   __ \                                
|       |    __/    __/                                
|___|___|___|  |___|                                   
                                                       """)
time.sleep(2)
print("Developed by Korrigan Jones")
time.sleep(2)
print("-------------------------------------------------------------")
print("Welcome to Banking App!")
time.sleep(1)
display_menu()