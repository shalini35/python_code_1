
import os
import pysftp
# from dateutil import parser
import re


cnopts = pysftp.CnOpts()
cnopts.hostkeys = None    
sftp=pysftp.Connection('192.168.X.X', username='username',password='password',cnopts=cnopts)

def get_files_sftp(sftp, remotedir, localdir):
    for entry in sftp.listdir(remotedir):
        #download the files of format <FileNo>-TimeStamp.csv
        matchObj = re.match( r'([a-zA-Z]+)-(\d+)-(.*?).csv', entry, re.M|re.I)
        # if entry.endswith(".csv") and parser.parse("2016-10-21 13:45")
        if matchObj: 
            remotepath = remotedir + "/" + entry
            localpath = os.path.join(localdir, entry)
            sftp.get(remotepath, localpath, preserve_mtime=preserve_mtime)

remote_path=input("enter the remote_path: ")
local_path=input("enter the local_path: ")

get_r_portable(sftp, remote_path, local_path, preserve_mtime=True)



