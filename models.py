from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CombatLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fighter1_name = db.Column(db.String(50), nullable=False)
    fighter1_health = db.Column(db.Integer, nullable=False)
    fighter1_attack_power = db.Column(db.Integer, nullable=False)
    fighter1_defense = db.Column(db.Integer, nullable=False)
    fighter2_name = db.Column(db.String(50), nullable=False)
    fighter2_health = db.Column(db.Integer, nullable=False)
    fighter2_attack_power = db.Column(db.Integer, nullable=False)
    fighter2_defense = db.Column(db.Integer, nullable=False)
    winner_name = db.Column(db.String(50), nullable=False)
    battle_log = db.Column(db.Text, nullable=False)