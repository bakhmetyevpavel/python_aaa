import re
from typing import List
from collections import Counter


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


if __name__ == "__main__":
    corpus = [
        "  Crock Pot Pa@@sta Never boil       pasta again",
        "Pasta Pomodoro Fresh   213 ingredients Parmesan to taste",
    ]

    vectorizer = MyCountVectorizer()
    matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(matrix)
