import os
import pickle
import sys
from glob import iglob


def print_repository(repo, i=0):
    print('-' * 80)
    print('ID         = ', i)
    print('URL        = ', repo.html_url)
    print('NAME       = ', repo.name)
    print('WATCH      = ', repo.subscribers_count)
    print('STARTS     = ', repo.watchers_count)
    print('LANGUAGE   = ', repo.language)
    print('FORK       = ', repo.forks)


def read(output_dir):
    glob_pattern = os.path.join(output_dir, '**.pkl')
    print('Search files here:', glob_pattern)
    i = 0
    for file in iglob(glob_pattern):
        with open(file, 'rb') as f:
            repo = pickle.load(f)
            print_repository(repo, i)
            i += 1


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        print('Help: python3 {0} OUTPUT_DIR'.format(args[0]))
        print('Help: python3 {0} data/'.format(args[0]))
    else:
        data_output_dir = args[1]
        print('OUTPUT_DIR = {}'.format(data_output_dir))
        read(data_output_dir)
