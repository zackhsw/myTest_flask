from flask import Flask, request, abort, jsonify
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# from flask_restful import  reqparse, abort,Api, Rsource
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'

# api = Api(app)
#
#
# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}


# api.add_resource(HelloWorld, '/')

# 简单restful实现
tasks = [{'aainfo': '测试数据 jack数据？'}]


@app.route('/test')
def hello_world():
    a_var = 'new start----end two shell 自动构建v 行不行'
    return 'Hello Jack,welcome {}!'.format(a_var)


@app.route('/add_task/', methods=['POST'])
def add_task():
    if not request.json or 'id' not in request.json or 'info' not in request.json:
        abort(400)
    task = {
        'id': request.json['id'],
        'info': request.json['info']
    }
    tasks.append(task)
    return jsonify({'result': 'success'})


@app.route('/get_task/', methods=['GET'])
def get_task():
    if not request.args or 'id' not in request.args:
        return jsonify(tasks)
    else:
        task_id = request.args['id']
        task = filter(lambda t: t['id'] == int(task_id), tasks)
        return jsonify(task) if task else jsonify({'result': 'not found'})


def create_app(config_class=Config):
    app = Flask(__name__)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')


from app import routes, models
