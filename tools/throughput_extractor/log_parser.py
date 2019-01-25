
import re
import csv

TIME_INDEX = 2
BYTES_READ_INDEX = 7
DESTINCTION_SIGN = 'driver-heartbeat'

#!!!!! deprecated atm !!!!!!
def extract_throughput_by_time(filename):
    #pattern to match the time (groups 1, 2, and 3) and the number of the bytes read (group 4)
    pattern = re.compile(r'^.*([0-9]{2,2}):([0-9]{2,2}):([0-9]{2,2}).*bytes-read=([0-9]*)')

    throughputs = {}

    with open(filename, 'r') as f:
        for line in f:
            print(line)

            m = pattern.match(line)
            try:
                time = int(m.group(1))*3600 + int(m.group(2))*60 + int(m.group(3))
                throughput = int(m.group(4))
                throughputs[time] = throughput
            except (AttributeError):
                print('the pattern was not matched against this particular line')

    return throughputs

def extract_throughput_by_ms(filename):
    """
    Uses a tgen log file of one particular client to extract the throughputs.
    :param filename: target tgen log file.
    :return:
    """
    throughputs = {}

    with open(filename, 'r') as f:
        for line in f:

            if not DESTINCTION_SIGN in line:
                continue

            parts = line.split()

            time = float(parts[TIME_INDEX])
            size = int(parts[BYTES_READ_INDEX].replace('bytes-read=',''))

            #this sets the granularity of the timestamps to be 100 ms
            throughputs[int(time*10)] = size

    return throughputs

def save_throughputs_to_csv_file(throughputs, filename, labels):
    """
    Saves previously extracted throughputs to csv file named filename.
    Creates first line according to labels list.
    :param throughputs: dictionary with extracted throughputs
    :param filename: name of the target CSV file
    :param labels: list of labels for target CSV file
    :return:
    """
    with open(filename, 'w') as csv_f:
        writer = csv.writer(csv_f)
        writer.writerow(labels)
        for key, value in throughputs.items():
            writer.writerow([key, value])