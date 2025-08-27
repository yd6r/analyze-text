#Imports the file with the text to be read
import ch1text
import dorian


def count_sentences(text):
    count=0

    TERM_CHARS = ".;?!"
    for char in text:
        if char in TERM_CHARS:
            count+=1

    return count

def count_syllables_in_word(word):
    count=0
    word=word.lower()

    ENDINGS='.,;!?:'
    last_char=word[-1]

    if last_char in ENDINGS:
        processed_word=word[0:-1]
    else:
        processed_word=word
    if len(processed_word)<=3:
        return 1

    if processed_word[-1] in "e":
        processed_word=processed_word[0:-1]

    VOWELS="aeiou"
    prev_char_vowel = False

    for char in processed_word:
        if char in VOWELS:
            if not prev_char_vowel:
                count=count+1
            prev_char_vowel=True
        else:
            prev_char_vowel=False

    if processed_word[-1] in 'y':
        count+=1

    return count


def count_syllables(words):
    count=0
    for word in words:
        word_count=count_syllables_in_word(word)
        count=count+word_count
    return count

    return syllables

def output_results(score):
    if score>=90.0:
        print('Reading level of 5th Grade')
    elif score>=80.0:
        print('Reading level of 6th Grade')
    elif score>=70.0:
        print('Reading level of 7th Grade')
    elif score>=60.0:
        print('Reading level of 8-9th Grade')
    elif score>=50.0:
        print('Reading level of 10-12th Grade')
    elif score>=30.0:
        print('Reading level of College Student')
    else:
        print('Reading level of College Graduate')


def compute_readability(text):
    #Creates the basic variables needed for the algorithm
    total_words=0
    total_sentences=0
    total_syllables=0
    score=0

    #Counts total words in the text and creates a list words[] which contains the broken up text
    words=text.split()
    total_words=len(words)
    total_sentences=count_sentences(text)
    total_syllables=count_syllables(words)

    score=(206.835-1.015 * (total_words/total_sentences)
           -84.6*(total_syllables/total_words))

    print(total_words, 'words')
    print(total_sentences, 'sentences')
    print(total_syllables, 'syllables')
    output_results(score)





compute_readability(dorian.text)
