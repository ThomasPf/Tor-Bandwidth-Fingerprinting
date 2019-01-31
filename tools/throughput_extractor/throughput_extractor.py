
import log_parser
import sys
import argparse
import os
import sys

DEFAULT_LABELS = ['timestamp', 'value']
DEFAULT_DIRECTORY = ['extracted_throughputs/setup/']
DEFAULT_FILES = ['shadow.data/hosts/adversaryclient/stdout-adversaryclient.tgen.1001.log', 'shadow.data/hosts/victimclient/stdout-victimclient.tgen.1001.log']

def parse_arguments():
    parser = argparse.ArgumentParser(description='Shadow throughput extractor script. Extracts throughput values'
                        ' from tgen log files based on heartbeat messages and saves data into csv file format.'
                        ' Created as a part of Blockchain Engineering'
                        ' course project at TU Delft during 2018/2019')
    
    parser.add_argument('-f', '--files', nargs='+', default=DEFAULT_FILES, 
                        help='specify the tgen log files for the throughput'
                        ' extraction. Delimited by spaces.\nDefault value: ' + str(DEFAULT_FILES))
    parser.add_argument('-l', '--labels', nargs='+', default=DEFAULT_LABELS, 
                        help='specify the labels for values in generated .csv files. Delimited by spaces.'
                        '\nDefault value: ' + str(DEFAULT_LABELS))
    parser.add_argument('-d', '--directory', nargs=1, default=DEFAULT_DIRECTORY, 
                        help='specify the directory for csv output storage. The target '
                        'csv files are stored in the path relative to directory where the'
                        ' extraction is run. The names of the csv files stored in the target'
                        ' directory are in form /{original_tgen_log_filename/}.csv\n'
                        'Default value: ' + str(DEFAULT_DIRECTORY))
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

