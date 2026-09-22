def word_frequency(sentence):
    frequency = {}

    for word in sentence.split():
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


sentence = input("Enter A Sentence : ")
print(word_frequency(sentence))
