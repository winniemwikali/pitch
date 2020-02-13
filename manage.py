from app import creat_app,db
from app.models import User
app = create_app('production')
manager = Manager(app)
manager.add_command('server',Server)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)
@manage .shell
def make_shell_context():
    return dict(app = app,db = db, User = User)

if __name__ == '__main__':
    manage.run()