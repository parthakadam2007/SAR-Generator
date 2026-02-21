from neo4j import GraphDatabase

uri = "neo4j+s://917d6831.databases.neo4j.io"
user = "neo4j17d6831"
password = "JqEpO7M2ddNpkPYnyokQQ-SY-KmPouBUr-7oc9HJP4o"

driver = GraphDatabase.driver(uri, auth=(user, password))

driver.verify_connectivity()

print("Connected successfully!")