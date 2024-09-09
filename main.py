import pandas


'''
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
nato_alphabet = {
    "A": "Alfa",    "B": "Bravo",    "C": "Charlie", "D": "Delta",
    "E": "Echo",    "F": "Foxtrot",  "G": "Golf",    "H": "Hotel",
    "I": "India",   "J": "Juliett",  "K": "Kilo",    "L": "Lima",
    "M": "Mike",    "N": "November", "O": "Oscar",   "P": "Papa",
    "Q": "Quebec",  "R": "Romeo",    "S": "Sierra",  "T": "Tango",
    "U": "Uniform", "V": "Victor",   "W": "Whiskey", "X": "X-ray",
    "Y": "Yankee",  "Z": "Zulu"
}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
'''

data=pandas.read_csv("nato_phonetic_alphabet.csv")
dict={r.letter:r.code for (i,r) in data.iterrows()}
print(dict)
ans=input("Enter WORD FOR NATO CONVERSION:").upper()
ans_list=[]
for i in ans:
    ans_list.append(i)
list_words=[]
for i in ans_list:
    for (k,v) in dict.items():
        if i==k:
            list_words.append(v)
print(list_words)

