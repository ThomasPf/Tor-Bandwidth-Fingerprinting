
import re

TIME_INDEX = 2
BYTES_READ_INDEX = 7

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
    throughputs = {}

    with open(filename, 'r') as f:
        for line in f:

            if not 'driver-heartbeat' in line:
                continue

            parts = line.split()

            time = float(parts[TIME_INDEX])
            size = int(parts[BYTES_READ_INDEX].replace('bytes-read=',''))

            throughputs[int(time*10)] = size

    return throughputs