
def create_app()
app = Flask(__name__)
app.config.from_objects(Config)