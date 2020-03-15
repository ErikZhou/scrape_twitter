import os
import sys

def usage():
    print('python get_following user')


def get_following(user):
    cmd = "twint -u " + user + " --following -o data/following.csv --csv"
    print(cmd)
    if not os.path.exist('data'):
        os.mkdir('data')

    returned_value = os.system(cmd)  # returns the exit code in unix
    print('returned value:', returned_value)


def main():
    for arg in sys.argv[1:]:
        print(arg)
    user = sys.argv[1]
    get_following(user)


if __name__ == "__main__":
    usage()
    main()

