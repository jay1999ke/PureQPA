# parse.py file contains

import sys
import os
import nltk
from collections import Counter
from stanfordcorenlp import StanfordCoreNLP
import logging
import json
from nltk.parse import stanford
from nltk.tree import Tree
import importlib
importlib.reload(sys)
import time
#sys.setdefaultencoding('utf8')

''' 
Parts of the parse function is based on the following source
Citation: https://www.khalidalnajjar.com/setup-use-stanford-corenlp-server-python/
''' 

class Parse:

    def __init__(self, host='http://localhost', port=9000):
        print("[Stanford CoreNLP server version 3.9.1]")
        print("Initiating Connection with Stanford CoreNLP server.")
        print("Connecting to http://127.0.0.1:9000/",)
        t1 = time.time()
        self.nlp = StanfordCoreNLP(host, port=port,
                                   timeout=30000)#, quiet=True, logging_level=logging.DEBUG)
        print("Connection time: ",round(time.time()-t1,4),"Seconds")
        print("Established Connection with Stanford CoreNLP server.","\n\n")
        print("[Django server version 2.1.5]")
        self.props = {
            'annotators': 'tokenize,ssplit,pos,lemma,ner,parse,depparse,dcoref,relation',
            'pipelineLanguage': 'en',
            'outputFormat': 'json'
        }

    def word_tokenize(self, sentence):
        return self.nlp.word_tokenize(sentence)

    def pos(self, sentence):
        return self.nlp.pos_tag(sentence)

    def ner(self, sentence):
        return self.nlp.ner(sentence)

    def parse(self, sentence):
        return self.nlp.parse(str(sentence))

    def dependency_parse(self, sentence):
        return self.nlp.dependency_parse(sentence)

    def annotate(self, sentence):
        return json.loads(self.nlp.annotate(sentence, properties=self.props))

    @staticmethod
    def tokens_to_dict(_tokens):
        tokens = defaultdict(dict)
        for token in _tokens:
            tokens[int(token['index'])] = {
                'word': token['word'],
                'lemma': token['lemma'],
                'pos': token['pos'],
                'ner': token['ner']
            }
        return tokens

    def parse(self, sentence):
        return self.nlp.parse(sentence)