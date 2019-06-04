# PURE - A Question Paper Assistant

An online portal for educational organizations to conduct online examinations and help with the generation and answering of factual questions from text. 

Question paper assistant aims to facilitate the process of conducting online exams and to help the faculty with the generation of basic factual questions from given text. Along with this, it aims to provide a functionality of factual question answering. It provides
support to educational organizations to conduct hassle-free examinations with the help of state-of-art question generation techniques.

### Functionalities

  >Generation of basic factual questions from given text.
  
  >An online portal for conducting examinations.
  
  
## Appendix : Developer manual

### 1. Host system requirements

The project is primarily built to be run on servers. For development purposes, the
project can be run on a general commercial computer, but with the following
prerequisites:

    ● Java and Python language running capabilities with “pip”
    ● NLTK dataset
        o Can be downloaded by running the following commands in the python interpreter
            o import nltk
            o nltk.download()
    ● Django framework
        o Can be installed with the command in terminal “pip install django"
    ● Widget-tweaks django-module
        o Can be installed with the command in “pip install django-widget-tweaks”
    ● StanfordCoreNLP server
        o Should be downloaded and unzipped from https://stanfordnlp.github.io/CoreNLP/download.html
    ● StanfordCoreNLP python support
        o Can be installed with the command in “pip install stanfordcorenlp”

Note : It is advised to install Django,widget-tweaks & StanfordCoreNLP python support in a virtual environment so as to leave default system settings untouched.


### 2. How to initiate servers

The project requires 2 server initiations. One is for the main Django server and the
other is for StanfordCoreNLP

    ● To start the StanfordCoreNLP server, the following command shall be run at the location of unzipped StanfordCoreNLP files. This should be done before the next step.
        o “ java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -annotators "tokenize,ssplit,pos,lemma,parse,sentiment" -port 9000 -timeout 30000 ”
    ● To start the Django server, the following command shall be run at the location of the project.
        o “ python qpa runserver ”



The project website can be accessed at “127.0.0.1:8000.”
