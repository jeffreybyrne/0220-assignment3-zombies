import random
import math

class Zombie:

    max_speed = 5
    max_strength = 8
    horde = []
    plague_level = 10
    default_speed = 1
    default_strength = 3

    def __init__(self, speed, strength):
        """Initializes zombie's speed and the strength
        """
        if speed > Zombie.max_speed:
            self.speed = Zombie.default_speed
        else:
            self.speed = speed

        if strength > Zombie.max_strength:
            self.strength = Zombie.default_strength
        else:
            self.strength = strength

    def __str__(self):
        return "This zombie has a speed of {} and a strength of {}.".format(self.speed,self.strength)

    @classmethod
    def spawn(cls):
        """Spawns a random number of new zombies, based on the plague level,
        adding each one to the horde.  Each zombie gets a random speed.
        """
        new_zombies = random.randint(1, Zombie.plague_level)
        count = 0

        while count < new_zombies:
            speed = random.randint(1, Zombie.max_speed)
            strength = random.randint(1, Zombie.max_strength)
            Zombie.horde.append(Zombie(speed,strength))
            count += 1

    @classmethod
    def new_day(cls):
        """Represents the events of yet another day of the zombie apocalypse.
        Every day some zombies die off (phew!), some new ones show up,
        and sometimes the zombie plague level increases.
        """
        Zombie.some_die_off()
        Zombie.spawn()
        Zombie.increase_plague_level()

    @classmethod
    def some_die_off(cls):
        """Removes a random number (between 0 and 10) of zombies from the horde.
        """
        how_many_die = random.randint(0, 10)
        counter = 0
        while counter < how_many_die and len(Zombie.horde) > 0:
            random_zombie = random.randint(0,len(Zombie.horde) - 1)
            Zombie.horde.pop(random_zombie)
            counter += 1

    @classmethod
    def increase_plague_level(cls):
        """Increases the plague level by a random number between 0 and half the number of total zombies
        """
        plague_increase = random.randint(0,math.floor(len(Zombie.horde)/2))
        Zombie.plague_level += plague_increase

    @classmethod
    def deadliest_zombie(cls):
        """Returns the zombie with the highest speed & strength
        """
        if len(Zombie.horde) == 1:
            return Zombie.horde[0]
        else:
            deadliest_zombie = Zombie.horde[0]
            deadliest_stats = Zombie.horde[0].speed + Zombie.horde[0].strength
            for num in range(1,len(Zombie.horde)):
                curr_stats = Zombie.horde[num].speed + Zombie.horde[num].strength
                if curr_stats > deadliest_stats:
                    deadliest_zombie = Zombie.horde[num]
                    deadliest_stats = curr_stats
            return deadliest_zombie

    def encounter(self):
        """This instance method represents you coming across a zombie! This can end in two possible outcomes:
        1. You outrun the zombie and escape unscathed!
        2. You don't outrun the zombie. If you don't, you end up fighting it
        3. If you win the fight, you still catch the zombie plague and turn into a zombie
        4. If you lose the fight, it eats your brains and you die. :(
        Returns a summary of what happened.
        """
        outrun = self.chase()
        won_fight = self.fight()

        if outrun:
            return 'You escaped!'
        elif won_fight:
            new_zomb = Zombie(random.randint(1,Zombie.max_speed),random.randint(1,Zombie.max_strength))
            Zombie.horde.append(new_zomb)
            return "You didn't outrun the zombie, but you managed to fight it off. Sadly, you're a zombie now."
        else:
            return 'You died.'

    def chase(self):
        """Represents you trying to outrun this particular zombie.
        Uses `Zombie.max_speed` to generate a random number that represents how fast you manage to run.
        """
        your_speed = random.randint(1, Zombie.max_speed)
        return your_speed > self.speed

    def fight(self):
        """Represents you trying to fight a zombie.
        """
        your_strength = random.randint(1, Zombie.max_strength)
        return your_strength > self.strength

# poor_bill = Zombie(7,3)
# print(poor_bill)
# Zombie.horde.append(poor_bill)
# print(Zombie.horde)


print(Zombie.horde) # []
Zombie.new_day()
print(Zombie.horde) # [<__main__.Zombie object at 0x7f6f594f0d30>, <__main__.Zombie object at 0x7f6f594f0b70>, <__main__.Zombie object at 0x7f6f594f0d68>]
print(Zombie.deadliest_zombie())
zombie1 = Zombie.horde[0]
print(zombie1) # Speed: 1 -- Strength: 7
# zombie2 = Zombie.horde[1]
# print(zombie2) # Speed: 2 -- Strength: 7
print(zombie1.encounter()) # You escaped!
# print(zombie2.encounter()) # You fought the zombie and caught the plague.  You are now a zombie too.  Raaaawrgh
Zombie.new_day()
print(Zombie.horde) # [<__main__.Zombie object at 0x7f6f594f0d30>, <__main__.Zombie object at 0x7f6f594efef0>, <__main__.Zombie object at 0x7f6f594f0c50>, <__main__.Zombie object at 0x7f6f594f0cc0>]
zombie1 = Zombie.horde[0]
# zombie2 = Zombie.horde[1]
print(zombie1.encounter()) # You died!
# print(zombie2.encounter()) # You escaped!
