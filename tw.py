import csv
import sys
import get_following
import read_csv
import get_tw
import merge_csv
import csv_to_txt

def usage():
    print('python tw.py user')
    print('output csv merged')

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

    # setp 5 csv to txt
    print(' step 5')
    mergedfile = 'merged.csv'
    csv_to_txt.csv_to_txt(mergedfile)



def main():
    for arg in sys.argv[1:]:
        print(arg)
    user = sys.argv[1]
    do(user)


if __name__ == "__main__":
    usage()
    main()
