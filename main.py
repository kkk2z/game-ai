from combat_simulation import Combatant, battle
from ml_agent import CombatEnv, QLearningAgent

# 戦闘シミュレーションの例
def run_combat_simulation():
    fighter1 = Combatant("戦士", 100, 20)
    fighter2 = Combatant("魔法使い", 80, 25)
    winner = battle(fighter1, fighter2)
    print(f"戦闘の勝者は{winner}です。")

# 機械学習エージェントのトレーニング
def train_ml_agent():
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

if __name__ == "__main__":
    # 戦闘シミュレーションの実行
    run_combat_simulation()
    
    # 機械学習エージェントのトレーニング
    train_ml_agent()
