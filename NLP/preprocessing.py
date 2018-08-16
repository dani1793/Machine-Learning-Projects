from pprint import pprint  # pretty-printer
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import gensim;
import os;
import nltk.data;
import time;


# path where the combined folder is present
TRAIN_DIR_PATH ='./train-corpus';

class Text(object):
    def __init__(self,dirname):
        self.dirname = dirname;
        self.readFiles = 0;
        self.allFiles = len([name for name in os.listdir(self.dirname)])

    def __iter__(self):
        for fname in os.listdir(self.dirname):
             # if self.readFiles % 500 == 0:
            self.readFiles += 1
            print('learning model: %d/ %d'%(self.readFiles,self.allFiles*6), end="\r" )
            filename, fileExtension = os.path.splitext(os.path.join(self.dirname,fname))
            if fileExtension == '.txt':
                for line in open(os.path.join(self.dirname,fname)):
                    token = self.tokenize(line) 
                    yield token

    # The method does the following in order
    # 1- It convert the copra paragraph into array of sentences using punkt tokenizer
    # 2- It then tokenize each line in paragraph into words and remove the stop words and the special characters
    def tokenize(self,line):
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

def createAndSaveModel(sg=1, size= 100, mincount= 5, window= 5,
corpusPath= TRAIN_DIR_PATH, saveFilePath = './wordToVec/modelTemp'):
    sentence = Text(corpusPath);
    model = gensim.models.Word2Vec(sentence, sg=sg,size= size,
    min_count=mincount, window =window, workers=4);
    pprint('saving data');
    model.save(saveFilePath);

def recordElapsedTime(str):
    file = open('TimeForModel-test.txt ','a') 
    file.writelines(str)  
    file.close() 
    
# different word2Vec configurations tested for data
models = {
    'modelOne': {
        'sg': 1, 
        'size': 600, 
        'mincount': 5, 
        'window': 10,
        'saveFilePath': './wordToVec/model-sg-1-size-600-window-10'
    },
        'modelTwo': {
        'sg': 1, 
        'size': 100, 
        'mincount': 5, 
        'window': 5,
        'saveFilePath': './wordToVec/model-sg-1-size-100'
    },
        'modelThree': {
        'sg': 2, 
        'size': 100, 
        'mincount': 5, 
        'window': 5,
        'saveFilePath': './wordToVec/model-sg-2-size-100'
    },
        'modelFour': {
        'sg': 1, 
        'size': 100, 
        'mincount': 10, 
        'window': 5,
        'saveFilePath': './wordToVec/model-sg-1-size-100-mincount-10'
    },
        'modelFive': {
        'sg': 1, 
        'size': 200, 
        'mincount': 10, 
        'window': 5,
        'saveFilePath': './wordToVec/model-sg-1-size-200-mincount-10'
    },
        'modelSix': {
        'sg': 1, 
        'size': 200, 
        'mincount': 5, 
        'window': 5,
        'saveFilePath': './wordToVec/model-sg-1-size-200-mincount-50'
    },
    
}

# Model selected for testing
SELECTED_MODEL = 'modelOne'
        
start = time.clock(); 
# Tokenize the reviews and feed it to word2Vec. The model created by word2Vec is saved.
createAndSaveModel(sg=models[SELECTED_MODEL]['sg'],size=models[SELECTED_MODEL]['size'], window = models[SELECTED_MODEL]['window'], 
                   saveFilePath =models[SELECTED_MODEL]['saveFilePath']);   
end = time.clock() ;
elapsed = end - start;
recordElapsedTime('Time spent in %s is: %f \n'% (SELECTED_MODEL, elapsed));