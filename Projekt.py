import os

mark = "x "

# 2. Aufgaben hinzufügen
def add_task():
    file = open("todo_list.txt", "a+")  # öffnet eine Datei im Append-Modus
    task = input("Aufgabe: ")  # nimmt die Benutzereingabe auf
    try:
        file.write(task + "\n")  # Die Eingabe erscheint in einer neuen Zeile 
    except Exception as error:
        print(error)
    file.close()  # schließt die Datei

# 3. Aufgaben anzeigen
def show_task():
    file = open("todo_list.txt", "r")  # Öffnet die Datei im Lesemodus
    tasks = []
    try:
        tasks = file.readlines()  # Liest alle Zeilen der Datei und speichert sie in "tasks"
    except Exception as error:
        print(error)  # Falls ein Fehler passiert, wird es ausgegeben
    file.close()  
    
    if tasks:
        for index, task in enumerate(tasks, 1):  # Geht durch die Liste und numeriert jede Aufgabe (beginnt ab 1)
            print(f"{index}. {task.strip()}") # f-Strings: Ersetzt index durch die Nummer und {task.strip()} durch die Aufgabe ohne Leerzeichen/Zeilenumbrüche
    else:
        print("Keine Aufgaben vorhanden.")  # Falls nichts vorhanden ist

# 4. Aufgaben als erledigt markieren
def mark_task_done():
    file = open("todo_list.txt", "r")  
    try:
        tasks = file.readlines()  # Liest alle Zeilen der Datei und speichert sie in "tasks"
    except Exception as error:
        print(error)
    file.close()  
    
    if tasks:
        show_task()  # Aufgaben anzeigen
        try:
            index = int(input("Bitte wähle eine Zahl: ")) - 1  # Die ausgewählte Zahl ist die Nummer der Aufgabe
            if 0 <= index < len(tasks): # überprüft ob die Zahl gültig ist
                tasks[index] = mark + tasks[index]  # setzt das "X" an den Anfang der Aufgabe (als erledigt markieren)
            
            file = open("todo_list.txt", "w")  
            file.writelines(tasks)  # schreibt die Aufgabenliste in die Datei
            file.close()
        except Exception as error:
            print("Fehler aufgetreten:", error)
    else:
        print("Keine Aufgaben vorhanden.")

# 5. Aufgaben löschen
def delete_task():
    file = open("todo_list.txt", "r")  
    try:
        tasks = file.readlines()  
    except Exception as error:
        print(error)
    file.close()  
    
    if tasks:
        show_task()  
        try:
            index = int(input("Bitte wähle eine Zahl: ")) - 1  # Nutzer wählt eine Aufgabe
            if 0 <= index < len(tasks):
                del tasks[index]  # Löscht die Aufgabe aus der Liste
                file = open("todo_list.txt", "w")  
                file.writelines(tasks)  # speichert die aktuelle Liste ab
                file.close()
        except Exception as error:
            print("Fehler aufgetreten:", error)
    else:
        print("Keine Aufgaben vorhanden.")

# 6. Menü und Benutzerinteraktion
def main():
    while True: # while-Schleife läuft endlos weiter bis sie durch "break" beendet wird
        print("""
1. Aufgabe hinzufügen
2. Aufgaben anzeigen
3. Aufgabe als erledigt markieren
4. Aufgabe löschen
5. Beenden
        """)
        number = input("Bitte gebe eine Zahl ein: ")
        if number == "1":
            add_task()
        elif number == "2":
            show_task()
        elif number == "3":
            mark_task_done()
        elif number == "4":
            delete_task()
        elif number == "5":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Eingabe.")

if __name__ == "__main__":
    main() # Startet das Programm
