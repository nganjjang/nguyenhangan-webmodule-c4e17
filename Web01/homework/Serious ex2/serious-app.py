from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def profile(username):
    users = {
        "hangan":   {
                        "Name": "Ha Ngan",
                        "Age": 25,
                        "Gender": "Female",
                        "Hobbies": "food"
                    },
        "kimngan":  {
                        "Name": "Kim Ngan",
                        "Age": 30,
                        "Gender": "Female",
                        "Hobbies": "bar"
                    },
        "quanglam": {
                        "Name": "Quang Lam",
                        "Age": 20,
                        "Gender": "Male",
                        "Hobbies": "gym"
                    },
        "quynhdo":  {
                        "Name": "Quynh Do",
                        "Age": 18,
                        "Gender": "Female",
                        "Hobbies": "sleep"
                    }
    }
    return render_template('index.html', username=username, users=users)

if __name__ == '__main__':
  app.run(debug=True)
