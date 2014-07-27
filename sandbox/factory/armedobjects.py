from factory import Factory
from baseobjects import BaseWorker, BaseWarrior

class ArmedWarrior(BaseWarrior):
    def fight(self):
        super(ArmedWarrior, self).fight()
        print 'tire un coup de fusil'

factory = Factory()
factory.extend('Warrior', ArmedWarrior)