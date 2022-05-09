import sqlite3
import os

BUILD = './data/db/build.sql'
DB = './data/db/main.sql'

def commit(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        commit()

    return inner

@commit
def build():
    if isfile(BUILD):
        scriptexec(BUILD)

def execute(command, *values):
    cur.execute(command, tuple(values))

def multiexecute(command, valueset):
    cur.executemany(command, valueset)

def column(command, *values):
    cur.execute(command, tuple(values))

    try:
        return [item[0] for item in cur.fetchall()]

    finally:
        pass
    
def field(command, *values):
    cur.execute(command, tuple(values))

    if (fetch := cur.fetchone()) is not None:
        return fetch[0]

def record(command, *values):
    cur.execute(command, tuple(values))

    return cur.fetchone()

def records(command, *values):
    cur.execute(command, tuple(values))

    return cur.fetchall()

def scriptexecute(path):
    with open(path, "r", encoding="utf-8") as script:
        cur.executescript(script.read())

def commit():
    cxn.commit()

def close():
    cxn.close()