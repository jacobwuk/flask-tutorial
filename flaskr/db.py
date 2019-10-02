import sqlite3
# A package that allows us to define command line commands
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


def init_db():
    db = get_db()
    # open schema file (@ path with reference to the current)
    # then read and execute the commands there (ie, create tables from the data)
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

# create a command line command (using Click package bundled in Flask)
@click.command('init_db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    # output to terminal via Click
    click.echo('Initialized the database.')

def init_app(app):
    # link a call to close_db when the context for the app ends
    app.teardown_appcontext(close_db)
    # add an additional command: flask init_db_command
    # can add a comma to specify the name (defaults to the command)
    app.cli.add_command(init_db_command)
