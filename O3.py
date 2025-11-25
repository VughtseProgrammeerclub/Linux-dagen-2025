width = int(input("Breedte? "))
height = int(input("Hoogte? "))
char = input("Karakter? (bijv. *) ")
for _ in range(height):
    print(char * width)