"""
Main file to calculate word count and median
Author: nave91
"""

import sys
import os

import pandas as pd

from manage import Tools, INPUT_DIR, OUTPUT_DIR
from manage import OUT_FILE_WC, OUT_FILE_MED


class ParseDir:
    """ Parses Directory to get files and
    compute necessary operations on them.
    """

    def __init__(self, dir_):
        self.dir_ = dir_
        
        # Loads tools into current model to 
        # maintain generated values
        self.tools = Tools()

        # Pandas Series and median generator
        # for computations
        self.word_count = pd.Series()
        self.gen_median = self.tools.get_median()

        # Locals
        self.medians = []
        self.file_series= []

    def get_files(self):
        for f in os.listdir(self.dir_):
            abs_file_path = self.dir_ + f
            if os.path.isfile(abs_file_path):
                self.file_series.append(
                    # Converts all files into
                    # Pandas Series
                    ParseFile(
                        abs_file_path, 
                        self.tools, 
                        self.gen_median
                    )
                )

    def parse_files(self):
        # Calculate medians and word counts
        for file_ in self.file_series:
            wc, med = file_.collect()
            self.word_count = self.word_count.append(wc)
            self.medians += med

    def show_results(self):
        # Writes results back to directory 
        wc_result = self.word_count.value_counts()
        wc_result = wc_result.sort_index()
        wc_result.to_csv(
            OUTPUT_DIR+OUT_FILE_WC,
            sep='\t'
        )
        med_result = self.medians
        with open(OUTPUT_DIR+OUT_FILE_MED,'w') as file_:
            for med in med_result:
                file_.write(str(med)+"\n")

    def get_results(self):
        # Flow to accomplish current task
        self.get_files()
        self.parse_files()
        self.show_results()

            
class ParseFile:
    """ Maintains pandas series and calculates
    medians from tools generator for each file.
    """
    
    def __init__(self, file_, tools, gen_medians):
        # Panda series for word counts
        self.words = pd.Series()
        self.file_ = file_

        # Tools to maintain median generator 
        # across the program
        self.tools = tools
        self.medians = []

        # Read and initialize file
        self.read(gen_medians)


    def read(self, gen_medians):
        lsts = []
        with open(self.file_, 'r') as f:
            while True:
                lst = self.tools.line(f)
                if lst != -1:
                    # Get medians from generator and maintain them
                    # across multiple files
                    med = gen_medians.send(len(lst))
                    self.medians.append(med)
                    lsts.append(lst)
                    
                    # Maintain words using pandas series
                    self.words = self.words.append(pd.Series(lst))
                else:
                    sys.stderr.write("WARNING: Empty File or EOF\n")
                    break
    
    def __str__(self):
        return "File Series:\n" + str(self.words)

    def collect(self):
        # Collect and show results
        return self.words, self.medians


if __name__=='__main__':
    f = ParseDir('../wc_input/')
    print f.get_results()
