from flask import Blueprint
from ..controllers.auth_controller import register, login, refresh, user_info

auth_bp = Blueprint('auth_bp', __name__)

auth_bp.route('/register', methods=['POST'])(register)
auth_bp.route('/login', methods=['POST'])(login)
auth_bp.route('/refresh', methods=['POST'])(refresh)
auth_bp.route('/user', methods=['GET'])(user_info)
