#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from factory import Factory
 
class BaseBug(object):
    def __init__(self):
        self.hits = []
    def move(self, x, y):
        print 'move', x, y
    def how_feel(self):
        print "i'm ", self.hits

class BaseWarrior(BaseBug):
    def fight(self):
        print 'fight'
    def hit(self, him):
        self.fight()
        him.hits.append('ematome')
        return him

class SpaceWarrior (BaseWarrior):
    def fight(self):
        super(SpaceWarrior, self).fight()
        print 'Se bat dans l\'espace'
 
class ArmedWarrior (BaseWarrior):
    def fight(self):
        super(ArmedWarrior, self).fight()
        print 'tire un coup de fusil'
    def hit(self, him):
        him = super(ArmedWarrior, self).hit(him)
        him.hits.append('perfore')
        return him
 
class TotoWarrior (ArmedWarrior):
    def fight(self):
        super(TotoWarrior, self).fight()
        print 'fait toto!'
 
class ArmedWarrior2 (ArmedWarrior):
    def how_feel(self):
        try:
            self.hits.index('perfore')
            print 'Damned! je suis perfore !'
        except ValueError:
          super(FooWarrior, self).how_feel()
 
factory = Factory()
 
factory.extend('Warrior', SpaceWarrior, BaseWarrior)
factory.extend('Warrior', ArmedWarrior, BaseWarrior)
 
factory.extend('Warrior', TotoWarrior, ArmedWarrior)
factory.extend('Warrior', ArmedWarrior2, ArmedWarrior)
 
some_bug_hited = factory.get_class('Warrior')()
 
warrior = factory.get_class('Warrior')()
warrior.hit(some_bug_hited)

print 'and hited bug say:'
some_bug_hited.how_feel()