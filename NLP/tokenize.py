from pprint import pprint  # pretty-printer
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import gensim;
import os;
import nltk.data;
import time;
import numpy as np;
import matplotlib.pyplot as plt;
from sklearn.manifold import TSNE;

# The method does the following in order
# 1- It convert the copra paragraph into array of sentences using punkt tokenizer
# 2- It then tokenize each line in paragraph into words and remove the stop words and the special characters
def tokenize(line):
    specialCharacters = ['@','#',',','.','(',')','*',';'] # array of special characters used for prune out the tokens
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    tknzr = TweetTokenizer()
    tokenized = sent_detector.tokenize(line.strip());
    wordList = [];
    for line in tokenized:
        wordList.extend(tknzr.tokenize(line));
    tokenized = [word for word in wordList if word not in
    stopwords.words('english') and word not in specialCharacters]
    return tokenized  

def tokens2Index(tokenArr, model):
    index = np.array([]);
    for token in tokenArr:
        try:
            index =  np.append(index,model.wv.index2word.index(token));
        except ValueError:
            index = np.append(index, -1);
    return index;

selectedModel = 'model-sg-1-size-600-window-10'
modelLoad = gensim.models.Word2Vec.load('./wordToVec/%s'%(selectedModel))

tokenized = [];

dirName = './train-corpus';
readFiles = 0
allFiles = len([name for name in os.listdir(dirName)])
for fname in os.listdir(dirName):
    readFiles = readFiles + 1
    print('learning model: %d / %d'%(readFiles, allFiles), end="\r" )
    filename, fileExtension = os.path.splitext(os.path.join(dirName,fname))
    if fileExtension == '.txt':
        for line in open(os.path.join(dirName,fname)):
            token = tokenize(line) 
            tokenized.append(tokens2Index(token, modelLoad));
            
np.save('tokenized', np.array(tokenized))