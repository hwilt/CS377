import FileReader
import PersonWriter
import FileWriter

def main():
    FILE_READ = FileReader.FileReader("gedcom.ged")   
    people = FILE_READ.read_record()
    family = {}
    
    for id in people.keys():
        person = PersonWriter.PersonWriter(people[id]['name'], people[id]['relationship'], id)
        family[id] = person.__str__()
        
    #print(family)    
    FILE_WRITE = FileWriter.FileWriter("graph.dot")
    FILE_WRITE.write_record(family)
    
    #print(people)
if __name__ == "__main__":
    main()