import logging
import numpy as np

from gensim.models import KeyedVectors
from six import string_types


logging.basicConfig(filename="vectorizer.log")
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.WARNING)


_WORD2VEC = KeyedVectors.load_word2vec_format("GoogleNews-vectors-negative300.bin", binary=True)


class WORD2VEC:

    def __init__(self, path_to_model=None):
        self.word2vec = _WORD2VEC


    def calculate_distances(self, word_or_vector, other_words) -> np.array:
        if isinstance(word_or_vector, string_types):
            try:
                input_vector = self.word2vec[word_or_vector]
            except KeyError as exp:
                logger.warning(exp)
                return np.asarray([])
        else:
            input_vector = word_or_vector
        if not other_words:
            return np.asarray([])
        else:
            other_vectors = []
            for word in other_words:
                try:
                    other_vectors += [self.word2vec[word]]
                except KeyError as exp:
                    logger.warning(exp)
                    other_vectors += [np.zeros((300,))]

            other_vectors = np.asarray(other_vectors)
            return 1 - self.word2vec.cosine_similarities(input_vector, other_vectors)
