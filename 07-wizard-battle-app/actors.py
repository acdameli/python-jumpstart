from random import randint


class Killable:
    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)

    def hit(self, amount):
        self.hp = min(self.hp - amount, 0)

    def is_alive(self):
        return self.hp > 0


class Creature(Killable):
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.max_hp = randint(level, level * 10)
        self.hp = self.max_hp

    def __repr__(self):
        return f'A level {self.level} {self.name}'

    def attack(self, other):
        other.hit(randint(1, self.level * 2))


class Player(Creature):
    def level_up(self):
        self.level += 1
        self.heal(self.max_hp)
