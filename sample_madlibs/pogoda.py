def madlib();

# user inputs
month = input("Miesiąc: ")
adj = input("Przymiotnik: ")
animal = input("Zwierzęta: ")

madlib = f"{month} zaskoczy nas swoją dynamiczną pogodą.\
W weekend pogoda zacznie się zmieniać i dla niektórych może być {adj}.\
Oznacza to, że trzeba być przygotowanym na ulewy, {animal}, ale też silne porywy wiatru."

#wywołanie całego tekstu 
print(madlib)
