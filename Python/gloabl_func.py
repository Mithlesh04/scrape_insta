import uuid
import time
from datetime import datetime
import urllib.request
import os.path
import urllib.parse
from pathlib import Path


#generate unique id
def unique_id():
  return '{0}{1}'.format(uuid.uuid4().hex , time.time_ns())


def date_time():
    d = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return d

#downlod img from url
def downloadImg(url,dir=''):
    n = fileNameAndExt(url,True)
    urllib.request.urlretrieve(url, dir+n)
    return n

#get the file name and extension
def fileNameAndExt(url,join=False):
    n = os.path.splitext(os.path.basename(urllib.parse.urlsplit(url).path))
    return  n[0] + n[1] if join else { "name" : n[0] , 'ext' : n[1] }


def create_directory(d='') : 
  Path(d).mkdir(parents=True, exist_ok=True)
  return d


def index_in_list(a_list, index):
    return index < len(a_list)

def delete_local_file(dir) : 
    return Path(dir).unlink()
    

# this is update in all steps during conditions checking
