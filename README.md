
# Simple youtube mp3-converter 

## General info
This project is simple mp3-converter , analog of https://github.com/GarryGon4ar/mp3-converter, but running asynchronous. Paste link of your video in the form and download mp3 file.

## REQUIREMENTS

This App Uses Python 3.6, Django 2.2.1, youtube-dl.

## INSTALLATION

To clone and run this repository, you'll need Git installed on your computer. I used virtualenv for this project, you may feel free to use the same. From your command line:

```
$ git clone https://github.com/GarryGon4ar/youtube_mp3.git
$ virtualenv sample_environment -p python3
$ source sample_environment/bin/activate
$ cd youtube_mp3
$ pip install -r requirements.txt
$ python manage.py runsever

# run workers
$ celery -A youtubedll worker -l info