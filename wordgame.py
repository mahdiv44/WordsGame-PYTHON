import math
import random
import string

def get_word_score(word, n):
    word = word.lower()
    letter_points = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1,
        'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8,
        'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1,
        'p': 3, 'q': 10,'r': 1, 's': 1, 't': 1,
        'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4,
        'z': 10, '*': 0
    }

    score1 = sum([letter_points.get(letter, 0) for letter in word])
    score2 = max(1, 7 * len(word) - 3 * (n - len(word))) #mohasebeye score
    return score1 * score2 #natayej akhar
def test_get_word_score():
    """
    Unit test for get_word_score
    """
    failure=False
    # dictionary of words and scores
    words = {("", 7):0, ("it", 7):2, ("was", 7):54, ("weed", 6):176,
             ("scored", 7):351, ("WaYbILl", 7):735, ("Outgnaw", 7):539,
             ("fork", 7):209, ("FORK", 4):308}
    for (word, n) in words.keys():
        score = get_word_score(word, n)
        if score != words[(word, n)]:
            print("FAILURE: test_get_word_score()")
            print("\tExpected", words[(word, n)], "points but got '" + \
                  str(score) + "' for word '" + word + "', n=" + str(n))
            failure=True
    if not failure:
        print("SUCCESS: test_get_word_score()")

def test_update_hand():
    """
    Unit test for update_hand
    """
    # test 1
    handOrig = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
    handCopy = handOrig.copy()
    word = "quail"

    hand2 = update_hand(handCopy, word)
    expected_hand1 = {'l':1, 'm':1}
    expected_hand2 = {'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print("FAILURE: test_update_hand('"+ word +"', " + str(handOrig) + ")")
        print("\tReturned: ", hand2, "\n\t-- but expected:", expected_hand1, "or", expected_hand2)

        return # exit function
    if handCopy != handOrig:
        print("FAILURE: test_update_hand('"+ word +"', " + str(handOrig) + ")")
        print("\tOriginal hand was", handOrig)
        print("\tbut implementation of update_hand mutated the original hand!")
        print("\tNow the hand looks like this:", handCopy)

        return # exit function

    # test 2
    handOrig = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    handCopy = handOrig.copy()
    word = "Evil"

    hand2 = update_hand(handCopy, word)
    expected_hand1 = {'v':1, 'n':1, 'l':1}
    expected_hand2 = {'e':0, 'v':1, 'n':1, 'i':0, 'l':1}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print("FAILURE: test_update_hand('"+ word +"', " + str(handOrig) + ")")
        print("\tReturned: ", hand2, "\n\t-- but expected:", expected_hand1, "or", expected_hand2)

        return # exit function

    if handCopy != handOrig:
        print("FAILURE: test_update_hand('"+ word +"', " + str(handOrig) + ")")
        print("\tOriginal hand was", handOrig)
        print("\tbut implementation of update_hand mutated the original hand!")
        print("\tNow the hand looks like this:", handCopy)

        return # exit function

    # test 3
    handOrig = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    handCopy = handOrig.copy()
    word = "HELLO"

    hand2 = update_hand(handCopy, word)
    expected_hand1 = {}
    expected_hand2 = {'h': 0, 'e': 0, 'l': 0, 'o': 0}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print("FAILURE: test_update_hand('"+ word +"', " + str(handOrig) + ")")
        print("\tReturned: ", hand2, "\n\t-- but expected:", expected_hand1, "or", expected_hand2)

        return # exit function

    if handCopy != handOrig:
        print("FAILURE: test_update_hand('"+ word +"', " + str(handOrig) + ")")
        print("\tOriginal hand was", handOrig)
        print("\tbut implementation of update_hand mutated the original hand!")
        print("\tNow the hand looks like this:", handCopy)

        return # exit function

    print("SUCCESS: test_update_hand()")

def test_is_valid_word(word_list):
    """
    Unit test for is_valid_word
    """
    failure=False
    # test 1
    word = "hello"
    handOrig = get_frequency_dict(word)
    handCopy = handOrig.copy()

    if not is_valid_word(word, handCopy, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", handOrig)

        failure = True

    # Test a second time to see if word_list or hand has been modified
    if not is_valid_word(word, handCopy, word_list):
        print("FAILURE: test_is_valid_word()")

        if handCopy != handOrig:
            print("\tTesting word", word, "for a second time - be sure you're not modifying hand.")
            print("\tAt this point, hand ought to be", handOrig, "but it is", handCopy)

        else:
            print("\tTesting word", word, "for a second time - have you modified word_list?")
            wordInWL = word in word_list
            print("The word", word, "should be in word_list - is it?", wordInWL)

        print("\tExpected True, but got False for word: '" + word + "' and hand:", handCopy)

        failure = True


    # test 2
    hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
    word = "Rapture"

    if  is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True

    # test 3
    hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
    word = "honey"

    if  not is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected True, but got False for word: '"+ word +"' and hand:", hand)

        failure = True

    # test 4
    hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
    word = "honey"

    if  is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True

    # test 5
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = "EVIL"

    if  not is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", hand)

        failure = True

    # test 6
    word = "Even"

    if  is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)
        print("\t(If this is the only failure, make sure is_valid_word() isn't mutating its inputs)")

        failure = True

    if not failure:
        print("SUCCESS: test_is_valid_word()")

def test_wildcard(word_list):
    """
    Unit test for is_valid_word
    """
    failure=False

    # test 1
    hand = {'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1}
    word = "e*m"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True

    # test 2
    hand = {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
    word = "honey"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected False, but got True for word: '"+ word +"' and hand:", hand)

        failure = True

    # test 3
    hand = {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
    word = "h*ney"

    if not is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected True, but got False for word: '"+ word +"' and hand:", hand)

        failure = True

    # test 4
    hand = {'c': 1, 'o': 1, '*': 1, 'w': 1, 's':1, 'z':1, 'y': 2}
    word = "c*wz"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected False, but got True for word: '"+ word +"' and hand:", hand)

        failure = True

    # dictionary of words and scores WITH wildcards
    words = {("h*ney", 7):290, ("c*ws", 6):176, ("wa*ls", 7):203}
    for (word, n) in words.keys():
        score = get_word_score(word, n)
        if score != words[(word, n)]:
            print("FAILURE: test_get_word_score() with wildcards")
            print("\tExpected", words[(word, n)], "points but got '" + \
                  str(score) + "' for word '" + word + "', n=" + str(n))
            failure=True

    if not failure:
        print("SUCCESS: test_wildcard()")


def test_game(word_list):
  word_list = load_words()
  print("----------------------------------------------------------------------")
  print("Testing get_word_score...")
  test_get_word_score()
  print("----------------------------------------------------------------------")
  print("Testing update_hand...")
  test_update_hand()
  print("----------------------------------------------------------------------")
  print("Testing is_valid_word...")
  test_is_valid_word(word_list)
  print("----------------------------------------------------------------------")
  print("Testing wildcards...")
  test_wildcard(word_list)
  print("All done!")

  VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
WORDLIST_FILENAME = "words.txt"
def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist
def get_frequency_dict(sequence):
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

word_list = load_words()
def deal_hand(n):

    hand={}
    num_vowels = int(math.ceil(n / 3))
    VOWELS = 'aeiou'
    CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
    HAND_SIZE = 7

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand
def update_hand(hand, word):
    new_hand = hand.copy()
    word = word.lower()
    for letter in word:
        if letter in new_hand and new_hand[letter] > 0:
            new_hand[letter] -= 1
    return {k: v for k, v in new_hand.items() if v > 0}
def is_valid_word(word, hand, word_list):
    word = word.lower()

    if word not in word_list:
        return False

    temp_hand = hand.copy()

    for letter in word:
        if temp_hand.get(letter, 0) > 0:
            temp_hand[letter] -= 1
        else:
            return False

    return True
def is_valid_word_with_wildcard(word, hand, word_list):
    if '*' not in word:
        if word in word_list:
            hand_copy = hand.copy()
            for letter in word:
                if hand_copy.get(letter, 0) == 0:
                    return False
                else:
                    hand_copy[letter] -= 1
            return True
        else:
            return False
    else:
        for vowel in 'aeiou':
            possible_word = word.replace('*', vowel)
            if possible_word in word_list:
                hand_copy = hand.copy()
                for letter in word:
                    if letter == '*':
                        if hand_copy.get('*', 0) == 0:
                            return False
                        else:
                            hand_copy['*'] -= 1
                    else:
                        if hand_copy.get(letter, 0) == 0:
                            return False
                        else:
                            hand_copy[letter] -= 1
                return True
        return False
def display_hand(hand):
         output = []
         for letter in hand:
              output.extend([letter] * hand[letter])
              print(" ".join(output))

def calculate_handlen(hand):
    return sum(hand.values())
def play_hand(hand, word_list):
    total_score = 0

    while calculate_handlen(hand) > 0:
        print("Current hand: ", end="")
        display_hand(hand)

        word = input("Please enter a word or '!!' to indicate you are done: ").strip().lower()

        if word == '!!':
            break

        if is_valid_word_with_wildcard(word, hand, word_list):
            score = get_word_score(word, calculate_handlen(hand))
            total_score += score
            print(f'"{word}" earned {score} points. Total: {total_score} points')
        else:
            print("That is not a valid word. Please choose another word.")

        hand = update_hand(hand, word)

    if calculate_handlen(hand) == 0:
        print(f"Ran out of letters. Total score for this hand: {total_score}")
    else:
        print(f"Total score for this hand: {total_score}")

    return total_score
def calculate_handlen(hand):
    return sum(hand.values())

def substitute_hand(hand, letter):
    VOWELS = 'aeiou'
    CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
    HAND_SIZE = 7

    letter = letter.lower()
    if letter not in hand:
        return hand

    all_letters = VOWELS + CONSONANTS
    available_letters = [l for l in all_letters if l not in hand and l != '*']

    new_letter = random.choice(available_letters)
    new_hand = hand.copy()
    new_hand[new_letter] = new_hand.pop(letter)
    return new_hand

word_list = load_words()
def play_hand(hand, word_list):
    total_score = 0

    while calculate_handlen(hand) > 0:
        print("Current hand: ", end="")
        display_hand(hand)

        word = input("Please enter a word or '!!' to indicate you are done: ").strip().lower()

        if word == '!!':
            break

        if is_valid_word_with_wildcard(word, hand, word_list):
            score = get_word_score(word, calculate_handlen(hand))
            total_score += score
            print(f'"{word}" earned {score} points. Total: {total_score} points')
        else:
            print("That is not a valid word. Please choose another word.")

        hand = update_hand(hand, word)

    if calculate_handlen(hand) == 0:
        print(f"Ran out of letters. Total score for this hand: {total_score}")
    else:
        print(f"Total score for this hand: {total_score}")

    return total_score

def play_game(word_list):
    total_hands = int(input("Enter total number of hands: "))
    total_score_all = 0
    replay_used = False

    for i in range(total_hands):
        hand = deal_hand(HAND_SIZE)

        print(f"\nCurrent hand: ", end="")
        display_hand(hand)

        substitute = input("Would you like to substitute a letter? ").strip().lower()
        if substitute == 'yes':
            letter = input("Which letter would you like to replace: ").strip().lower()
            hand = substitute_hand(hand, letter)

        print(f"\nPlaying hand {i + 1}...")
        hand_score = play_hand(hand, word_list)

        if not replay_used:
            replay = input("Would you like to replay the hand? ").strip().lower()
            if replay == 'yes':
                print("\nReplaying the hand...")
                replay_score = play_hand(hand, word_list)
                hand_score = max(hand_score, replay_score)
                replay_used = True

        total_score_all += hand_score

    print(f"\nTotal score over all hands: {total_score_all}")




play_game(word_list)