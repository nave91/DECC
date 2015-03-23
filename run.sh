#!/usr/bin/env bash

# run script for running the word count

# first I'll load all my dependencies
apt-get install python-pandas

# Give proper permissions
chmod a+x ./src/wc_med.py
chmod a+x ./src/manage.py
chmod a+x ./src/properties.py

# Show sample of how arg parsing works
python ./src/wc_med.py -h

# Execute program on default directories
python ./src/wc_med.py ./wc_input ./wc_output/


