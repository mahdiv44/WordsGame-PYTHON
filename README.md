# 🧠 Word Game in Python
This is a text-based word game implemented in Python where the player builds valid words using a given set of random letters (a "hand"). The goal is to make as many valid English words as possible from those letters to achieve a high score.

Inspired by games like Scrabble, this project includes score calculations, dictionary validation, letter tracking, and word verification.

## 🎯 Game Objective
The player is dealt a random hand of letters and must form valid English words using those letters. Each word earns a score based on:

The letters used (each letter has a point value)

The word length

A bonus formula that encourages using more letters

The player continues forming words until the hand is empty or they choose to stop.

## 🧩 Features
Score calculation based on Scrabble-style letter values.

Support for wildcard letters (*) that can represent any vowel.

Automatic updating of the letter hand after each word.

Word validation using a provided word list (word_list).

Unit tests for key functions.

## 🛠 Key Functions
get_word_score(word, n)
Calculates the score for a given word:

Sum of letter values

Multiplied by a bonus factor:

perl
Copy
Edit
score = (letter values) * max(1, 7 * word length - 3 * (n - word length))
Where n is the hand size.

update_hand(hand, word)
Removes the letters used in the word from the current hand.
Returns a new hand dictionary, keeping the original unchanged.

is_valid_word(word, hand, word_list)
Checks:

If the word exists in the dictionary

If the player has the necessary letters in their current hand

Supports wildcard character *, which can be any vowel

get_frequency_dict(sequence)
Utility function that returns a dictionary with the frequency of each element (used for counting letters in words and hands).

# 🧪 Tests
This project includes test functions to validate correctness:

test_get_word_score(): Ensures scoring is calculated properly.

test_update_hand(): Ensures that used letters are correctly removed.

test_is_valid_word(): Ensures that word validation logic works.

test_wildcard(): Specifically tests word validation when wildcards are used.

## 💡 Future Improvements
Add a user interface (text-based or GUI)

Allow multiplayer turns

Implement a timer or difficulty levels

Track high scores

# 📂 How to Run
Clone the repository

Ensure Python 3 is installed

Run the main script in your terminal or IDE

Make sure to provide a valid word list file (e.g., words.txt)

# 🗃 Example Word List File
The word list file (words.txt) should contain valid English words, one per line. Example:

python-repl
Copy
Edit
apple
quiet
mouse
...
