import numpy as np

from enchant import Dict
from enchantx.vectorizer import WORD2VEC


class XDict:
    """
    Extended Dictionary object for the Enchant spellchecker.
    This class internally creates the Dict object from the pyenchant
    package to support basic and legacy functions.

    This class mainly extends the functionality of naive suggestions
    of correct spellings for misspelled words to smart suggestions
    using words vectors.

    Dictionary objects are responsible for checking the spelling of words
    and suggesting possible corrections.  Each dictionary is owned by a
    Broker object, but unless a new Broker has explicitly been created
    then this will be the 'enchant' module default Broker and is of little
    interest.

    The important methods of this class include:

        * check():              check whether a word id spelled correctly
        * suggest():            suggest correct spellings for a word
        * add():                add a word to the user's personal dictionary
        * remove():             add a word to the user's personal exclude list
        * add_to_session():     add a word to the current spellcheck session
        * store_replacement():  indicate a replacement for a given word

        * smart_suggest():      suggest most relevant correct spellings for a word
        * smart_suggest_with_scores(): suggest most relevant correct spellings for a word with probabilities

    Information about the dictionary is available using the following
    attributes:
        * model_path  path of pretrained model ("GoogleNews-vectors-negative300.bin")
        * tag:        the language tag of the dictionary
        * provider:   a ProviderDesc object for the dictionary provider

    """
    def __init__(self, model_path=None, tag=None, broker=None):
        """XDict object constructor.

        XDict requires pretrained model "GoogleNews-vectors-negative300.bin"
        in order to give smart suggestions for misspelled words.

        It is recommended to give model path while creating XDict object.
        Otherwise XDict will try to search the model at following locations:
        1) /home/$USER/.enchantx/GoogleNews-vectors-negative300.bin
        2) In current working directory

        A dictionary belongs to a specific language, identified by the
        string <tag>.  If the tag is not given or is None, an attempt to
        determine the language currently in use is made using the 'locale'
        module.  If the current language cannot be determined, Error is raised.

        If <tag> is instead given the value of False, a 'dead' Dict object
        is created without any reference to a language.  This is typically
        only useful within PyEnchant itself.  Any other non-string value
        for <tag> raises Error.

        Each dictionary must also have an associated Broker object which
        obtains the dictionary information from the underlying system. This
        may be specified using <broker>.  If not given, the default broker
        is used.
        """
        self.enchant_obj = Dict(tag=tag, broker=broker)
        self.enchantX = WORD2VEC(model_path)

    def check(self, word) -> bool:
        """Check spelling of a word.

        This method takes a word in the dictionary language and returns
        True if it is correctly spelled, and false otherwise.
        """
        return self.enchant_obj.check(word)

    def suggest(self, word) -> list:
        """Suggest possible spellings for a word.

        This method tries to guess the correct spelling for a given
        word, returning the possibilities in a list.
        """
        return self.enchant_obj.suggest(word)

    def add(self, word) -> None:
        """Add a word to the user's personal word list"""
        self.enchant_obj.add(word)

    def remove(self, word) -> None:
        """Add a word to the user's personal exclude list."""
        self.enchant_obj.remove(word)

    def add_to_session(self, word) -> None:
        """Add a word to the session personal list."""
        self.enchant_obj.add_to_session(word)

    def store_replacement(self, mis, cor) -> None:
        """Store a replacement spelling for a miss-spelled word.

        This method makes a suggestion to the spellchecking engine that the
        miss-spelled word <mis> is in fact correctly spelled as <cor>.  Such
        a suggestion will typically mean that <cor> appears early in the
        list of suggested spellings offered for later instances of <mis>.
        """
        self.enchant_obj.store_replacement(mis,cor)

    def is_added(self, word):
        """Check whether a word is in the personal word list."""
        return self.enchant_obj.is_added(word)

    def is_removed(self, word):
        """Check whether a word is in the personal exclude list."""
        return self.enchant_obj.is_removed(word)

    def smart_suggest(self, word: str, next_word: str) -> list:
        """
        Suggest most relevant correct spellings for a word based on
        given next word. If the word is the last of sentence/text then
        provide previous word in next_word parameter
        :param word: misspelled word
        :param next_word: next / previous word of current misspelled word
        :return: list with suggestions
        """

        if self.check(word):
            return []
        if not next_word:
            return []
        suggested_words = self.suggest(word)
        if len(suggested_words) > 0:
            distances = self.enchantX.calculate_distances(next_word, suggested_words)

            if distances.size == 0:
                return suggested_words
            else:
                words_with_score = dict()
                for word, dist in zip(suggested_words, list(distances)):
                    words_with_score[word] = dist
                return sorted(words_with_score, key=words_with_score.get)

        else:
            return []

    def smart_suggest_with_scores(self, word: str, next_word: str) -> dict:
        """
        Suggest most relevant correct spellings with probabilites for a word
        based on given next word.
        :param word: misspelled word
        :param next_word: next / previous word of current misspelled word
        :return: dict with suggestions and scores (probabilities)
        """

        if self.check(word):
            return {}

        suggested_words = self.suggest(word)
        if len(suggested_words) > 0:
            distances = self.enchantX.calculate_distances(next_word, suggested_words)

            if distances.size == 0:
                return {}
            else:
                words_with_score = dict()
                for word, dist in zip(suggested_words, list(distances)):
                    if not np.isnan(dist):
                        words_with_score[word] = dist

                suggestions = dict()
                for word, dist in sorted(words_with_score.items(), key=lambda tup: tup[1]):
                    suggestions[word] = int(round(1 - dist, 2)*100)
                return suggestions

        else:
            return {}