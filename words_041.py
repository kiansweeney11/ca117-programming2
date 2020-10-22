#!/usr/bin/env python

def main():
    import sys
    d = {}
    a = []
    
    for line in sys.stdin:
        sentence = line.lower().split()
        for token in sentence:
            count = 0
            i = 0
            while i < len(token) and token[i] is not token.isalnum() and token[i] != " ":
                if token[i] !=  









if __name__ == '__main__':
    main()
