#!/usr/bin/python3
from youtube_search import YoutubeSearch
import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ('spotitube.py -i <Search Keyword>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        results = YoutubeSearch(inputfile, max_results=10).to_dict()
        
        
        ans = 'https://youtu.be/' + results[0]['url_suffix'][9:]
        print(ans)

if __name__ == "__main__":
    main(sys.argv[1:])