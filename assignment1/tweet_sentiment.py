import sys
import json

def prob2():
    afinnfile = open("AFINN-111.txt")
    scores = {}
    for line in afinnfile:
        term, score = line.split("\t")
        scores[term] = int(score) 
    tweet_file = open("output.txt") 
    for line in tweet_file:
        pline = json.loads(line)
        sentscore = 0
        if 'text' in pline: 
            for word in pline['text'].split(" "):
                if word in scores.keys():
                    sentscore += scores[word]
        print sentscore 

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    prob2()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
