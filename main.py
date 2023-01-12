import pandas
data=pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)

my_dict={raw.letter:raw.code for (index,raw) in data.iterrows()}


user_input=input("Enter your name: ").upper()
for letter in user_input:
    print(my_dict[letter])