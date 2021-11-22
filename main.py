def sort_sentence(sentence):
    sentence = sentence.split()
    for i in range(len(sentence)-1):
        for j in range(len(sentence)-i-1):
            if len(sentence[j]) > len(sentence[j+1]):
                sentence[j], sentence[j+1] = sentence[j+1],sentence[j]
    return ' '.join(sentence).lower().capitalize()

if __name__ == '__main__':
    print(sort_sentence("Keep calm and carry on"))