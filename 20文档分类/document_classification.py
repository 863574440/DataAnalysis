import os
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

STOP_WORDS_PATH = "./text classification/stop/stopword.txt"
TRAIN_DATA_PATH = "./text classification/train"
TEST_DATA_PATH = "./text classification/test"


def load_stop_words(file_path):
    file = open(file_path, "r", encoding="utf-8")
    stop_words = [line.strip().encode("utf-8").decode("utf-8") for line in file.readlines()]
    return stop_words


class Data:
    def __init__(self, path):
        self.path = path

    def load_documents(self, document_type):
        contents = []
        labels = []
        path = self.path + "/" + document_type
        files_name = os.listdir(path)
        for file in files_name:
            file_path = path + "/" + file
            content = open(file_path, "r", encoding="ANSI")
            line = content.readline().strip().encode("utf-8").decode("utf-8")
            contents.append(line)
            labels.append(" ".join(jieba.cut(document_type)))
            content.close()
        return contents, labels


def train_model(stop_words):
    train_data_list = []
    train_labels = []

    train_data = Data(TRAIN_DATA_PATH)
    sport_contents, sport_labels = train_data.load_documents("体育")
    female_contents, female_labels = train_data.load_documents("女性")
    literature_contents, literature_labels = train_data.load_documents("文学")
    school_contents, school_labels = train_data.load_documents("校园")

    train_data_list.extend(sport_contents)
    train_data_list.extend(female_contents)
    train_data_list.extend(literature_contents)
    train_data_list.extend(school_contents)

    train_labels.extend(sport_labels)
    train_labels.extend(female_labels)
    train_labels.extend(literature_labels)
    train_labels.extend(school_labels)

    tfidf = TfidfVectorizer(stop_words=stop_words, max_df=0.5)
    train_features = tfidf.fit_transform(train_data_list)

    clf = MultinomialNB(alpha=0.001)
    clf.fit(train_features, train_labels)

    return clf, tfidf.vocabulary_


def predict_model(clf, stop_words, train_vocabulary):
    test_data_list = []
    test_labels = []

    test_data = Data(TEST_DATA_PATH)
    sport_contents, sport_labels = test_data.load_documents("体育")
    female_contents, female_labels = test_data.load_documents("女性")
    literature_contents, literature_labels = test_data.load_documents("文学")
    school_contents, school_labels = test_data.load_documents("校园")

    test_data_list.extend(sport_contents)
    test_data_list.extend(female_contents)
    test_data_list.extend(literature_contents)
    test_data_list.extend(school_contents)

    test_labels.extend(sport_labels)
    test_labels.extend(female_labels)
    test_labels.extend(literature_labels)
    test_labels.extend(school_labels)

    test_tdidf = TfidfVectorizer(stop_words=stop_words, max_df=0.5, vocabulary=train_vocabulary)
    test_features = test_tdidf.fit_transform(test_data_list)

    predicted_labels = clf.predict(test_features.toarray())
    score = metrics.accuracy_score(test_labels, predicted_labels)
    print(score)

    print(test_labels)
    print(list(predicted_labels))


def main():
    stop_words = load_stop_words(STOP_WORDS_PATH)
    clf, train_vocabulary = train_model(stop_words)
    predict_model(clf, stop_words, train_vocabulary)


if __name__ == '__main__':
    main()
