import csv
import sys
import os
import get_following
import read_csv
import get_tw
import merge_csv
import csv_to_txt
import csv_sort

def usage():
    print('python tw.py user')
    print('output csv merged')


def run_cmd(cmd): 
    print(cmd)
    returned_value = os.system(cmd)  # returns the exit code in unix
    print('returned value:', returned_value)


def do(user):
    # step 1
    print(' step 1')
    get_following.get_following(user)

    # step 2
    print(' step 2')
    filename = 'data/following.csv'
    rows = read_csv.read_csv(filename)
    #print(rows)
    print(' step 3')
    for c in rows:
        #print(c)
        #print(str(c[0]))

        # step 3
        get_tw.get_tw(str(c[0]))

    # step 4 merge csv
    print(' step 4')
    merge_csv.do()

    # setp 5 sort csv
    print(' step 5')
    mergedfile = 'merged.csv'
    csv_sort.csv_sort(mergedfile)

    # setp 6 csv to txt
    print(' step 6')
    mergedfile = 'merged.csv_.csv'
    csv_to_txt.csv_to_txt(mergedfile)

    # setp 7 delete csv
    print(' step 7')
    cmd = 'rm -rf tweets_*.csv'
    run_cmd(cmd)


def main():
    for arg in sys.argv[1:]:
        print(arg)
    user = sys.argv[1]
    do(user)


if __name__ == "__main__":
    usage()
    main()

