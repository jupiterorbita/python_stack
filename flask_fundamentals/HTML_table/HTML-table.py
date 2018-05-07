from flask import Flask, render_template
app = Flask(__name__)
print('\n', '--- server start ---')


usersA = (
   {
       'first_name': 'Michael', 'last_name': 'Choi'
    },
   {
       'first_name': 'John', 'last_name': 'Supsupin'
    },
   {'first_name': 'Mark', 'last_name': 'Guillen'},
   {'first_name': 'KB', 'last_name': 'Tonel'}
)

# print(users[0]['first_name'])


def usersprint(xxxx):
    for user in (xxxx):
        print("<td>" + user['first_name'] + "</td>")
        print(user['first_name'])
        print(user['last_name'])
        print("******")


usersprint(usersA)


@app.route('/')
def index():
    print('returing index.html')
    # return render_template('index.html', firstHTML=usersA['first_name'], lastHTML=usersA['last_name'])
    return render_template('index.html', usersHtml=usersA)


# user.first_name

if __name__ == "__main__":
    app.run(debug=True)
