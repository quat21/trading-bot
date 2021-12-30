'''Delete all logs.'''

import os

files = [ file for file in os.listdir('logs') if file.endswith('.log') ]
for file in files:
    os.remove(os.path.join('logs', file))