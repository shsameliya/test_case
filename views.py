# from app import User
from models import User
from app import app, db
from flask import request, jsonify, make_response


@app.route('/', methods=['GET'])
def hello():
    return "Hello, World!"


@app.route('/test', methods=['GET'])
def test():
  print('check test...')
  return make_response(jsonify({'message': 'test endpoint'}), 200)


@app.route('/users', methods=['POST'])
def create_user():
    print('check user post method')
    try:
      username = request.form.get('username')
      email = request.form.get('email')

      if not username or not email:
        return make_response(jsonify({'message': 'username and email are required'}), 400)

      new_user = User(username=username, email=email)
      db.session.add(new_user)
      db.session.commit()
      return make_response(jsonify({'message': 'user created'}), 201)
    except Exception as e:
      print(str(e))
      return make_response(jsonify({'message': 'error creating user'}), 500)


@app.route('/users', methods=['GET'])
def get_users():
  try:
    users = User.query.all()
    return make_response(jsonify([user.json() for user in users]), 200)
  except Exception as e:
    print(str(e))
    return make_response(jsonify({'message': 'error getting users'}), 500)


@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
  try:
    user = User.query.filter_by(id=id).first()
    if user:
      return make_response(jsonify({'user': user.json()}), 200)
    return make_response(jsonify({'message': 'user not found'}), 404)
  except Exception as e:
    print(str(e))
    return make_response(jsonify({'message': 'error getting user'}), 500)


@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
  try:
    user = User.query.filter_by(id=id).first()
    if user:
      user.username = request.form.get('username')
      user.email = request.form.get('email')
      db.session.commit()
      return make_response(jsonify({'message': 'user updated'}), 200)
    return make_response(jsonify({'message': 'user not found'}), 404)
  except Exception as e:
    print(str(e))
    return make_response(jsonify({'message': 'error updating user'}), 500)


@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
  try:
    user = User.query.filter_by(id=id).first()
    if user:
      db.session.delete(user)
      db.session.commit()
      return make_response(jsonify({'message': 'user deleted'}), 200)
    return make_response(jsonify({'message': 'user not found'}), 404)
  except Exception as e:
    print(str(e))
    return make_response(jsonify({'message': 'error deleting user'}), 500)