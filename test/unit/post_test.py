from unittest import TestCase
from post import Post

class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Nico', 'Nico Content')
        self.assertEqual('Nico',p.title)
        self.assertEqual('Nico Content', p.content)
    
    def test_json(self):
        p = Post('Nico', 'Nico Content')
        expected = {'title': 'Nico', 'content':'Nico Content'}
        self.assertDictEqual(expected, p.json())