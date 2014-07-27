from factory import Factory
from baseobjects import BaseWorker, BaseWarrior

class SpaceWarrior(BaseWarrior):
    def fight(self):
        super(SpaceWarrior, self).fight()
        print 'Se bat dans l\'espace'

factory = Factory()
factory.extend('Warrior', SpaceWarrior)