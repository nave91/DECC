"""
Manager of module to declare defaults
and also define necessary tools.
Author: nave91
"""

import sys
import re

from heapq import heappush as push, heappushpop as pushpop

# Defaults used in module 
INPUT_DIR = "../wc_input/"
OUTPUT_DIR = "../wc_output/"
OUT_FILE_WC = "wc_result.txt"
OUT_FILE_MED = "med_result.txt"


class Tools:
    """ All necessary tools can be factored
    here for convenience.
    """
    
    def line(self, file_):
        """ Filters out non-alphabet characters
        excluding spaces.
        """
        l = file_.readline()
        if l != '':
            l = re.sub(r'[^\w\s]', '', l)
            return l.lower().split()
        else:
            return -1


    def get_median(self):
        """Maintain low and high heaps for receiving 
        lengths of line. Low having lengths less than median
        and high having lengths greater than median.
        len(high) > len(low)
        """        
        def gen():
            # Highest element of low is at its root and
            # Lowest element of high is at its root
            low, high = [], [(yield)]
            while True:
                # Yield high if high > low
                push(low,  -pushpop(high, (yield high[0]*1.0)))
                # Else yield average of roots
                push(high, -pushpop(
                    low, 
                    -(yield((high[0] - low[0]) / 2.0)))
                )
        g = gen()
        next(g)
        return g
