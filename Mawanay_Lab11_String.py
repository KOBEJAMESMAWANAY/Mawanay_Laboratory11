#Introductory message
print("Hi! Please enter 10 words.")

#Variable for word results
print_word_list= []

#WORDS define the ten words inputted by the user
WORDS = []
for i in range (10):
    TEN_WORDS = input(f"Please enter your word {i+1}: ")
    WORDS.append(TEN_WORDS)

#request number input of the user    
Number_In_Letters = int(input("Please enter any number: "))

#initialize words that match with numbers=letters
Match_Words = []
for TEN_WORDS in WORDS:
    if len(TEN_WORDS) .= Number_In_Letters:
        print_word_list.append(TEN_WORDS)

#Displaying the results
if len(print_word_list) == 0:
    print(f"Unfortunately, there are no words found with {Number_In_Letters} letter/s.")
else:
    print(f"Here are the words found with {Number_In_Letters} letter/s: ", print_word_list)
