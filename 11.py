# 1)WAP to ask for a sentence and calculate the frequency of characters in the sentences.
def calculateSentFreq(sentence):
    letter_count ={}
    for char in sentence:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
        
    for letter, count in letter_count.items():
        print(f'{letter}: {count}')
    
sentence = "the quick brown fox jumps over the lazy dog"
calculateSentFreq(sentence)
