import sqlite3
import click
# current_app is an object pointing to the Flask object making the request
# g is an object for the request (unique),
# it persists throughout the current request (same if get_db called again)
if get_db called
from flask import current_app, g
from falsk.cli import with_appcontext

# establish a connection with the database 
def get_db():
    if 'db' not in g:
        # connect to the DATABASE config key
        g.db = sqlite3.connect(
            current_app.config['DATABASE']
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # returns rows(...) that behave like dicts, allowing row[colName] access
        g.db.row_factory = sqlite3.Row

    return g.db

# close the connection, if it exists
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
