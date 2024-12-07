from flask import Flask,jsonify,request,redirect, url_for,session
from DataController import user,data as D
import re
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users', methods=['GET'])
def get_users():
    users = user.get_all_users()
    return jsonify([{
        'id': user.id,
        'name': user.name,
        'email_id': user.email_id,
        'role_id': user.role_id
    } for user in users])

@app.route('/add_user', methods=['GET','POST'])
def collect_user_input_and_add():
    name = input("Enter name: ")
    email_id = input("Enter email ID: ")
    role = input("Enter role as Bulk/Tankers: ")

    # Validate email format before sending
    if not is_valid_email(email_id):
        return "Invalid email format. Please enter a valid email."
    
    if role == "Bulk":
        role_id = 2
    if role == "Tankers":
        role_id = 3

    # Prepare the data payload
    data = {
        'name': name,
        'email_id': email_id,
        'role_id': role_id
    }
    new_user = user.create_user(data['name'], data['email_id'], data['role_id'])
    return "Congrats {} you have been successfuly registered".format(new_user.name)

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

@app.route('/login', methods=['GET','POST'])
def login_user():
     email_id = input("Enter email ID: ")
     if email_id is not None and is_valid_email:
         user_exist = user.login_auth(email_id)

     if user_exist is not None:
        #  session['role_id'] = user_exist.role_id
         return redirect(url_for('show_data',role_id = user_exist.role_id ))
     else:
         return redirect(url_for('collect_user_input_and_add')), 302

@app.route('/show_data', methods=['GET'])
def show_data():
    print("called show")
    role_id = int(request.args.get('role_id'))
    print(role_id)
    if role_id is None:
        return "Unauthorized", 403  # User not logged in
    
    today = datetime.now().date()  # Get today's date
    yesterday = today - timedelta(days=1) 

    data = D.get_all_data(today)
    if data is None :
       data = D.get_all_data(yesterday)
       
    if role_id == 1:
        # Role 1: Show all data
        # data = D.get_all_data()
        pass
    elif role_id == 2:
        # Role 2: Show only 'bulk' data
        # data = D.fetch_speicfic_data("Bulk")
        data = [d for d in data if d.group_name == 'Bulk']
    elif role_id == 3:
        # Role 3: Show only 'tanker' data
        data = [d for d in data if d.group_name == 'tanker']
    else:
        return "Access denied", 403

    # Convert data to a list of dictionaries for easy JSON response
    data_list = [{
        'data_id': d.data_id,
        'value': d.value
    } for d in data]

    return jsonify(data_list)

if __name__ == '__main__':
    app.run(debug=True)
