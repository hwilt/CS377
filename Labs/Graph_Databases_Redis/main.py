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
			nodes.append(["MOTHER", Node(label = "MOTHER", properties=family[person])])
		elif family[person]['relationship'] == 'FATHER':
			nodes.append(["FATHER", Node(label = "FATHER", properties=family[person])])
		else:
			nodes.append(["CHILD", Node(label = "CHILD", properties=family[person])])
	for node in nodes:
		graph.add_node(node)
		if node[0] == "MOTHER":
			for innerNode in nodes:
				if node[0] == "FATHER":
					married = Edge(node, 'Married', innnerNode)
					graph.add_edge(married)	
				elif node[0] == "CHILD":
					children = Edge(node, "child", innerNode)
					graph.add_edge(children)
		elif node[0] == "FATHER":
			for innerNode in nodes:
				if node[0] == "MOTHER":
					married = Edge(node, 'Married', innnerNode)
					graph.add_edge(married)
				elif node[0] == "CHILD":
					children = Edge(node, "child", innerNode)
					graph.add_edge(children)
		else:
			for innerNode in nodes:
				if node[0] == "MOTHER" or node[0] == "FATHER":
					children = Edge(node, "is child", innerNode)
					graph.add_edge(children)
	graph.commit()
	query = "MATCH (a:MOTHER)-[d1:Married]->(b:FATHER) RETURN a.name, b.name"

def main():
	graph = make_graph()
	FILE_READ = FileReader.FileReader("gedcom.ged")   
	people = FILE_READ.read_record()
	family = {}

	for id in people.keys():
		person = PersonWriter.PersonWriter(people[id]['name'], people[id]['relationship'], id)
		family[id] = person.__str__()
	
	makeNodes(family, graph)

if __name__ == "__main__":
    main()
'''
# Reinitialize
redisdb.flushdb() # also redisdb.delete(keyname)

kphl = Node(label="airport", properties={"description": "Philadelphia International Airport"})
kmco = Node(label="airport", properties={"description": "Orlando International Airport"})
kbwi = Node(label="airport", properties={"description": "Thurgood Marshall Baltimore Washington International Airport"})
kabq = Node(label="airport", properties={"description": "Albuquerque International Sunport"})

graph.add_node(kphl)
graph.add_node(kmco)
graph.add_node(kbwi)
graph.add_node(kabq)

route1 = Edge(kphl, 'direct', kmco)
route2 = Edge(kmco, 'direct', kabq)
route3 = Edge(kbwi, 'direct', kabq)

graph.add_edge(route1)
graph.add_edge(route2)
graph.add_edge(route3)

graph.commit()

# Direct routes
query1 = """MATCH (a:airport)-[d1:direct]->(b:airport) RETURN a.description, b.description"""
graph.query(query1).pretty_print()

# One layover routes
query2 = """MATCH (a:airport)-[d1:direct]->(b:airport)-[d2:direct]->(c:airport) RETURN a.description, b.description, c.description"""
graph.query(query2).pretty_print()
'''

