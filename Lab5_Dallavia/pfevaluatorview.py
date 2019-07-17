#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 15:22:58 2018

@author: RCD
"""

from model import PFEvaluatorModel
#from model import PFEvaluator
#from scanner import Scanner

class PFEvaluatorView(object):
    
    def __init__(self):
        self.model = PFEvaluatorModel()
        #self.model.run()
    
    def run(self):
        while True:
            postfix = input("Enter a postfix expression: ")
            if not len(postfix):
                return
            normalized_str = self.model.format(postfix)
            print(normalized_str)
            value = self.model.evaluate(normalized_str)
            if isinstance(value, int):
                print(value)
            else:
                print("Error: " + str(value), end="")
                print(self.model.evaluationStatus())
                
                