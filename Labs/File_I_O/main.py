import FileWriter
import DictWriter


def main():
    '''
    This is the main, it will take in a specific file location,
    add dictonaries to an array for easier access, and then write them
    to said file location.
    '''
    fr = FileWriter.FileWriter("labs\File_I_O\XC_ROSTER_TIMES.csv")

    people = [] #This holds all the dicts

    brandon = DictWriter.DictWriter("Brandon", 22, "16:59").dictmaker()
    steve = DictWriter.DictWriter("Steve", 20, "16:20").dictmaker()
    nate = DictWriter.DictWriter("Nate", 22, "18:43").dictmaker()
    henry = DictWriter.DictWriter("Henry", 19, "17:15").dictmaker()

    people.append(brandon)
    people.append(steve)
    people.append(nate)
    people.append("Not a Dict")
    people.append(henry)
    
    '''
    This loop is going over the array with all the dict objects.
    "x" is each dict in people, the array.
    It will try to write to the file and if it doesn't work then it will skip over
    if the object is not a dict
    '''
    for x in people:
        try:
            #print(x)
            fr.write_record(x)  
        except TypeError():
            print(x)
            print("Need to use a Dictonary to write to the file")
            

if __name__ == "__main__":
  main()