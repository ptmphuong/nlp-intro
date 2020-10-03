import pickle
import nltk
import random

#get training data
documents_f = open("pickled/documents.pickle", "rb")
documents = pickle.load(documents_f)
documents_f.close()

#check frequencies
word_features5k_f = open("pickled/word_features.pickle", "rb")
word_features = pickle.load(word_features5k_f)
word_features5k_f.close()


def find_features(document):
    words = nltk.word_tokenize(document)
    features = {}
    for word in word_features:
        features[word] = (word in words) 
    
    return features

featuresets = [(find_features(rev), category) for (rev,category) in documents]
random.shuffle(featuresets)

#positive data example
training_set = featuresets[:8530]
testing_set = featuresets[8530:]

classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Original Naive Bayes Algo accuracy: ", (nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)

def sentiment(text):
    feats = find_features(text)
    return classifier.classify(feats)

print(sentiment("It was awesome!"))