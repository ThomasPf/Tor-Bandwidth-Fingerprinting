
import log_parser
import sys
import argparse
import os
import sys

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--files', nargs='+')
    parser.add_argument('-l', '--labels', nargs='+')
    parser.add_argument('-d', '--directory', nargs=1)
    return parser.parse_args()

if __name__ == '__main__':
    arguments = parse_arguments()
    files = arguments.files
    labels = arguments.labels
    directory = arguments.directory[0]

    print('command line arguments read:')
    print('files to extract from: {}'.format(files))
    print('labels to be used for output: {}'.format(labels))
    print('directory to store the output csv files: {}'.format(directory))

    #make sure that the directory exists
    if not os.path.isdir(directory):
        try:
            os.makedirs(directory)
        except (FileExistsError):
            print("File with name {} exists. Can't create target directory, aborting".format(directory))
            sys.exit(-1)

    for file in files:
        print('Extracting throughputs from file ... {}'.format(file))
        throughputs = log_parser.extract_throughput_by_ms(file)

        csv_filename = directory + '/' + os.path.basename(file) + '.csv'
        print('Writing throughputs into csv file ... {}'.format(csv_filename))
        log_parser.save_throughputs_to_csv_file(throughputs, csv_filename, labels)
