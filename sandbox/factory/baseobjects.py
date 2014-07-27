from factory import Factory

class BaseBug(object):
    def move(self, x, y):
        print 'move', x, y

class BaseWorker(BaseBug):
    def work(self):
        print 'work based'

class BaseWarrior(BaseBug):
    def fight(self):
        print 'fight'
