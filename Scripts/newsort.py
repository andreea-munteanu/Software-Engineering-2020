import sys
import csv
import shutil
import os

def main(argv):

    # create the destination folders
    output_folder = "D:\\CavernsLeft3"
    try:
        os.makedirs(output_folder)
    except OSError:
        print("Creation of the directory %s failed" % output_folder)
    affected_file = output_folder + "\\Affected"
    os.makedirs(affected_file)
    unaffected_file = output_folder + "\\Unaffected"
    os.makedirs(unaffected_file)
    sourcefile = "D:\\Test2\\"
    # open and read csv file
    f = open('TrainingSet.csv')
    csv_f = csv.reader(f)
    col = []   # declare list col with no elements
    for row in csv_f:
        col.append(row[1])  # add one item from specified row in the list
    for i in range(65, 71):
        if i < 10:
            j = "00" + str(i)
        elif i < 100:
            j = "0" + str(i)
        elif i < 1000:
            j = str(i)
        source_path = sourcefile + j
        if col[i] == '1':
            out_path = affected_file + "\\" + j
            shutil.move(source_path, out_path)
        elif col[i] == '0':
            out_path = unaffected_file + "\\" + j
            shutil.move(source_path, out_path)
        else:
            print("Error: unknown value at line %s" % i)
            sys.exit()


# call the function to start the program
if __name__ == "__main__":
    main(sys.argv[1:])