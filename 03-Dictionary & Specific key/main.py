sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
# Pay attention that the given sentence is a string, but the keys in the dictionary are words.
sentence_list = sentence.split()
word_counts = {}
for word in sentence_list:
    word_counts[word] = word_counts.get(word, 0) + 1

ks = list(word_counts.keys())
ks[0] = max_value_key
# Assign the first key to max_value_key, then compare its value with the next key, and assign the one with a larger value to max_value_key. Repeat the process till the end.
for k in ks:
    if word_counts[k] > word_counts[max_value_key]:
        max_value_key = k
print(word_counts, max_value_key)        
