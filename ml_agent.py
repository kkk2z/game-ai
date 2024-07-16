import numpy as np
import random

class CombatEnv:
    def __init__(self):
        self.state_space = 2  # 例えば、攻撃力と健康状態
        self.action_space = 2  # 攻撃するか回避するか

    def reset(self):
        self.state = np.array([100, 100])  # 戦闘開始時の状態
        return self.state

    def step(self, action):
        if action == 0:  # 攻撃
            reward = random.randint(0, 10)  # ダメージに基づく報酬
            self.state[1] -= reward
        else:  # 回避
            reward = 0
        done = self.state[1] <= 0
        return self.state, reward, done

class QLearningAgent:
    def __init__(self, action_space):
        self.q_table = np.zeros((100, action_space))  # 状態数とアクション数
        self.learning_rate = 0.1
        self.discount_factor = 0.9
        self.exploration_rate = 1.0
        self.exploration_decay = 0.995

    def choose_action(self, state):
        if np.random.rand() < self.exploration_rate:
            return np.random.choice([0, 1])
        else:
            return np.argmax(self.q_table[state])

    def update_q_table(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.q_table[next_state])
        td_target = reward + self.discount_factor * self.q_table[next_state][best_next_action]
        td_error = td_target - self.q_table[state][action]
        self.q_table[state][action] += self.learning_rate * td_error

        self.exploration_rate *= self.exploration_decay
