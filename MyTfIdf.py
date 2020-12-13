import re
from typing import List
from collections import Counter
import math


class MyCountVectorizer:
    """
    My CountVectorizer MVP
    """

    def __init__(self):
        self._prepared_corpus = []
        self._bag_of_words = {}
        self._count_matrix = []

    def get_feature_names(self):
        """
        Returns a list of feature names.
        """
        return list(self._bag_of_words.keys())

    def _corpus_preprocessing(self, corpus: List[str]):
        """
        Input text preprocessing
        """
        for index in range(len(corpus)):
            corpus[index] = corpus[index].lower()
            corpus[index] = corpus[index].strip()
            corpus[index] = re.sub(r" +", " ", corpus[index])
            corpus[index] = re.sub(r"[^A-za-zА-Яа-я- ]+", "", corpus[index])

        self._prepared_corpus = corpus

    def _tokenize_corpus(self):
        """
        Corpus tokenization
        """
        for string in self._prepared_corpus:
            self._bag_of_words.update(dict.fromkeys(string.split()))

    def _get_matrix(self):
        """
        Returns result matrix as list of lists
        """
        for string in self._prepared_corpus:
            counted_words = Counter(string.split())
            self._count_matrix.append(
                [counted_words[word] for word in self._bag_of_words]
            )

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        """
        Learn the vocabulary dictionary and return document-term matrix.

        Parameters:
        -----------

        corpus: list
            Raw document as a list of sentenses
        """
        self._corpus_preprocessing(corpus)
        self._tokenize_corpus()
        self._get_matrix()
        return self._count_matrix


class TfidfTransformer:
    """
    pass
    """

    @staticmethod
    def _tf_transform(matrix):
        """
        TF transformer
        """
        tf_matrix = []
        for line in matrix:
            total = sum(line)
            tf_matrix.append([round(value / total, 3) for value in line])

        return tf_matrix

    @staticmethod
    def _idf_transform(matrix):
        """
        IDF transformer
        """
        docs_cnt = len(matrix)
        idf_len = len(matrix[0])
        idf_matrix = [0] * idf_len

        for index in range(idf_len):
            for text in matrix:
                if text[index] > 0:
                    idf_matrix[index] += 1

        idf_matrix = [
            round(math.log((docs_cnt + 1) / (x + 1)) + 1, 3) for x in idf_matrix
        ]

        return idf_matrix

    @staticmethod
    def _tfidf_transform(tf_matrix, idf_matrix):
        """
        TFIDF transformer
        """
        tfidf_matrix = []
        for line in tf_matrix:
            tfidf_matrix.append(
                [round(line[i] * idf_matrix[i], 3) for i in range(len(idf_matrix))]
            )

        return tfidf_matrix

    def fit_transform(self, matrix):
        """
        fit_transform method
        """
        return self._tfidf_transform(
            self._tf_transform(matrix), self._idf_transform(matrix)
        )


class TfidfVectorizer(MyCountVectorizer):
    """
    My TfidfVectorizer class
    """

    def __init__(self):
        super().__init__()
        self.transformer = TfidfTransformer()

    def fit_transform(self, corpus):
        count_matrix = super().fit_transform(corpus)
        return self.transformer.fit_transform(count_matrix)


if __name__ == "__main__":
    corpus = [
        "  Crock Pot Pa@@sta Never boil       pasta again",
        "Pasta Pomodoro Fresh   213 ingredients Parmesan to taste",
    ]

    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(matrix)
