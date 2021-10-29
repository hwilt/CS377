
class PersonWriter():
    
    def __init__(self, _name, _relationship, _personID):
        self.name = _name
        self.ID = _personID
        
        if _relationship == "WIFE":
            self.relationship = "MOTHER"
        elif _relationship == "HUSB":
            self.relationship = "FATHER"
        else:
            self.relationship = "CHILD"
            
    def __str__(self):
        exampledict = {}
        exampledict['name'] = self.name
        exampledict['relationship'] = self.relationship
        exampledict['id'] = self.ID
        return exampledict
    

