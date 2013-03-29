import random

class Probability(object):
  
  @staticmethod
  def getChoiceForPercents(choices):
    choices_values = Probability.getValuesForPercentChoices(choices)
    randomint = Probability.getRandomForPercentChoices(choices_values)
    for choice_value in choices_values:
      if randomint >= choice_value[0] and randomint <= choice_value[1]:
        return choices_values.index(choice_value)
    raise "N'est pas parvenu a faire un choix ! (si cette erreur est lance: erreur d'algo!)"
  
  @staticmethod
  def getValuesForPercentChoices(choices):
    values =  []
    previous_percent = 0
    for choice_percent in choices:
      values.append((previous_percent+1, previous_percent+choice_percent))
      previous_percent += choice_percent
    return values
  
  @staticmethod
  def getRandomForPercentChoices(choices_values):
    total = 0
    # TODO: Rendre ca plus joli, il faut connaitre la taille de la lise pour aller chercher la derniere
    # on pourra directement calculer ca dans getChoiceForPercents
    for choice_value in choices_values:
      total = choice_value[1]
    return random.randint(1, total)