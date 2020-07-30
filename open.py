#!/usr/bin/python3
from youtube_search import YoutubeSearch
import sys, getopt

def main(argv):
    inputfile = ''
    numberfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ('spotitube.py -i <Search Keyword> -o <Index>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('spotitube.py -i <Search Keyword> -o <Index>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ifile"):
            numberfile = arg
    results = YoutubeSearch(inputfile, max_results=int(numberfile)).to_dict()    
    ans = 'https://youtu.be/' + results[int(numberfile)-1]['url_suffix'][9:]
    print(ans)

if __name__ == "__main__":
    main(sys.argv[1:])