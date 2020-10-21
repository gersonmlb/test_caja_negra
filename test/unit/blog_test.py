from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Nico Content', 'Nico')
        
        self.assertEqual('Nico Content',b.title)
        self.assertEqual('Nico', b.author)
        self.assertEqual([], b.posts)
    
    def test_repr(self):
        b = Blog('Test', 'Nico Author')
        b1 = Blog('My Day', 'Nico')

        self.assertEqual(b.__repr__(), 'Test By Nico Author (0 posts)')
        self.assertEqual(b1.__repr__(), 'My Day By Nico (0 posts)')
    
    def test_repr_multiple_posts(self):
        b = Blog('Test', 'Nico Author')
        b.posts = ['test']
        
        b1 = Blog('My Day', 'Nico')
        b1.posts = ['test', 'another']
        
        self.assertEqual(b.__repr__(), 'Test By Nico Author (1 post)')
        self.assertEqual(b1.__repr__(), 'My Day By Nico (2 posts)')
    
    def test_read(self):
        r = Blog('', 'FF')
        r1 = Blog('', 'Nico')
        
        self.assertEqual(r.__read__(), 'The author dont exist')
        self.assertEqual(r1.__read__(), 'Nico By 5 posts')
        