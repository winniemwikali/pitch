from app import creat_app,db
from app.models import User
@manage .shell
def make_shell_context():
    return dict(app = app,db = db, User = User)

if __name__ == '__main__':
    manage.run()