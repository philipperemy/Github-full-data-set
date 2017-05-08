import pickle
from glob import iglob

HEADERS = ['name',
           'clone_url',
           'created_at',
           'forks',
           'has_issues',
           'language',
           'subscribers_count',
           'watchers_count',
           'stargazers_count',
           'size']

DIR = 'data_1m/GITHUB/'


def repo_to_txt(rep):
    r_values = []
    for field in HEADERS:
        r_values.append(str(rep.raw_data[field]))
    return r_values


if __name__ == '__main__':
    sep = '\t'
    count = 0
    with open('output.txt', 'w') as w:
        w.write(sep.join(HEADERS) + '\n')
        for filename in iglob(DIR + '*.pkl', recursive=False):
            try:
                with open(filename, 'rb') as f:
                    repo = pickle.load(f)
                    values = repo_to_txt(repo)
                    w.write(sep.join(values) + '\n')
                    count += 1
                    if count % 100 == 0:
                        print(count)
            except EOFError:
                print('ERROR. SKIPPING.')
