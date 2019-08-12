import re

def Find_Email_Addresses(file):
    with open(file, "r") as f:
        matches = list()
        lines = f.readlines()
        for line in lines:
            line = line.split(" ")
            for word in line:
                if "@" in word: matches.append(word)
    with open("Email_Addresses_From_" + file, "w") as file: file.write("\n".join(matches))

Find_Email_Addresses("Sample.txt")