from app import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String)
    team = db.Column(db.String)
    position = db.Column(db.String)
    age = db.Column(db.Integer)
    games_played = db.Column(db.Integer)
    minutes_per_game = db.Column(db.Float)
    ft_attempts = db.Column(db.Integer)
    ft_percentage = db.Column(db.Float)
    tp_attempts = db.Column(db.Integer)
    tp_percentage = db.Column(db.Float)
    th_attempts = db.Column(db.Integer)
    th_percentage = db.Column(db.Float)
    points_per_game = db.Column(db.Float)
    rebounds_per_game = db.Column(db.Float)
    assists_per_game = db.Column(db.Float)
    steals_per_game = db.Column(db.Float)
    blocks_per_game = db.Column(db.Float)
    turnovers_per_game = db.Column(db.Float)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self) -> str:
        return f'{self.name} ({self.position})' 