import os
import nltk

if not 'neg_text' in globals() or not 'pos_text' in globals():
    from read_text import neg_text, pos_text

words = {}

neg_words = []
pos_words = []

neg = []
pos = []

for text in neg_text:
    tokens = nltk.word_tokenize(text)
    neg_words.append(tokens)
    
    for token in tokens:
        if not token in words:
            words[token] = 0
        words[token] += 1

for text in pos_text:
    tokens = nltk.word_tokenize(text)
    pos_words.append(tokens)
    
    for token in tokens:
        if not token in words:
            words[token] = 0
        words[token] += 1

words_filtered = dict((k, v) for k, v in words.items() if v >= 4)

words_key = words_filtered.keys()

words_index = dict((k, v) for v, k in enumerate(words_key))

word_len = len(words_filtered)

for tokens in neg_words:
    d = [0] * word_len

    for token in tokens:
        if token in words_filtered:
            d[words_index[token]] = 1

    neg.append(d)

for tokens in pos_words:
    d = [0] * word_len
    
    for token in tokens:
        if token in words_filtered:
            d[words_index[token]] = 1

    pos.append(d)

posfile = open("./pos_vec.txt", "w")
posfile.write(str(pos))
posfile.close()

negfile = open("./neg_vec.txt", "w")
negfile.write(str(neg))
negfile.close()
