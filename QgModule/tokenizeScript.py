import sys
import os
import nltk
from QgModule.name_entity_processing import NEP
    
class Tokenise:
    """ tokenize wiki article into sentences with top_k option """ 
    def main(self, k, article, topK = True):
        acc = []
        # 1. tokenize chunk of raw string into sentence
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        raw_data = article
        NEP_output = NEP.transform_pronoun(raw_data)
        raw_data = NEP_output[0]

        NE = NEP_output[1]
        # print "***********", raw_data
        sentences = (tokenizer.tokenize(raw_data))
        # 2. filter out ill-format sentences := ones contain new line symbol
        sentences = [si for si in sentences if "\n" not in si]
        #sentences = [s.encode('ascii', 'ignore') for s in sentences]
        # if we want to get top k shortest sentences
        if topK:
            # 3. get top 10 shortest sentences
            sentences_top_k = sorted(sentences, key = len)[:k]
            sentences = sentences_top_k
        
        if(True):
            print("\nCheck Point 2: Sentence selection")
            print(sentences)
        
        return [sentences, NE]

NEP = NEP()