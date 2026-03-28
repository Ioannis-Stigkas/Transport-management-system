transfers = []     # Δημιουργία λίστας για τις μεταφορές

def add_transfers():
    num = int(input("Πόσες μεταφορές θέλετε να προσθέσετε σήμερα; "))
    transfers.append(num)
    print("Καταχωρήθηκαν οι μεταφορές!")

def average():
    if len(transfers) == 0:
        print("Δεν υπάρχουν μεταφορές για να υπολογιστεί ο μέσος όρος. Παρακαλώ προσθέστε μεταφορές πρώτα.")
    else:
        avg = sum(transfers) / len(transfers)
        print("Ο μέσος ορος των μεταφορών είναι :", avg)

def show_transfers():
    if len(transfers) == 0:
        print("Δεν υπάρχουν μεταφορές για να εμφανιστούν.")
    else:
        print("\ν---Αναλυτική εμφάνιση μεταφορών---")
        for i in range(len(transfers)):
            print("Μέρα", i+1, ":", transfers[i], "μεταφορές")

def reset_transfers():
    transfers.clear()
    print("Οι μεταφορές έχουν μηδενιστεί.")

while True:
    print("\n--- Σύστημα Διαχείρισης Μεταφορών ---")
    print("1. Προσθήκη Μεταφορών")
    print("2. Υπολογισμός Μέσου Όρου")
    print("3.Αναλυτική Προβολή Καταχώρησης Μεταφορών")
    print("4.Μηδενισμός Μεταφορών")
    print("5.Έξοδος απο το σύστημα")
    choice = input("Επιλέξτε μια επιλογή: ")

    if choice == "1":
        add_transfers()
    elif choice == "2":
        average()
    
    elif choice == "3":
        show_transfers()        
    
    elif choice == "4":
        reset_transfers()
        
    elif choice == "5":
        print("Έξοδος από το σύστημα.") 
        break
    else:
        print("Άκυρη επιλογή. Παρακαλώ δοκιμάστε ξανά.")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          