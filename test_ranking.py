from unittest import TestCase
import ranking


class Testranking(TestCase):
    def test_no_match_tilte_no_match_doc(self):
        self.assertEqual(0, ranking.final("Yummy Food", "American cuisine is very diverse",
                                          "When tourist come to American, there is a lot of choice that they can choose"))

    def test_individual_match_tilte_individual_match_doc(self):
        self.assertEqual(9, ranking.final("Yummy Food", "Food in America is yummy",
                                          "Food in American is very yummy. The food come from around the world"))

    def test_pair_of_words_match_tilte_pair_of_words_match_doc(self):
        self.assertEqual(13, ranking.final("Yummy Food", "Yummy Food in America",
                                           "Yummy food in American is everywhere. The food come from around the world"))

    def test_match_tilte_individual_only_no_match_doc(self):
        self.assertEqual(6, ranking.final("Yummy Food", "Food in America is yummy", "I don't know what to say."))

    def test_match_tilte_pair_of_words_only_no_match_doc(self):
        self.assertEqual(8, ranking.final("Yummy Food", "Yummy Food in America", "I don't know what to say."))

    def test_no_match_tilte_match_doc_individual_only(self):
        self.assertEqual(3, ranking.final("Yummy Food", "American cuisine is very diverse",
                                          "Food in American is very yummy. The food come from around the world"))

    def test_no_match_tilte_pair_of_words_match_doc(self):
        self.assertEqual(4, ranking.final("Yummy Food", "American cuisine is very diverse",
                                          "Yummy food in American is everywhere. They come from around the world"))
