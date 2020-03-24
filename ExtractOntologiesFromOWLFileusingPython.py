"""
Author: Shweta Katkade
This script will execute the SPARQL query on ontologies.
"""

import argparse
import rdflib
from rdflib import plugin
from rdflib.graph import Graph
import os

CUR_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)))

def get_ontologies(file_path, property_name):
        #inputs: owl_file: owl file path, query: SPARQL query to be executed
        #output: output of the query
        g = Graph()
        g.parse(file_path)
        x="""PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: 
        PREFIX rdfs: 
        PREFIX xsd: 
        SELECT * WHERE {?object rdfs:subClassOf?<http://xyz.owl#>}
        """
                
        qres = g.query(x)
        property_name = []
        for sub in qres:
                property_name.append(str(sub).split("#")[1])
                
        return property_name



if __name__ == '__main__':
              action = get_ontologies(r"C:\Shweta\xyz.owl", "ABC" )
          
         
                              

