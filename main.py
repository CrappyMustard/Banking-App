import time
import mysql.connector
connection = mysql.connector.connect(user = 'root', database = 'bankingappdata', password = 'SurgeIsCool!2020')

def display_menu():
    print("Welcome to Banking App!")
    time.sleep(1)
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
        results = cursor.fetchall()
        row_count = cursor.rowcount
        if row_count == 0:
            cursor.execute("INSERT INTO details (Username, Passkey) VALUES (%s, %s)", (userchoice, userpass))
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
    if option == '2':
        print("-------------------------------------------------------------")
        print("LOG IN")
        time.sleep(3)
        userchoice2 = input("Type in your username here... ")
        userpass2 = input("Type in your password here...")

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
display_menu()