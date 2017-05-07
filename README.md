# Github-full-data-set
Generating GitHub data!

## How to get started?
```
git clone https://github.com/philipperemy/Github-full-data-set.git
cd Github-full-data-set/
sudo pip3 install -r requirements.txt
cat data_100k/x* > data_100k/GITHUB.tar.gz # because GitHub does not allow files bigger than 100Mb.
md5sum data_100k/GITHUB.tar.gz # 5886b24033991283a4dbfa6b328be011  data_100k/GITHUB.tar.gz
tar xvzf data_100k/GITHUB.tar.gz # goes to GITHUB/
```

## Read from pre existing data
```
python3 read.py GITHUB/
```

## Generate your own data
```
python3 main_run_scraper.py <GITHUB_USERNAME> <GITHUB_PASSWORD> GITHUB/
```

## Example of data
```
OUTPUT_DIR = GITHUB/
Search files here: GITHUB/**.pkl
--------------------------------------------------------------------------------
ID         =  0
URL        =  https://github.com/10gen/external
NAME       =  external
WATCH      =  3
STARTS     =  2
LANGUAGE   =  JavaScript
FORK       =  1
--------------------------------------------------------------------------------
ID         =  1
URL        =  https://github.com/4l3x2k/8086macs
NAME       =  8086macs
WATCH      =  2
STARTS     =  0
LANGUAGE   =  C
FORK       =  0
--------------------------------------------------------------------------------
ID         =  2
URL        =  https://github.com/A1kmm/cellml_meta_1_1
NAME       =  cellml_meta_1_1
WATCH      =  2
STARTS     =  3
LANGUAGE   =  None
FORK       =  0
--------------------------------------------------------------------------------
ID         =  3
URL        =  https://github.com/aaronchi/jrails
NAME       =  jrails
WATCH      =  3
STARTS     =  721
LANGUAGE   =  Ruby
FORK       =  82
```

NB: There are way more tags than just those represented above.
Please refer to the links below for a complete documentation of all the available tags.
- https://github.com/PyGithub/PyGithub
- https://github.com/PyGithub/PyGithub/blob/master/github/tests/Repository.py 
