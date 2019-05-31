CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' },
    { 'name': 'Baidu', 'url': 'https://www.baidu.com'}]

#数据库
import os
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')    #数据库文件的路径。
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')            #SQLAlchemy-migrate 数据文件存储在这里。