import os
import pickle
import sys
from time import time, sleep

import numpy as np
from github import Github


def run_scraper(github_username, github_password, output_dir):
    print('Collection of data has started.')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    g = Github(github_username, github_password)

    # limts are in raw_headers - https://developer.github.com/v3/#rate-limiting
    count = 0
    prev_time = time()
    for repo in g.get_repos():
        print('-' * 80)
        try:
            rate_limit_remaining = int(repo.raw_headers['x-ratelimit-remaining'])
            print('Rate limit remaining = ', rate_limit_remaining)
            rate_limit_date_reset = int(repo.raw_headers['X-RateLimit-Reset'.lower()])
            if rate_limit_remaining < 100:  # Dangerous zone. Let's not go over the limits.
                time_to_sleep = int(rate_limit_date_reset - time() + 10)
                sleep(time_to_sleep)

            full_name = repo.full_name.replace('/', '-') + '.pkl'
            print(full_name)

            with open(os.path.join(output_dir, full_name), 'wb') as w:
                pickle.dump(repo, w)
                print('count =', count, 'repo =', full_name, 'time elapsed =', np.round(time() - prev_time, 2))
                prev_time = time()
            count += 1
        except Exception as e:
            print('ERROR HAPPENED.')
            print(e)
            pass


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 4:
        print('Help: python3 {0} GITHUB_USERNAME GITHUB_PASSWORD OUTPUT_DIR'.format(args[0]))
        print('Help: python3 {0} tim.cook i_love_apple data/'.format(args[0]))
    else:
        username = args[1]
        password = args[2]
        data_output_dir = args[3]
        print('USERNAME   = {}'.format(username))
        print('PASSWORD   = {}'.format(password[0:2] + len(password[2:-2]) * '*' + password[-2:]))
        print('OUTPUT_DIR = {}'.format(data_output_dir))
        run_scraper(username, password, data_output_dir)
