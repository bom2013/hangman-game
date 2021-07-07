import unittest
import hanggame


class TestHangGame(unittest.TestCase):

    def test_check_is_win(self):
        check_is_win = hanggame.check_is_win
        # Check empty word
        self.assertTrue(check_is_win("", []))
        self.assertTrue(check_is_win("", ['a', 'b']))
        # Check all words contain in list in word but not enough
        self.assertFalse(check_is_win('world', ['o', 'l']))
        self.assertFalse(check_is_win('world', []))
        # Check all words contain in list in word + other word
        self.assertTrue(check_is_win('world', ['o', 'w', 'r', 'd', 'l', 'c']))
        # Check normal
        self.assertTrue(check_is_win('world', ['o', 'w', 'r', 'd', 'l']))

    def test_create_printable_mask(self):
        create_printable_mask = hanggame.create_printable_mask_list
        # Check no letters in word\list
        self.assertEqual(create_printable_mask("world", []), [None]*5)
        self.assertEqual(create_printable_mask("", ['w', 'a']), [])
        # Check full mask
        self.assertEqual(create_printable_mask(
            "world", ['w', 'l', 'r', 'o', 'd']), ['w', 'o', 'r', 'l', 'd'])
        # Assert double letters
        self.assertEqual(create_printable_mask("Hello", ['l', 'a']), [None, None, 'l', 'l', None])
        

if __name__ == '__main__':
    unittest.main()
