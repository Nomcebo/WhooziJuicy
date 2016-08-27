wjPatrons = ["A19", "B28", "C23", "D4", "E78", "F90", "G32", "H54", "I32", "J12", "J67", "L90", "M87", "N6", "O36",
             "P12", "Q24"]

print("Input List: " + str(wjPatrons) + "\n")
length = len(wjPatrons)

# --START Validate Age
# Check if age is under 18 or if = to 90 not if 90 and above just if = 90-- as per requirements in entry rule
wjEntranceQueue = []

for x in range(0, length):
    age = int(wjPatrons[x][1:])
    if age < 18:
        print(str(wjPatrons[x]) + " is under 18 and is being kicked out of the entrance queue!\n")
    elif age == 90:
        print
        str((wjPatrons[x]) + " is 90 and cannot be helped onto the entrance queue!\n")
    else:
        wjEntranceQueue.append(wjPatrons[x])
# --END Validate Age


