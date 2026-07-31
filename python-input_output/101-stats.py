#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""
import sys


def print_stats(stats, file_size):
    """Prints accumulative metrics and statistics."""
    print("File size: {}".format(file_size))
    for key in sorted(stats.keys()):
        if stats[key] > 0:
            print("{}: {}".format(key, stats[key]))


if __name__ == "__main__":
    file_size = 0
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            data = line.split()

            try:
                file_size += int(data[-1])
            except (IndexError, ValueError):
                pass

            try:
                code = data[-2]
                if code in status_codes:
                    status_codes[code] += 1
            except IndexError:
                pass

            if line_count % 10 == 0:
                print_stats(status_codes, file_size)

        print_stats(status_codes, file_size)

    except KeyboardInterrupt:
        print_stats(status_codes, file_size)
        raise
