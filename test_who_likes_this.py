# -*- coding:utf-8 -*-
import unittest
import who_likes_this

class TestWhoLikesThis(unittest.TestCase):
    def test(self):
        self.assertEqual(who_likes_this.likes([]), 'no one likes this')
        self.assertEqual(who_likes_this.likes(['Peter']), 'Peter likes this')
        self.assertEqual(who_likes_this.likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
        self.assertEqual(who_likes_this.likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
        self.assertEqual(who_likes_this.likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')
