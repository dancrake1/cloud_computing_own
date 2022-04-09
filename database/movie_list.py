from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class movie_list(db.model):
  
  listname = "movie_list"
  
  l_id = db.Column(db.Integer, 
                 primary_key=True)
  
  username_reviewer = db.Column(db.String(100), 
                                unique=True, 
                                nullable=False)
  
  movie_name = db.Column(db.String(100), 
                         nullable=False)
  
  director = db.Column(db.String(100), 
                       nullable=False)
  
  year = db.Column(db.int(4), 
                   nullable=False)
  
  score = db.Column(db.float(),
                    nullable=True)
  
  def __repr__(self):
        return '' % self.id
