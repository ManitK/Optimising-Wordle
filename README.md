# Optimizing Wordle Guessing: Data Analysis and Strategic Selection

Code Repository for article (DOI:18.15001/JOT.2024/V12I6.24.490) published in [Volume 12, Issue 6 2024](https://journaloftechnology.org/volume-12-issue-6-2024/) of the **Journal of Technology**. This project aims to enhance the player's chances of success in the game of Wordle by employing mathematical strategies, common gameplay tactics combined with data analysis with strategic selection.


## csv folder 
5_letter_dict_foodle.csv = List of all 5 letter words in Foodle  
all_solns_scores.csv = Scores of all possible solutions in Wordle  
all_unique_solns_scores.csv = Scores of all possible solutions in Wordle having unique letters  
all_words_scores.csv = Scores of all possible guesses in Wordle  
foodle_scores.csv = Scores of all possible solutions in Foodle  
foodle_unique_scores.csv = Scores of all possible solutions in Foodle having unique letters  
valid_guesses.csv = List of all 5 letter words in dictionary (valid guesses)  
valid_solutions.csv = List of all solutions in Wordle (valid solutions)  

## notebooks
create_foodle_scores.ipynb = Python notebook used to calculate the word scores & seed words for Foodle  
for_all_valid_guesses.ipynb = Python Notebook used to create graphs, the word scores & seed words based on all valid guesses for Wordle  
for_all_valid_solutions.ipynb = Python Notebook used to create graphs based on all valid solutions for Wordle  

## programs
foodle_solver.py = Foodle Solver Program which takes input the answer and solves the Foodle Puzzle  
foodle_solver_testing.py = Testing Foodle Solver Program for each valid solution in Foodle  
testing.py = Testing Wordle Solver Program for each valid solution in Wordle  
wordle_solver.py = Wordle Solver Program which takes input the answer (word of the day) and solves Wordle  

Created by - 
Manit Kaushik  
manit22277@iiitd.ac.in  
