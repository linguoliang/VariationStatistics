__author__ = 'Guoliang Lin'
Softwarename = 'splitGFF'
version = '1.0.1'
bugfixs = ''
import sys, getopt
import time
def trim(y):
    y = y.replace("[", '')
    y = y.replace(']', '')
    y = y.replace("',", '\t')
    y = y.replace("'", '')
    y = y.replace('\\n', '')
    y = y.replace(' ', '')
    # y=y.replace(',','')
    y = y.strip()
    y = y + '\n'
    return y

print('%s software version is %s' % (Softwarename, version))
print(bugfixs)
print('starts at :' + time.strftime('%Y-%m-%d %H:%M:%S'))

opts, args = getopt.getopt(sys.argv[1:], 'i:h', ['inputfile=', 'help'])
InputFileName = ''
for o, a in opts:
    if o in ['-i', '--inputfile']:
        fpkm = a
    elif o in ['-h', '--help']:
        help = True
with open(InputFileName, 'w') as InputFile:
