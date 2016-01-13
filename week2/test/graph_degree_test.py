'''
Created on Sep 8, 2015

@author: jglara
'''
import unittest
from graph_degree import make_complete_graph


class Test(unittest.TestCase):
    '''
    '''

    def test_make_complete_graph(self):
        self.assertEquals(make_complete_graph(0), {})
        self.assertEquals(make_complete_graph(-1), {})
        self.assertEquals(len(make_complete_graph(6)), 6)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()