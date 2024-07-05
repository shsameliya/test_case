from flask import request, jsonify
from flask.views import MethodView
from app import app, db
from app.models import User


#auth file
class User_data(MethodView):
    def post(self):
        print('check user post method')
        try:
            username = request.form.get('username')
            password = request.form.get('password')

            if not username or not password:
                return jsonify({'message': 'username required'}), 400
            
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({'message': 'user created'}), 201
        except Exception as e:
            print(str(e))
            return jsonify({'message': 'error creating user'}), 500
        
    def delete(self):
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            return jsonify({'message': 'username and password required'}), 400
        
        user = User.query.filter_by(username=username).first()
        # if not user or not user.password(password):
        #     return jsonify({'message': 'Invalid username or password'}), 401
        
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'user deleted'}), 200


class LoginAPI(MethodView):
    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            return jsonify({'message': 'Login successful'})
        else:
            return jsonify({'message': 'Invalid credentials'}), 401

class LogoutAPI(MethodView):
    def post(self):
        return jsonify({'message': 'Logout successful'})



#routes
app.add_url_rule('/user', view_func=User_data.as_view('user_api'))
app.add_url_rule('/login', view_func=LoginAPI.as_view('login_api'))
app.add_url_rule('/logout', view_func=LogoutAPI.as_view('logout_api'))
