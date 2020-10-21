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
        
      