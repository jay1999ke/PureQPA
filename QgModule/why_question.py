import sys
import os
import nltk
from collections import Counter
import numpy as np
# import matplotlib.pyplot as plt
from stanfordcorenlp import StanfordCoreNLP
import logging
import json
from nltk.parse import stanford
from nltk.tree import Tree as Tree
from parse_sentence import *
from pattern.en import conjugate
from pattern.en import tenses
from binary import *
import importlib
importlib.reload(sys)  
#sys.setdefaultencoding('utf8')

# sNLP = StanfordNLP()
Binary = Binary()

class Why:

	def is_why(self, tree):
		for t in tree.subtrees(lambda t: t.label() == "SBAR"):
			if "because" in t.leaves() or "since" in t.leaves() or "so" in t.leaves():
					return True
		return False

	def remove_SBAR(self, tree):
		top_level_structure = []
		parse_by_structure = []
		for t in tree[0]:
			if t.label() != "SBAR" and t.label() != "VP" and t.label() != ",":
				parse_by_structure.append(" ".join(t.leaves()))
				top_level_structure.append(t.label())
			elif t.label() == "VP":
				for tt in t:
					if tt.label() != "SBAR":
						parse_by_structure.append(" ".join(tt.leaves()))
						top_level_structure.append(tt.label())
		return (top_level_structure, parse_by_structure)

	def main(self, text,parser):
		print(text)
		tree = parser.parse(text)
		tree = Tree.fromstring(str(tree))
		# print tree
		if not self.is_why(tree):
			print ("It could not be converted to why question.") 
		(top_level_structure, parse_by_structure) = self.remove_SBAR(tree)
		# print top_level_structure
		# print parse_by_structure
		sent = " ".join(parse_by_structure)
		sent = Binary.main(sent,parser)
		print("Why " + sent)
		return ("Why " + sent)


# Why = Why()
# Why.main("it periodically brightens by one magnitude or less because it is a flare star.")
# Why.main("he is tall since he is a good man.")
# Why.main("because he lives a good life, he never likes her.")

