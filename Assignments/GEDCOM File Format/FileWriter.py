import os

class FileWriter:
    
    '''
    Construct a FileWriter
    
    :param _filename: The filename to open
    :param _append: Whether to append to the file or overwrite
    '''
    def __init__(self, _filename, _append=False):
        self.filename = _filename
        
        if _append:
            mode = 'a+'
        else:
            mode = 'w'
        self.f = open(self.filename, mode)

    '''
    Destructor: flush and close the file 
    '''
    def __del__(self):
        self.f.flush()
        self.f.close()    

    '''
    Write a dictionary row, writing the keys as the header line if the file is empty.
    
    :param data: The dictionary to write - must be a dict
    :raises TypeError: if the data parameter is a type other than dict
    '''
    def write_record(self, family):
        MOM_DAD = False
        if isinstance(family, dict): # ensure data is a dict
        # write header if the file is empty
            if os.stat(self.filename).st_size == 0:
                self.f.write("digraph G { \n \tnode [shape = box]\n")
                for person in family.keys():
                    self.f.write("\t" + person + " [label= \"" +  family[person]['name'] + "\n" + family[person]['relationship'] + "\"]\n")
                    if family[person]['relationship'] != 'CHILD' and not MOM_DAD:
                        MOM_DAD = True    
                        for children in family.keys():
                            if family[children]['relationship'] == 'CHILD':
                                self.f.write("\t" + family[person]['id'] + " -> " + family[children]['id'] + " [label = \"Child\"]\n")
                            elif family[children]['relationship']  == 'FATHER' and family[person]['relationship'] != 'FATHER':
                                self.f.write("\t" + family[person]['id'] + " -> " + family[children]['id'] + " [arrowhead=none; label = \"Married\"]\n")
                            elif family[children]['relationship']  == 'MOTHER' and family[person]['relationship'] != 'MOTHER':
                                self.f.write("\t" + family[person]['id'] + " -> " + family[children]['id'] + " [arrowhead=none; label = \"Married\"]\n")
                                
                for parent in family.keys():
                    if family[parent]['relationship'] == 'MOTHER':
                        for _parent in family.keys():
                            if family[_parent]['relationship'] == 'FATHER':
                                self.f.write("\t { rank = same; " + family[parent]['id'] + ", " + family[_parent]['id'] + "}\n")
                # write a newline
                self.f.write("}\n")
                self.f.flush()
        else:
            return TypeError("Data must be a dict")
  
    
  
    
  
