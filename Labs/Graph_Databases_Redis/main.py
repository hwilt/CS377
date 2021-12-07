
import redis
import FileReader
import PersonWriter
from redisgraph import Node, Edge, Graph


def make_graph():
	password = "uGfCyWtQJcN1wpUbs5mpAdTH9dSGpoIZ";
	dbname = "GEDCOM"
	url = "redis-14543.c91.us-east-1-3.ec2.cloud.redislabs.com"
	port = 14543

	redisdb = redis.Redis(host=url, port=port, password=password) 
	redisdb.flushdb()
	return Graph('social', redisdb)


def makeNodes(family, graph):
	nodes = []
	for person in family.keys():
		if family[person]['relationship'] == 'MOTHER':
			nodes.append(["MOTHER", Node(label = "PARENT", properties=family[person])])
		elif family[person]['relationship'] == 'FATHER':
			nodes.append(["FATHER", Node(label = "PARENT", properties=family[person])])
		else:
			nodes.append(["CHILD", Node(label = "CHILD", properties=family[person])])
	for node in nodes:
		graph.add_node(node[1])
		#print(node[1])
	
	for node in nodes:
		if node[0] == "MOTHER":
			for innerNode in nodes:
				if innerNode[0] == "FATHER":
					married = Edge(node[1], 'MARRIED', innerNode[1])
					graph.add_edge(married)	
					#print(married)
				elif innerNode[0] == "CHILD":
					children = Edge(node[1], 'PARENT', innerNode[1])
					graph.add_edge(children)
					#print(children)
		elif node[0] == "FATHER":
			for innerNode in nodes:
				if innerNode[0] == "MOTHER":
					married = Edge(node[1], 'MARRIED', innerNode[1])
					graph.add_edge(married)
					#print(married)
				elif innerNode[0] == "CHILD":
					children = Edge(node[1], 'PARENT', innerNode[1])
					graph.add_edge(children)
					#print(children)
		else:
			for innerNode in nodes:
				if innerNode[0] == "MOTHER" or innerNode[0] == "FATHER":
					children = Edge(node[1], 'CHILD', innerNode[1])
					graph.add_edge(children)
					#print(children)
	graph.commit()
	
def querying(graph):
	print("Married Couples: ")
	query1 = """MATCH (Mother:PARENT {relationship: "MOTHER"})-[relation:MARRIED]->(Father:PARENT {relationship: "FATHER"}) RETURN Mother.name, Father.name"""
	graph.query(query1).pretty_print()
	print("Children:")
	query2 = """MATCH (Parent:PARENT)-[:PARENT]->(Child:CHILD) RETURN Parent.name, Parent.relationship, Child.name, Child.relationship """
	graph.query(query2).pretty_print()


def main():
	graph = make_graph()
	FILE_READ = FileReader.FileReader("gedcom.ged")   
	people = FILE_READ.read_record()
	family = {}

	for id in people.keys():
		person = PersonWriter.PersonWriter(people[id]['name'], people[id]['relationship'], id)
		family[id] = person.__str__()
	
	makeNodes(family, graph)
	querying(graph)
	
if __name__ == "__main__":
    main()

