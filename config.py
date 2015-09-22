import os
basedir = os.path.abspath(os.path.dirname(__file__))
#print basedir
class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASK_ADMIN = os.environ.get('FLASK_ADMIN')
    @staticmethod
    def init_app(app):
        pass