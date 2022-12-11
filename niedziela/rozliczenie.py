#1. Odczyt pliku csv z zapisem poszczegolnych pol
path = 'C:\\Users\\vdi-student\\Desktop\\rozliczenie.csv'
mode = 'r'
with open (path, mode) as plik:
    content = plik.readlines()
print(content[3])

for i in range (len(content)):
    print(content[i])
    content[i] = content[i].split(',')
    print(content[i])
    #print(content[2][2])

#2.Obliczenie sredniej wyplaty

total = 0
for i in range (1, len(content)):
    total = total + int(content[i][1])
print("Suma wynagrodzenia: " , total)
average = total / (len(content)-1)
print("Srednia wynagrodzen: " , (round(average,2)))

#3.Ile kobiet jest na macierzynskim.

total = 0
for i in range(1,len(content)):
    print(content[i])
    content[i][4] = content[i][4].replace('\n', '')
    if content[i][4] == 't' and content[i][3] == 'k':
        total = total + 1
print(total)


