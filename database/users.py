class User(db.Model):
  
  table_name = "user_list"
  
  uid = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(100), unique=True, nullable=False)
  pass_hash = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '' % self.username
