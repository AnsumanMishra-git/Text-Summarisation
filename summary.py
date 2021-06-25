# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 01:06:26 2021

@author: hp
"""

text="During the Jagannath Rath jatra, the triads are usually worshiped in the sanctum of the temple at Puri, but once during the month of Asadha (Rainy Season of Odisha, usually falling in month of June or July), they are brought out onto the Bada Danda (main street of Puri) and travel to the Shri Gundicha Temple, in huge chariots (ratha), allowing the public to have darśana (Holy view). This festival is known as Rath Jatra, meaning the journey (jatra) of the chariots (ratha). The Rathas are huge wheeled wooden structures, which are built anew every year and are pulled by the devotees. The chariot for Jagannath is approximately 45 feet high and 35 feet square and takes about 2 months to construct.[8] The artists and painters of Puri decorate the chariots and paint flower petals and other designs on the wheels, the wood-carved charioteer and horses, and the inverted lotuses on the wall behind the throne. The Ratha-Jatra is also termed as the Shri Gundicha jatra. The most significant ritual associated with the Ratha-jatra is the chhera pahara. During the festival, the Gajapati King wears the outfit of a sweeper and sweeps all around the deities and chariots in the Chera Pahara (sweeping with water) ritual. The Gajapati King cleanses the road before the chariots with a gold-handled broom and sprinkles sandalwood water and powder with utmost devotion. As per the custom, although the Gajapati King has been considered the most exalted person in the Kalingan kingdom, he still renders the menial service to Jagannath. This ritual signified that under the lordship of Jagannath, there is no distinction between the powerful sovereign Gajapati King and the most humble devotee. Chera pahara is held on two days, on the first day of the Ratha Jatra, when the deities are taken to garden house at Mausi Maa Temple and again on the last day of the festival, when the deities are ceremoniously brought back to the Shri Mandir."

#Tokenization - converting the sentences into tokens 

import string
punc=string.punctuation #string punc contains all the punctuations

#Data Cleaning  
import spacy
nlp = spacy.load('en_core_web_sm')
from spacy.lang.en.stop_words import STOP_WORDS
doc=nlp(text)

tokens = [token.text for token in doc]
print(tokens)


#making a list of stopwords
stopwords = list(STOP_WORDS)

#counting frequencies of each word
freq = {}
for word in doc:
    if word.text.lower() not in stopwords:
        if word.text.lower() not in punc:
            if word.text not in freq.keys():
                freq[word.text] = 1
            else:
                freq[word.text] += 1
                
print(freq)

max_frequency = max(freq.values())
max_frequency

#normalising the token w.r.t the max freq
for word in freq.keys():
    freq[word]=freq[word]/max_frequency
print(freq)  
 
sentence_tokens = [sent for sent in doc.sents]
print(sentence_tokens)


sentence_scores = {} #it helps us to select those sentences which have most frequent words
for sent in sentence_tokens:
    for word in sent:
        if word.text.lower() in freq.keys():
            if sent not in sentence_scores.keys():
                sentence_scores[sent] = freq[word.text.lower()]
            else:
                sentence_scores[sent] += freq[word.text.lower()]
                
sentence_scores

#get 40% of sentences with maximum score
from heapq import nlargest
chosen_len = int(len(sentence_tokens)*0.4)
chosen_len

summary = nlargest(chosen_len, sentence_scores, key = sentence_scores.get)
summary
 

final_summary = [word.text for word in summary]
final_summary
summary = ' '.join(final_summary)

print(text)

print(summary)
len(text)
len(summary)












