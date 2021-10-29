'''
This class holds the person's name, age, and 5k time

'''
class DictWriter():
    """
    Construct a Dict

    :param _name: The name of the person
    :param _age: The age of the person
    :param _time: Their fastest 5k time
    """
    def __init__(self, _name, _age, _time):
        self.Name = _name
        self.Age = _age
        self.Time = _time

    def dictmaker(self):
        exampledict = {}
        exampledict['Name'] = self.Name
        exampledict['Age'] = self.Age
        exampledict['5k Time'] = self.Time
        return exampledict
