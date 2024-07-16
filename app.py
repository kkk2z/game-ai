from flask import Flask, render_template, jsonify
from combat_simulation import generate_random_combatant, battle
from ml_agent import CombatEnv, QLearningAgent

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/battle')
def battle_endpoint():
    fighter1 = generate_random_combatant()
    fighter2 = generate_random_combatant()
    
    battle_log = []
    def log_action(action, damage, state):
        battle_log.append(f"{action}: {state} ダメージ {damage}")
    
    def battle(fighter1, fighter2):
        while fighter1.is_alive() and fighter2.is_alive():
            damage = fighter1.attack(fighter2)
            log_action(f"{fighter1.name}の攻撃", damage, f"{fighter2.name}の健康: {fighter2.health}")
            if not fighter2.is_alive():
                return fighter1.name

            damage = fighter2.attack(fighter1)
            log_action(f"{fighter2.name}の攻撃", damage, f"{fighter1.name}の健康: {fighter1.health}")
            if not fighter1.is_alive():
                return fighter2.name

    winner = battle(fighter1, fighter2)
    result = {
        'fighter1': {
            'name': fighter1.name,
            'health': fighter1.health,
            'attack_power': fighter1.attack_power,
            'defense': fighter1.defense
        },
        'fighter2': {
            'name': fighter2.name,
            'health': fighter2.health,
            'attack_power': fighter2.attack_power,
            'defense': fighter2.defense
        },
        'winner': winner,
        'battle_log': battle_log
    }
    return jsonify(result)

@app.route('/train')
def train_endpoint():
    env = CombatEnv()
    agent = QLearningAgent(action_space=2)
    
    for episode in range(1000):
        state = env.reset()
        done = False
        while not done:
            action = agent.choose_action(int(state[0]))
            next_state, reward, done = env.step(action)
            agent.update_q_table(int(state[0]), action, reward, int(next_state[0]))
            state = next_state

    return "Training complete!"

if __name__ == '__main__':
    app.run(debug=True)
    from flask import Flask, render_template, jsonify
from models import db, CombatLog
from combat_simulation import generate_random_combatant, battle
from ml_agent import CombatEnv, QLearningAgent

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///combat_simulation.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

# 残りのエンドポイントは省略
@app.route('/battle')
def battle_endpoint():
    fighter1 = generate_random_combatant()
    fighter2 = generate_random_combatant()
    
    battle_log = []
    def log_action(action, damage, state):
        battle_log.append(f"{action}: {state} ダメージ {damage}")
    
    def battle(fighter1, fighter2):
        while fighter1.is_alive() and fighter2.is_alive():
            damage = fighter1.attack(fighter2)
            log_action(f"{fighter1.name}の攻撃", damage, f"{fighter2.name}の健康: {fighter2.health}")
            if not fighter2.is_alive():
                return fighter1.name

            damage = fighter2.attack(fighter1)
            log_action(f"{fighter2.name}の攻撃", damage, f"{fighter1.name}の健康: {fighter1.health}")
            if not fighter1.is_alive():
                return fighter2.name

    winner = battle(fighter1, fighter2)
    result = {
        'fighter1': {
            'name': fighter1.name,
            'health': fighter1.health,
            'attack_power': fighter1.attack_power,
            'defense': fighter1.defense
        },
        'fighter2': {
            'name': fighter2.name,
            'health': fighter2.health,
            'attack_power': fighter2.attack_power,
            'defense': fighter2.defense
        },
        'winner': winner,
        'battle_log': battle_log
    }

    # データベースに保存
    log_entry = CombatLog(
        fighter1_name=fighter1.name,
        fighter1_health=fighter1.health,
        fighter1_attack_power=fighter1.attack_power,
        fighter1_defense=fighter1.defense,
        fighter2_name=fighter2.name,
        fighter2_health=fighter2.health,
        fighter2_attack_power=fighter2.attack_power,
        fighter2_defense=fighter2.defense,
        winner_name=winner,
        battle_log='\n'.join(battle_log)
    )
    db.session.add(log_entry)
    db.session.commit()

    return jsonify(result)
    @app.route('/history')
def history_endpoint():
    logs = CombatLog.query.all()
    history = [{
        'fighter1_name': log.fighter1_name,
        'fighter1_health': log.fighter1_health,
        'fighter1_attack_power': log.fighter1_attack_power,
        'fighter1_defense': log.fighter1_defense,
        'fighter2_name': log.fighter2_name,
        'fighter2_health': log.fighter2_health,
        'fighter2_attack_power': log.fighter2_attack_power,
        'fighter2_defense': log.fighter2_defense,
        'winner_name': log.winner_name,
        'battle_log': log.battle_log
    } for log in logs]
    return jsonify(history)