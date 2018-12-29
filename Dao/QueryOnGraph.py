#-*- coding:UTF-8 -*-
'''
Created on 2018年11月12日

@author: master
'''

from neo4j.v1 import  GraphDatabase


class QueryOnGraph:
    
   
    
    
    
    
    
    def __init__(self,driver):
        self.driver = driver
    
    
    def listreader(self,cypher,keys):
        with self.driver.session() as session:
            with session.begin_transaction() as tx:
                data = []
                result = tx.run(cypher)
                for record in result:
                    rows = []
                    for key in keys:
                        rows.append(record[key])
                    data.append(rows)
                return data
    
    
    
    
    
if __name__ == '__main__':
    url= 'bolt://localhost:7687'
    driver = GraphDatabase.driver(url,auth=("neo4j","546301"))
    cypher_read = "MATCH (n:Movie)-[r:is]-(g:Genre) where n.movie_title = 'Forrest Gump' return g.genre_name as g"
    QG = QueryOnGraph(driver)
    results = QG.listreader(cypher_read, ['g'])
    for r in results:
        print r[0]
    
     
   