def battle_score(health, attack, reward):
    score=  reward+(health/10)- attack
    return int(score)

def find_monster(monsters, name):
    for monster in monsters:
        if monster[0] == name:
            return monster

    return None