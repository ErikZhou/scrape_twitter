import sys
import csv

def csv_to_txt(filename):
    csv_file = filename
    txt_file = filename +'.txt'
    with open(txt_file, "w") as my_output_file:
        with open(csv_file, "r") as my_input_file:
            [ my_output_file.write(str(" ".join(row))[str(" ".join(row)).find('202'):]+'\n') for row in csv.reader(my_input_file)]
        my_output_file.close()


def main():
    for arg in sys.argv[1:]:
        print(arg)
    filename = sys.argv[1]
    csv_to_txt(filename)


if __name__ == "__main__":
    main()

