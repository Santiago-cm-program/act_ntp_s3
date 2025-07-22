count = 0
word = "programacion es divertida"
for letter in word.lower():
   if letter in ("a","e","i","o","u"):
       count +=1
print(f"La cantidad de vocales es {count}")