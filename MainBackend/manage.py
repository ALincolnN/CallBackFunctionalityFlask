from app import create_app, db
from app.models import *
from flask_migrate import Migrate, upgrade

app = create_app('production')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Transactions': Transcations}


@app.cli.command()
def runserver():
    app.run()


@app.cli.command()
def dbupgrade():
    with app.app_context():
        upgrade()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
