import sys
import os
import nltk
from collections import Counter
# import matplotlib.pyplot as plt
from stanfordcorenlp import StanfordCoreNLP
import logging
import json
from nltk.parse import stanford
from nltk.tree import Tree as Tree
from QgModule.parse import Parse
from pattern.en import conjugate
from pattern.en import tenses
from QgModule.binary import *
import importlib
importlib.reload(sys)  
#sys.setdefaultencoding('utf8')

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
		tree = parser.parse(text)
		tree = Tree.fromstring(str(tree))
		if not self.is_why(tree):
			return None 
		(top_level_structure, parse_by_structure) = self.remove_SBAR(tree)
		sent = " ".join(parse_by_structure)
		sent = Binary.main(sent,parser)
		return "Why " + sent
  

