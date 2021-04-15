import unittest

from enchantx import XDict


class XDictTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.spellchecker = XDict("GoogleNews-vectors-negative300.bin")

    def test_suggest(self):
        self.assertIsInstance(self.spellchecker.suggest("joket"), list)

    def test_smart_suggest(self):
        self.assertIsInstance(self.spellchecker.smart_suggest("joket", "clown"), list)

    def test_smart_suggest_with_scores(self):
        self.assertIsInstance(self.spellchecker.smart_suggest_with_scores("joket", "clown"), dict)


if __name__ == '__main__':
    unittest.main()
