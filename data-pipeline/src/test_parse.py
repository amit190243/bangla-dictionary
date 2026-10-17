
import unittest

from parse_test import parse_json_list


class TestParseJsonList(unittest.TestCase):

    def test_valid_json_array(self):
        self.assertEqual(
            parse_json_list('["one", "two"]'),
            ["one", "two"],
        )

    def test_empty_value(self):
        self.assertEqual(parse_json_list(""), [])

    def test_malformed_json(self):
        self.assertEqual(parse_json_list('["one",'), [])

    def test_non_array_json(self):
        self.assertEqual(parse_json_list('"one"'), [])

    def test_empty_items_are_removed(self):
        self.assertEqual(
            parse_json_list('["one", "", "  ", "two"]'),
            ["one", "two"],
        )


if __name__ == "__main__":
    unittest.main()
