from app.controllers.user_controller import store, activate_user, get_users, get_user_by_id, delete_user

def init_routes(app):
    @app.route('/users', methods=['GET'])
    def users():
        return get_users()

    @app.route('/users/<int:user_id>', methods=['GET'])
    def user_detail(user_id):
        return get_user_by_id(user_id)

    @app.route('/users/', methods=['POST'])
    def store_user():
        return store()

    @app.route('/users/activate', methods=['POST'])
    def activate_user_route():
        return activate_user()

    @app.route('/users/<int:user_id>', methods=['DELETE'])
    def delete_user_route(user_id):
        return delete_user(user_id)