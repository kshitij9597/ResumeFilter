#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 14:07:49 2018

@author: himanshu
"""

import urllib
import numpy as np
import os
import re
import zipfile

#NEEDS UPDATION.

def create_embedding(data_dir_path,embedding_size = None, download = False):
    if embedding_size == None:
        embedding_size = 50
    if(download):
        print('Glove.6B.zip is being downloaded>>>>')
        glove_zip = os.path.join(data_dir_path + 'glove.6B.zip')
        urllib.request.urlretrieve(url='http://nlp.stanford.edu/data/glove.6B.zip', filename=glove_zip)
        zipped = zipfile.ZipFile(glove_zip,mode = 'r')
        zipped.extractall()
        zipped.close()
        
    glove_file_path =  data_dir_path + '/glove.6B.' + str(embedding_size) + 'd.txt'
    embedding_dict = {}
    with open(glove_file_path,'r') as file:
        for line in file:
            word = line.strip().split(' ')[0]
            embed = np.array(line.strip().split(' ')[1:], dtype = np.float32)
            embedding_dict[word] = embed
            
    return embedding_dict    
            
             
            
class GloveVector():
    def __init__(self,embedding_size = None):
        self.embedding_size = embedding_size
        
    def embedding_creation(self,data_dir_path,embedding_size):
        if embedding_size == None:
            embedding_size = 50
        embedding_dict = create_embedding(data_dir_path, embedding_size)
        return embedding_dict
#    
#    def encode_text(self,input_text_or_file):
#        if input_text_or_file.is
#        
        
        
    
    