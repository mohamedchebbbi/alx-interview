#!/usr/bin/python3
'''
Module Log Parsing: script that reads stdin line by line and computes metrics
'''
import sys
from collections import Counter


if __name__ == '__main__':
    # name the file sizes as list and status code as dict
    file_sizes = []
    status_codes = []
    count = 0

    def processline(line, file_sizes, status_codes):
        ''' function to process line to retrieve data '''
        strip_line = line.strip()
        parsed_line = strip_line.split(' ')
        file_size = int(parsed_line[-1])
        status_code = int(parsed_line[-2])

        # append file_size to file_sizes
        file_sizes.append(file_size)

        # append status_code to status_codes
        status_codes.append(status_code)

    def print_metrics(file_sizes, status_codes):
        ''' function to calculate metrics and print them'''
        print(f'File size: {sum(file_sizes)}')

        occ = Counter(status_codes)
        for key, value in sorted(occ.items()):
            if value > 0:
                print(f'{key}: {value}')

    try:
        for line in sys.stdin:
            count += 1
            # process line fn
            processline(line, file_sizes, status_codes)

            # try computing metrics
            try:
                if count % 10 == 0:
                    # print metrics fn
                    print_metrics(file_sizes, status_codes)
            except KeyboardInterrupt:
                # print metrics fn
                print_metrics(file_sizes, status_codes)
    finally:
        print_metrics(file_sizes, status_codes)
