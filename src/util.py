import sys
from time import time


def print_progress(iteration, total, prefix = '', suffix = '', decimals = 1, bar_length = 100):
    format_str = "{0:." + str(decimals) + "f}"
    percent = format_str.format(100 * (iteration / float(total)))
    filled_length = int(round(bar_length * iteration / float(total)))
    bar = '#' * filled_length + '-' * (bar_length - filled_length)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()


def timeformat(start):
    end = time() - start
    e = int(end)
    return "{:02d}:{:02d}:{:02d}.{:03d}".format(e // 3600, e % 3600 // 60, e % 60, int((end - e) * 1000))