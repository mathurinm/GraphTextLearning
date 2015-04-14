# -*- coding: utf-8 -*-

"""
represent each document as an undirected graph with weigthed edges

@authors: Mathurin Massias, Clement Nicolle, Michael Weiss
"""

from __future__ import division
import networkx as nx
import numpy as np

class GraphOfWordsWeighted :
    def __init__ (self,train_data,dico,sizeWindow):
        self.train_data=train_data
        self.n_doc = len(train_data)
        self.n_words = len(dico)
        self.sizeWindow=sizeWindow
        self.documentTerm=np.zeros((self.n_doc,self.n_words))
        self.graphs=[]        
        for i in range (self.n_doc):
            graph=nx.MultiGraph()
            doc = np.asarray(train_data[i])
            graph.add_edge(doc[0],doc[1])
            for j in range (len(doc)):
                for k in range (1,min(sizeWindow,len(doc)-j)):
                    graph.add_edge(doc[j],doc[j+k])
            self.graphs.append(graph)    
        
                    
    def compute_documentTerm(self,mode,dico):
        dico=np.asarray(dico)
        if mode==0 :
            for i in range(self.n_doc) :
                deg_centrality = nx.degree_centrality(self.graphs[i])
                for word,value in deg_centrality.items():
                    index=np.nonzero(dico==word)                    
                    self.documentTerm[i,index[0][0]]=value
        elif mode==1:
            for i in range(self.n_doc):
                    eig_centrality=nx.eigenvector_centrality(self.graphs[i])
                    for word,value in eig_centrality.items():
                        index=np.nonzero(dico==word)                    
                        self.documentTerm[i,index[0][0]]=value