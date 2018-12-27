from random import choice
from actors import Player
from actors import Creature

def main():
     print_header()
     game_loop()


def print_header():
    print()
    print('--------------------------------------------------------------------------------')
    print('''
       (  )   /\   _                 (
        \ |  (  \ ( \.(               )                      _____
      \  \ \  `  `   ) \             (  ___                 / _   \\
     (_`    \+   . x  ( .\            \/   \____-----------/ (o)   \_
    - .-               \+  ;          (  O                           \____
         WIZARD BATTLE        )        \_____________  `              \  /
    (__       APP      +- .( -'.- <. - _  VVVVVVV VV V\                 \/
    (_____            ._._: <_ - <- _  (---\_AAAAAAA__A_/               |
      .    /./.+-  . .- /  +--  - .     \______________//_              \_______
      (__ ' /x  / x _/ (                                  \___'          \     /
     , x / ( '  . / .  /                                      |           \   /
        /  /  _/ /    +                                      /              \/
       '  (__/                                             /                  \\
        ''')
    print()
    print('--------------------------------------------------------------------------------')
    print()
    exit


def game_loop():
    creatures = [
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Creature('Bat', 3),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000),
    ]
    hero = Player('Gandolf', 75)
    while True:
        active_creature = choice(creatures)
        print(f'A {active_creature.name} of level {active_creature.level} has appeared from a dark and foggy forest...')
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            print(f'The hero has {hero.hp} hit points')
            print(f'The {active_creature.name} has {active_creature.hp} hit points')
            while hero.is_alive() and active_creature.is_alive() and input('Continue? (y/n)').strip().lower() == 'y':
                hero.attack(active_creature)
                if not active_creature.is_alive():
                    print(f'The wizard has killed the {active_creature.name}')
                    creatures.remove(active_creature)
                    break

                active_creature.attack(hero)
                if not hero.is_alive():
                    print(f'The wizard was killed by the {active_creature.name}')
                    hero.heal(hero.max_hp)
                    break

                print(f'The hero has {hero.hp} hit points')
                print(f'The {active_creature.name} has {active_creature.hp} hit points')

        elif cmd == 'r':
            hero.heal(hero.max_hp)
            print(f'The wizard has healed')
        elif cmd == 'l':
            print(f'The wizard {hero.name} takes in the surroundings and sees:')
            for c in creatures:
                print(f' * A {c.name} of level {c.level}')
        else:
            print('Ok, exiting game... bye!')
            break

        if not creatures:
            print('You have defeated all the creates, well done!')
            break

        print()


if __name__ == '__main__':
    main()
