import unittest

from counting_words import count_words


class CountingWordsTest(unittest.TestCase):
    def test_count_words_empty_dict(self):
        self.assertEqual(count_words([]), {})

    def test_count_words_word_only_once(self):
        self.assertEqual(count_words(["apple", "banana", "pear"]), {"apple": 1, "banana": 1, "pear": 1})

    def test_count_words_word_more_times(self):
        self.assertEqual(count_words(["apple", "apple", "pear"]), {"apple": 2,"pear": 1})

    def test_count_words_one_word(self):
        self.assertEqual(count_words(["apple"]), {"apple": 1})

    def test_count_words_empty_string(self):
        self.assertEqual(count_words([" "]), {" ": 1})

if __name__ == "__main__":
    unittest.main()
