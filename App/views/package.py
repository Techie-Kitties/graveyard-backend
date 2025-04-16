from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify

from App.controllers import (
    init_packages,
    # init_components,
    get_all_packages,
    create_package,
    delete_package
)
from App.models import Package
from App.models.customPackage import customPackage
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required, get_jwt_identity

package_views = Blueprint('package_views', __name__, template_folder='../templates')


@package_views.route('/api/packages', methods=['GET'])
def getPackages():
    return get_all_packages()

@package_views.route('/api/addpackage', methods=['POST'])
@cross_origin(supports_credentials=True)
@jwt_required()
def addPackage():
    data = request.data.decode()
    package = create_package(data)
    if (package):
        print("package added successfully")
    return get_all_packages()


@package_views.route('/api/removepackage/<int:package_id>', methods=['DELETE'])
@cross_origin(supports_credentials=True)
@jwt_required()
def removePackage(package_id):
    try:
        success = delete_package(package_id)
        if success:
            return jsonify({'message': 'Package deleted successfully'}), 200
        return jsonify({'message': 'Package not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@package_views.route('/package/init', methods=['POST'])
@cross_origin(supports_credentials=True)
@jwt_required()
def init_package():
    package = customPackage.get_instance()
    return jsonify({
        "message": "Package initialized successfully.",
        "package": package.get_json()
    }), 201


@package_views.route('/api/setCustomPrices', methods=['POST'])
@cross_origin(supports_credentials=True)
@jwt_required()
def set_custom_prices():
    package = customPackage.get_instance()

    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data provided"}), 400

        package.update(data)

        return jsonify({
            "message": "Custom package prices updated successfully.",
            "package": package.get_json()
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@package_views.route('/api/getCustomPrices', methods=['GET'])
def get_custom_prices():
    package = customPackage.get_instance()
    return jsonify({
        "package": package.get_json()
    }), 200


@package_views.route('/api/package/edit', methods=['PUT'])
@cross_origin(supports_credentials=True)
@jwt_required()
def edit_package():
    user = get_jwt_identity()
    # print(user)
    data = request.get_json()
    # print(data.get("name"))
    package = Package.query.filter_by(id=data.get("id")).first()
    # print(package.body_preparation)
    package.update_from_json(data)
    return jsonify({
        "message": "Package updated successfully.",
        "package": package.get_json()
    }), 200
