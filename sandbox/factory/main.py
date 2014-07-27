from factory import Factory
import spaceobjects
import armedobjects

factory = Factory()

warrior = factory.get_class('Warrior')()
warrior.fight()