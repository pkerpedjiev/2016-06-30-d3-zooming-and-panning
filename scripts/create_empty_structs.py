#!/usr/bin/python

import sys
from optparse import OptionParser

def main():
    usage = """
    python create_empty_structs.py '((..))'

    Print out an array containing strings representing a growing RNA strand
    up until the sequence specified at the end.
    """
    num_args= 1
    parser = OptionParser(usage=usage)

    #parser.add_option('-o', '--options', dest='some_option', default='yo', help="Place holder for a real option", type='str')
    #parser.add_option('-u', '--useless', dest='uselesss', default=False, action='store_true', help='Another useless option')

    (options, args) = parser.parse_args()

    if len(args) < num_args:
        parser.print_help()
        sys.exit(1)

    output = []
    for i in range(1, len(args[0])):
        output += ["".join(['.']*i)]

    output += [args[0]]

    print "[" + ",".join(map(lambda x: '"' + x + '"' , output)) + "].reverse()"
if __name__ == '__main__':
    main()

