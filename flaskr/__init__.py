import os
from flask import Flask

# application factory function
def create_app(test_config=None):
    # create flask instance
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the "default" instance config, if it exists
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the provided config
        app.config.from_mapping(test_config)

    # ensure the app.instance_path exists, as Flask does not create this
    # The SQLite database will get put there
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # as a tutorial, this is the legally-mandated example
    @app.route('/hello')
    def hello():
        return 'Hello, World'

    return app
