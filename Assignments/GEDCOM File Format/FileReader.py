
class FileReader():
    
    """
    Constructor: Open the file
    
    :param _filename: The filename of the file to open.
    """
    def __init__(self, _filename):
        self.filename = _filename
        
        self.f = open(self.filename, 'r')
        
    """ 
    Destructor: close the file 
    """
    def __del__(self):
        self.f.close()
    
    
    def read_record(self):
        person = {}
        people = {}
        
        id = ''
        
        for line in self.f:
            #print(line)
            
            tokens = line.split()
            #print(tokens)
            
            if tokens[0] == "0":
                if len(tokens) >= 3:    
                    if tokens[2] == 'INDI':
                        #print("Found an INDI, They are " + tokens[1])
                        #print(person)
                        if not (id == ''):
                            people[id] = person
                        id = tokens[1].strip('@')
                        person = {}
                        
            elif tokens[0] == '1':
                if tokens[1] == 'NAME':
                    #print("I found a name!")
                    #print(line)
                    name = line.strip() 
                    spacelocation = name.index(' ')
                    secondspacelocation = name.index(' ', spacelocation+1)
                    # This line below turns '1 NAME Bob /Lee' to 'Bob Lee'
                    person['name'] = name[secondspacelocation:].replace('/', '').strip()   
                    
                elif tokens[1] == "WIFE" or tokens[1] == "CHIL" or tokens[1] == "HUSB":
                    #print(line)
                    relationship = line.strip()
                    spacelocation = relationship.index(' ')
                    secondspacelocation = relationship.index(' ', spacelocation+1)
                    personID = line[secondspacelocation:].replace('@', '').strip()
                    if personID in people:
                        # This line below turns '1 CHIL @I1@' to 'CHIL' for the correct id
                        people[personID]['relationship'] = relationship[spacelocation:secondspacelocation].strip()
                    else:
                        # This line below turns '1 CHIL @I1@' to 'CHIL'
                        person['relationship'] = relationship[spacelocation:secondspacelocation].strip()
                    
        
        # get the last person
        people[id] = person
        
        #print(people)
        return people     