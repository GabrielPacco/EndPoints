from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify

from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

from backend.models.task_model import TaskModel

task_blueprint = Blueprint('task_blueprint', __name__)

model = TaskModel()



@task_blueprint.route('/task/add_teacher', methods=['POST'])
@cross_origin()
def create_task_2():
    content = model.add_teacher(request.json['Apellidos'], request.json['Nombres'], request.json['Correo'], request.json['Ciudad'])
    return jsonify(content)

@task_blueprint.route('/task/delete_teacher', methods=['POST'])
@cross_origin()
def delete_task_2():
    return jsonify(model.delete_teacher(int(request.json['CUI'])))

@task_blueprint.route('/task/get_teacher', methods=['POST'])
@cross_origin()
def task_2():
    return jsonify(model.get_teacher(int(request.json['CUI'])))

@task_blueprint.route('/task/get_teachers', methods=['POST'])
@cross_origin()
def tasks_2():
    return jsonify(model.get_teachers())


#############################################

@task_blueprint.route('/task/add_course', methods=['POST'])
@cross_origin()
def create_task_4():
    content = model.add_course(request.json['Nombre'])
    return jsonify(content)

@task_blueprint.route('/task/get_courses', methods=['POST'])
@cross_origin()
def tasks_4():
    return jsonify(model.get_courses())

@task_blueprint.route('/task/delete_course', methods=['POST'])
@cross_origin()
def delete_task_4():
    return jsonify(model.delete_course((request.json['Nombre'])))


#############################################


@task_blueprint.route('/task/add_group', methods=['POST'])
@cross_origin()
def create_task_5():
    content = model.add_group(request.json['Grupo'])
    return jsonify(content)

@task_blueprint.route('/task/get_groups', methods=['POST'])
@cross_origin()
def tasks_5():
    return jsonify(model.get_groups())

@task_blueprint.route('/task/delete_group', methods=['POST'])
@cross_origin()
def delete_task_5():
    return jsonify(model.delete_group((request.json['Grupo'])))

