"""Module to define arguments and properties
"""

import sys
import os
import argparse

def get_args(name,args):
    """ Parses arguments of any file
    """
    desc = {
        "wc_med" : "Main class used to calculate word count and medians.",
        "manage" : "Global import file to maintain arguments across modules. Doesn't give any output.",
        "properties" : "Module to parse arguments. Doesn't give any output." 
    }
    need_input_dir = ["wc_med"]
    need_output_dir = ["wc_med"]
    if name in desc:
        parser = argparse.ArgumentParser(description=desc[name])
    else:
        parser = argparse.ArgumentParser()


    # Adding arguments which need input question file
    if name in need_input_dir:
        parser.add_argument("idir", type=str,
                            help="full path of directory to"
                            "load from. default: "+
                            "../wc_input/")
        
    # Adding arguments which need output question file
    if name in need_output_dir:
        parser.add_argument("odir", type=str,
                            help="full path of output directory to"
                            "write into. default: "+
                            "../wc_output/")
        
    # Adding global arguments 
    parser.add_argument("-v", "--verbose", type=int,
                        help="increase output verbosity")
    a = parser.parse_args()
    
    # Handling input file argument
    if name in need_input_dir:
        if a.idir:
            args['idir'] = a.idir

    # Handling output file argument
    if name in need_output_dir:
        if a.odir:
            args['odir'] = a.odir
    
    # Handling global arguments
    if a.verbose:
        sys.stderr.write("-"*5+" Note: Verbose output is on "
                         +"-"*5+"\n")
        args['v'] = a.verbose
    
if __name__ == "__main__":
    # Find current running program name 
    # and pass it for argument parsing
    running_file_name = os.path.basename(__file__).split('.')[0]
    get_args(running_file_name,args)
