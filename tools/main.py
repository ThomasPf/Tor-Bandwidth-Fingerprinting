
import log_parser
import sys

throughputs = log_parser.extract_throughput_by_ms(sys.argv[1])

print(throughputs)