class Author:
    
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography
        
    def author_name(self):
        return self.name
    
    def author_biography(self):
        return self.biography
    
    def __str__(self):
        return f"Author: {self.name}, Biography: {self.biography}"
    
    def __repr__(self):
        return str(self)
    