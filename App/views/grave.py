from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt
from datetime import datetime, date

from App.controllers import (
    create_grave, 
    get_all_graves,
    get_grave,
    get_grave_by_plot_num,
    get_grave_by_graveyard,
    get_grave_by_type,
    update_grave,
    delete_grave,
    graves_available,
    graves_unavailable,
    get_graveyard,
    at_max_plots
)

grave_views = Blueprint('grave_views', __name__, template_folder='../templates')

@grave_views.route('/api/graves', methods=['POST'])
@jwt_required()
def create_grave_route():
    jwt = get_jwt()
    if jwt['role'] > 1:
        return jsonify({"message":"Not Authorized"}), 403

    data = request.json
    if not 'plot_num' in data or not 'graveyard_id' in data or not 'grave_type' in data:
        return jsonify({"message":"Missing parameters"}), 400

    graveyard = get_graveyard(data['graveyard_id'])
    if not graveyard.exists:
        return jsonify({"message":"Graveyard does not exist"}), 404
    if at_max_plots(data['graveyard_id']):
        return jsonify({"message":"Graveyard is at maximum plots"}), 400

    if not 'id' in data:
        grave = create_grave(data['plot_num'], data['graveyard_id'], data['grave_type'])
    else:
        grave = get_grave(data['id'])
        if grave.exists:
            return jsonify({"message":"Id already in use"}), 400
        grave = create_grave(data['plot_num'], data['graveyard_id'], data['grave_type'], data['id'])

    return jsonify({"message":"grave Created"}), 201

@grave_views.route('/api/graves', methods=['GET'])
@jwt_required()
def get_graves_route():
    jwt = get_jwt()
    if jwt['role'] > 2:
        return jsonify({"message":"Not Authorized"}), 403
        
    id = request.args.get('id')
    plot_num = request.args.get('plot_num')
    graveyard_id = request.args.get('graveyard_id')
    grave_type = request.args.get('grave_type')

    if id:
        grave = get_grave(id)
        if grave.exists:
            grave_dict = grave.to_dict()
            grave_dict['id'] = grave.id
            return grave_dict, 200
        return jsonify({"message":"grave Not Found"}), 404

    if plot_num:
        graves = get_grave_by_plot_num(int(plot_num))
        if graves:
            graves_array = []
            for grave in graves:
                grave_dict = grave.to_dict()
                grave_dict['id'] = grave.id
                graves_array.append(grave_dict)
            return jsonify(graves_array), 200
        return jsonify({"message":"grave Not Found"}), 404
    
    if graveyard_id:
        graves = get_grave_by_graveyard(graveyard_id)
        if graves:
            graves_array = []
            for grave in graves:
                grave_dict = grave.to_dict()
                grave_dict['id'] = grave.id
                graves_array.append(grave_dict)
            return jsonify(graves_array), 200
        return jsonify({"message":"grave Not Found"}), 404

    if grave_type:
        graves = get_grave_by_type(grave_type)
        if graves:
            graves_array = []
            for grave in graves:
                grave_dict = grave.to_dict()
                grave_dict['id'] = grave.id
                graves_array.append(grave_dict)
            return jsonify(graves_array), 200
        return jsonify({"message":"graves Not Found"}), 404

    graves = get_all_graves()
    graves_array = []
    for grave in graves:
        grave_dict = grave.to_dict()
        grave_dict['id'] = grave.id
        graves_array.append(grave_dict)
    return jsonify(graves_array), 200

@grave_views.route('/api/graves/available', methods=['GET'])
@jwt_required()
def get_available_graves_route():
    jwt = get_jwt()
    if jwt['role'] > 2:
        return jsonify({"message":"Not Authorized"}), 403

    graves = graves_available()
    return jsonify(graves), 200

@grave_views.route('/api/graves/unavailable', methods=['GET'])
@jwt_required()
def get_unavailable_graves_route():
    jwt = get_jwt()
    if jwt['role'] > 2:
        return jsonify({"message":"Not Authorized"}), 403
        
    graves = graves_unavailable()
    return jsonify(graves), 200

@grave_views.route('/api/graves', methods=['PUT'])
@jwt_required()
def update_grave_route():
    jwt = get_jwt()
    if jwt['role'] > 2:
        return jsonify({"message":"Not Authorized"}), 403

    data = request.json
    if not 'id' in data or not 'date' in data:
        return jsonify({"message":"Missing id or date parameter"}), 400
    grave = get_grave(data['id'])
    if grave.exists:
        update_grave(data['id'], datetime.fromisoformat(data['date']))
        return jsonify({"message":"grave updated"}), 200
    return jsonify({"message":"grave not found"}), 404

@grave_views.route('/api/graves', methods=['DELETE'])
@jwt_required()
def delete_grave_route():
    jwt = get_jwt()
    if jwt['role'] > 1:
        return jsonify({"message":"Not Authorized"}), 403

    id = request.args.get('id')
    if not id:
        return jsonify({"message":"Missing id parameter"}), 400
    grave = get_grave(id)
    if grave.exists:
        delete_grave(id)
        return jsonify({"message":"Grave Deleted"}), 200
    return jsonify({"message":"Grave Not Found"}), 404