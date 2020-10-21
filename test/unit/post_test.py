from unittest import TestCase
from post import Post

class PostTest(TestCase):
    def test_post(self):
        p = Post('Nico', '10/10/20', '02:40 PM', 'Nico Content')
        self.assertEqual('Nico',p.title)
        self.assertEqual('Nico Content', p.content)
    
    def test_create_post(self):
        cp = Post('Post Nico', '10/10/20', '02:40 PM', 'Nico Content')
        test = {'title':'Post Nico', 'fecha':'10/10/20', 'hora':'02:40 PM', 'content': 'Nico Content'}
        self.assertDictEqual(test, cp.create_post())
        
    def test_json(self):
        p = Post('Nico', '10/10/20', '02:40 PM', 'Nico Content')
        expected = {'title': 'Nico', 'content':'Nico Content'}
        self.assertDictEqual(expected, p.json())