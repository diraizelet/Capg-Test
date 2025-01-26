#counts the numeber of  times the word repeates in the same sentence
def word_counter(sentence):
    words = sentence.split()
    word_count = {}
    
    for word in words:
        word = word.lower()  # Convert to lowercase to ensure case insensitivity
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    counts = word_counter(sentence)
    for word, count in counts.items():
        print(f"{word}: {count}")