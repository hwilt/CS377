import redis
from redisgraph import Node, Edge, Graph

# https://dev.to/ramko9999/host-and-use-redis-for-free-51if
# https://github.com/RedisGraph/redisgraph-py
# https://www.redislabs.com

# control-shift-S to launch repl.it shell and set these variables
password = "uGfCyWtQJcN1wpUbs5mpAdTH9dSGpoIZ";
dbname = "GEDCOM"
url = "redis-14543.c91.us-east-1-3.ec2.cloud.redislabs.com"
port = 14543

redisdb = redis.Redis(host=url, port=port, password=password)
graph = Graph('social', redisdb)

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

