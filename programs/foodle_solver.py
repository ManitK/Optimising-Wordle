answer = input("Input Answer: ")
print()

import csv
def get_answer_arr():
    answers_arr = []
    with open('/Users/manitk/Desktop/Wordle/csv/5_letter_dict_foodle.csv', mode='r') as answers_list:
        answers_list = csv.reader(answers_list)
        for i in answers_list:
            answers_arr.append(i[0])
    return answers_arr

def get_letter_indices(word, letter):
    index_list = [i for i, ch in enumerate(word) if ch == letter]
    return index_list

def get_scores(arr):
    guess_scores = {}  # Scores for all the remaining guesses
    with open('/Users/manitk/Desktop/Wordle/csv/foodle-scores-new.csv', mode='r') as scores_list:
        scores_list = csv.DictReader(scores_list)
        for row in scores_list:
            word = row['Word']
            score = float(row['Score'])
            if word in arr:
                guess_scores[word] = score
    return guess_scores

answers_arr = get_answer_arr()
guess_scores = get_scores(answers_arr)
grey_letters = []        # List of All Alphabets which aren't in the answer
yellow_letters_dict = {} # key - alphabet   : value - indexes where this alphabet is not present in answer
green_letters_dict = {}  # key - index      : value - correct alphabet at this index
guess_set = set()        # Filter out words that don't fit our information

guesses = 0

while guesses <= 6:
    seed_words = ["salty","boned","prick"]
    if(guesses < 3):
        highest_score_word = seed_words[guesses]
    else:
        highest_score_word = max(guess_scores, key=guess_scores.get)
    guesses += 1
    print("Guess Number: ",guesses)
    print("Guessing:", highest_score_word)

    if highest_score_word == answer:
        print("Correct!")
        break
    
    print("\nIncorrect!")
    new_green = []
    new_yellow = []
    new_grey = []
    new_indexes = {}
    info_about_index = [] # Indexes of Guess for which I have information

    for i in green_letters_dict:
        info_about_index.append(i)

    for i in range(len(highest_score_word)):
        if highest_score_word[i] not in answer:  # check for grey letters
            grey_letters.append(highest_score_word[i])
            info_about_index.append(i)
        else: # check for green letters
            if answer[i] == highest_score_word[i]:  # letter is in answer and at correct index
                #if highest_score_word[i] not in green_letters_dict.values(): # check if already letter is not in green_letters_dict
                green_letters_dict[i] = highest_score_word[i]
                info_about_index.append(i)
    
    green_letters_dict = dict(sorted(green_letters_dict.items(), key=lambda item: item[0]))

    #check for yellow letters
    for i in range(len(highest_score_word)):
        if i not in info_about_index:
            if bool(yellow_letters_dict.get(highest_score_word[i])) == False:
                yellow_letters_dict[highest_score_word[i]] = [i]
            else:
                if i not in yellow_letters_dict[highest_score_word[i]]:
                    yellow_letters_dict[highest_score_word[i]].append(i)

    green_letters_dict.update(new_indexes)  # Update the green letters dictionary
    print("\nUpdated green - ", green_letters_dict)
    print("Updated yellow - ", yellow_letters_dict)
    print("Updated grey - ", grey_letters,"\n")

    for word in answers_arr:
        if word not in guess_set:
            count = 0
            for i in green_letters_dict:
                if word[i] == green_letters_dict[i]:
                    count += 1
            if count != len(green_letters_dict):
                #print("Removed By New Green -  ",word)
                guess_set.add(word)
                guess_scores.pop(word)

    for word in answers_arr:
        if word not in guess_set:
            count = 0
            for i in grey_letters:
                if i in word:
                    #print("Removed By New Grey - ",word)
                    guess_set.add(word)
                    guess_scores.pop(word)
                    break

    for word in answers_arr:
        if word not in guess_set:
            count = 0
            for letter in yellow_letters_dict:
                if letter in word:
                    for index in yellow_letters_dict[letter]:
                        if word[index] != letter:
                            count += 1
            total = []
            for lst in yellow_letters_dict.values():
                total.extend(lst)
            if count != len(total):
                #print("Removed By New Yellow -  ",word)
                guess_set.add(word)
                guess_scores.pop(word)
    if(guesses>3):
        print("Remaing Guess List After Guess ",guesses," is - ",guess_scores)