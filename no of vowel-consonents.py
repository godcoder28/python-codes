file = open("data_old.txt", "r")
vowel = 0
consonant = 0
upper = 0
lower = 0
for i in file.read():
    if i.islower():
        lower += 1
    elif i.isupper():
        upper += 1

    if i in ['a', 'e', 'i', 'o', 'u', 'A','E' 'I', 'O','U']:
        vowel += 1
    elif i.isalpha() and i not in \
         ['a', 'e', 'i', 'o', 'u', 'A','E' 'I', 'O','U']:
        consonant += 1

print("No of vowel, consonent, upper, lower are: ",\
      vowel, consonant, upper, lower)
