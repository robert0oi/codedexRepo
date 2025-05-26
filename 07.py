'''
#Opening Files

file = open("example0.txt", a)

#To write on multiple lines, you can make in this mode
file.write("This is a line.\n")
file.write("This is the next line.\n")

#Or in this mode
lines = ['This is a line.\n', 'This is the next line.\n']
file.writelines(lines)

#--------------------------------------------------------#
#Reading Files
file = open("example.txt", "r")
conteudo = file.read()
print("Using read(): ", conteudo)

#Read line to line
line1 = file.readline() #Reading the 1st line
print(line1, end="") #Printing the 1st line

line2 = file.readline() #Reading the 2nd line
print(line2, end="") #Printing the 2nd line

To print each line on a single line without adding a '\n' newline character at the end, we use the end='' option in the print() function.


#--------------------------------------------------------#
#Closing Files

In Python, the .close() method is used to finish working with a file and free up resources.


file = open("example.txt", "r")

file.close()


Always call .close() after reading or writing to the file to ensure everything is saved.

You can also use a with block to open a file, handle it, and close it automatically:

with open('filename', 'r') as f:
  # handle file here

No .close() method necessary!
'''

#--------------------------------------------------------#
#Exercise down below:

liked_songs = {
  "Fogo nos Racistas": "Black Pantera",
  "El Anillo del Capitán Beto": "Invisible",
  "Me Gusta Este Tajo": "Pescado Rabioso",
  "Enjoy the Silence": "Depeche Mode",
  "Beautiful": "Gustavo Cerati"
}

def write_liked_songs_to_file(liked_songs, file_name):
    with open(file_name, "w") as file:
        file.write("Liked Songs:\n")
        for song, artist in songs.items():
            file.write(f"{song} by {artist}\n")
        print(f"Successfully added Liked songs to {file_name}")

write_liked_songs_to_file(liked_songs, "liked_songs.txt")