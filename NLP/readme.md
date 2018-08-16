# Natural Language Processing
This repositiory contains code regarding machine learning and feature extraction techniques used in NLP. The repository contains the following codes
- Sentimental analysis

## Sentimental Analysis
Sentimental analysis is one of the oldest problems tackled when the field of NLP was introduced. With the passage of time advance technqiues are developed to extract features and improve the acurracy of sentimental analysis.

The program performs the sentimental analysis on benchmark dataset of [IMDB movie reviews dataset](http://ai.stanford.edu/~amaas/data/sentiment/).

To perfrom sentimental analysis, we first need to perform some data processing tasks.

### Data Processing

The raw data needs processing to be brought into standardized format before feeding it into any type of neural network. The data processing tasks performed are as follows
- Tokenization of words
- Removal of stopwards

The processed data is than fed into **word2Vec generator**. Word2Vec convert words in text into vectors which makes it easy to group together similar words. This is the standard representation which is used as input of neural networks, these neural networks than perform specialized tasks to extract information from the vectors. There are many hyperparamters used in the coversion and in the code different recommended combinations of hyperparameters were used and the best one was picked up using interinsic testing.

To perform the data processing we need to download the data and copy the training data into one file. To ease up the process the bash file is created and attched we need to copy files from different folder into single folder and that folder should be provided in the code to tokenize the data and convert words into vectors.
```
chmod u+r ./copy_reviews.sh # assign appropirate writes to run batch file
./copy_reviews.sh train/neg/ train/pos/ train-corpus
```
**NOTE: The code in preprocessing.ipby expects that there is a word2Vec folder created at same level as file to save the word2Vec model created. The folder name could be changed inside code**

### Intrinsic Testing


