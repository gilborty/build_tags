#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    __author__="Gilbert Montague"
    Super simple way to add build tags to a file
"""
import argparse








if __name__ == '__main__':
    
    #Parse command line arguments
    parser = argparse.ArgumentParser()
    #Need a file name
    parser.add_argument('-f','--file',help='File to edit',required=True)

    #The tag we are operating on
    parser.add_argument('-t', '--tag',help='The tag to operate on',required=True)

    #Subparsers
    subparsers = parser.add_subparsers(dest='subcommand')
    #Add tags?
    parser_add = subparsers.add_parser('add')
    parser_add.add_argument('-t','--text',help='The text to be inserted')

    #Or remove them
    parser_remove = subparsers.add_parser('remove')

    args = parser.parse_args()
    print(args)
                
