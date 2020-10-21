class Blog:
    def __init__(self, title, author):
      self.title = title
      self.author = author
      self.posts = []
    
    def __repr__(self):
        #return 'Test writer By Nico (0 post)'
        return '{} By {} ({} {})'.format(self.title, self.author, 
                                         len(self.posts), 
                                         'posts' if len(self.posts) != 1 else 'post')
    
    def read_author(self):
      #title, author, posts
      authors = ['Test', 'Nico', 'FM', 'AM']
      posts = ['3 posts', '5 posts', '4 posts', '8 posts']
      
      if self.author in authors:
        longitud = authors.index(self.author)
        return '{} By {}'.format(self.author, posts[longitud])
      
      else:
        return 'The author dont exist'
      
        
      