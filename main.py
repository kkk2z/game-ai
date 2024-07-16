from combat_simulation import Combatant, battle, generate_random_combatant

def run_combat_simulation():
    fighter1 = generate_random_combatant()
    fighter2 = generate_random_combatant()
    print(f"戦士1: {fighter1.name}, 健康: {fighter1.health}, 攻撃力: {fighter1.attack_power}, 防御力: {fighter1.defense}")
    print(f"戦士2: {fighter2.name}, 健康: {fighter2.health}, 攻撃力: {fighter2.attack_power}, 防御力: {fighter2.defense}")
    winner = battle(fighter1, fighter2)
    print(f"戦闘の勝者は{winner}です。")

if __name__ == "__main__":
    run_combat_simulation()