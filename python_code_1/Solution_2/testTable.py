from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
import csv
import os
import pysftp
# from dateutil import parser
import re

db_url = {'drivername': 'postgres',
          'username': 'postgres',
          'password': 'password',
          'host': '127.0.0.1',
          'port': 5432}

# database_url = 'postgresql+psycopg2://postgres:password@localhost:5432/mydatabase'
engine = create_engine(URL(**db_url))
# engine = create_engine(database_url)
Base = declarative_base()

class TestTable(Base):
    __tablename__ = 'Test Table'
    id   = Column(Integer, primary_key=True)
    Result_Time  = Column(String, nullable=False)
    Granularity_Period  = Column(String)
    Object_Name = Column(String)
    Cell_ID =  Column(String, unique=True)
    CallAttemps = Column(String)


print('Dropping the tables if they already existed')
Base.metadata.drop_all(engine)
# create tables
print("creating table")
Base.metadata.create_all(bind=engine)

# create session
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# data = {'a': 5566, 'b': 9527, 'c': 183}



cnopts = pysftp.CnOpts()
cnopts.hostkeys = None    


def get_files_sftp(host_address, username, password, remotedir, localdir, preserve_mtime=True):
    sftp=pysftp.Connection(host_address, username=username,password=password,cnopts=cnopts)
    for entry in sftp.listdir(remotedir):
        #download the files of format <FileNo>-TimeStamp.csv
        matchObj = re.match( r'([a-zA-Z]+)-(\d+)-(.*?).csv', entry, re.M|re.I)
        # if entry.endswith(".csv") and parser.parse("2016-10-21 13:45")
        download = False
        if matchObj: 
            remotepath = remotedir + "/" + entry
            localpath = os.path.join(localdir, entry)
            sftp.get(remotepath, localpath, preserve_mtime=preserve_mtime)
            download = True
        
        if download:
            insert_data_to_db(localpath)



def insert_data_to_db(file):

    try:
        # for _key, _val in data.items():
        #     row = TestTable(key=_key, val=_val)
        #     session.add(row)
        # session.commit()
        with open(file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                # print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
                db_row = TestTable(Result_Time = row["Result Time"], Granularity_Period = row["Granularity Period"], Object_Name = row["Object Name"], Cell_ID = row["Cell ID"], CallAttemps = row["CallAttemps"])
                session.add(db_row)
                line_count += 1
            print(f'Processed {line_count} lines.')
        session.commit()
        print("data added to table")
    except SQLAlchemyError as e:
        print(e)
    finally:
        session.close()

host_address = input("enter the remote host ip address")
username = input("enter username")
password = input("enter password")
remote_path=input("enter the remote_path: ")
local_path=input("enter the local_path: ")

get_files_sftp(host_address, username, password, remote_path, local_path, preserve_mtime=True)
# file = 'data.csv'
# insert_data_to_db(file)