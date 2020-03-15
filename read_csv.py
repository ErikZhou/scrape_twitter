import csv
import sys

def read_csv(filename): 
    rows = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            #print(row)
            rows.append(row)
    return rows


def main():
    # print command line arguments
    for arg in sys.argv[1:]:
        print(arg)
    filename = sys.argv[1]
    rows = read_csv(filename)
    print(rows)


if __name__ == "__main__":
    #usage()
    main()

