from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify

from App.controllers import (
    init_packages,
    # init_components,
    get_all_packages,
    create_package,
    delete_package
)

package_views = Blueprint('package_views', __name__, template_folder='../templates')


@package_views.route('/api/packages', methods=['GET'])
def getPackages():
    return get_all_packages()

@package_views.route('/api/initpackages', methods=['GET'])
def initPackages():
    return init_packages()


@package_views.route('/api/addpackage', methods=['POST'])
def addPackage():
    data = request.data.decode()
    print(data)
    package = create_package(data)
    return get_all_packages()

@package_views.route('/api/removepackage/<int:package_id>', methods=['DELETE'])
def removePackage(package_id):
    try:
        success = delete_package(package_id)
        if success:
            return jsonify({'message': 'Package deleted successfully'}), 200
        return jsonify({'message': 'Package not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 400
