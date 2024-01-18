from flask import Flask, render_template, request, redirect, url_for
from Forms import CreateUserForm
import shelve, User

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


# ... Your existing code ...


@app.route('/createUser', methods=['GET', 'POST'])
def create_user():
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'c')
        try:
            users_dict = db['Users']
        except:
            print("Error in retrieving Users from user.db.")
        user = User.User(create_user_form.name.data, create_user_form.email.data,
                         create_user_form.message.data)
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict
        return redirect(url_for('home'))
    return render_template('createUser.html', form=create_user_form)





# @app.route('/thankYou/<int:user_id>')
# def thank_you(user_id):
#     # Retrieve user information from storage based on user_id
#     db = shelve.open('user.db', 'r')
#     users_dict = db.get('Users', {})
#     user = users_dict.get(user_id)
#     db.close()
#
#     # Render the thank_you template with user information
#     if user:
#         return render_template('thank_you.html', user_name=User.User.get_name(self=User.User.get_name()), user_email=User.User.get_email())
#     else:
#         # Handle the case where the user_id is not fou
#         return render_template('error.html', message='User not found')
@app.route('/retrieveUsers')
def retrieve_users():
    users_dict = {}
    db = shelve.open('user.db','r')
    users_dict = db['Users']
    db.close()

    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)
    return render_template('retrieveUsers.html', count=len(users_list), users_list=users_list)
@app.route('/updateUser/<int:id>/', methods=['GET', 'POST'])
def update_user(id):
    update_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and update_user_form.validate():
        db = shelve.open('user.db', 'w')
        users_dict = db['Users']
        user = users_dict.get(id)
        user.set_name(update_user_form.name.data)
        user.set_email(update_user_form.email.data)
        user.set_message(update_user_form.message.data)

        db['Users'] = users_dict
        db.close()
        return redirect(url_for('retrieve_users'))
    else:
        users_dict = {}
        db = shelve.open('user.db', 'r')
        users_dict = db['Users']
        db.close()
        user = users_dict.get(id)
        update_user_form.name.data = user.get_name()
        update_user_form.email.data = user.get_email()
        update_user_form.message.data = user.get_message()
        return render_template('updateUser.html', form=update_user_form)
@app.route('/deleteUser/<int:id>', methods=['POST'])
def delete_user(id):
    users_dict = {}
    db = shelve.open('user.db', 'w')
    users_dict = db['Users']
    users_dict.pop(id)
    db['Users'] = users_dict
    db.close()
    return redirect(url_for('retrieve_users'))





if __name__ == '__main__':
    app.run(debug=True)

