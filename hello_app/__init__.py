from flask import Flask
app = Flask(__name__)
app.config.from_object('config')    # 获取根目录下面的config文件内容

from hello_app import views,models
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

