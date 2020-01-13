# put your code here.
text = open("twain.txt")
def count_word(text):
    words = {}

    for line in text:
        line_stripped = line.rstrip()
        list_word = line_stripped.split(" ")
        #print(word)
        for word in list_word:
            words[word] = words.get(word, 0) + 1

    return words
def print_word_count(word_dictionary):
    for word, count in word_dictionary.items():
        print(f'{word} {count}')

print_word_count(count_word(text)) 
