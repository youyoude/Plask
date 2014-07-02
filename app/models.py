from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50), index=True, unique=True)
	password = db.Column(db.String(16))
	mail = db.Column(db.String(50))
	isAdmin = db.Column(db.Boolean)
	isClosed = db.Column(db.Boolean)

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)

	def __repr__(self):
		return '<User %r>' % (self.username)