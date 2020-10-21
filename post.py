class Post:
    def __init__(self, title, fecha, hora, content):
      self.title = title
      self.fecha = fecha
      self.hora = hora
      self.content = content
    
    def create_post(self):
      return {'title': self.title, 'fecha': self.fecha, 'hora':self.hora, 'content': self.content, }
    
    def json(self):
      return{'title': self.title, 'content': self.content, }
      