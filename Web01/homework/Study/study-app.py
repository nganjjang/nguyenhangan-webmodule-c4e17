from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/about-me')
def index():
    post ={
    "title": "Ngân Ngân's page",
    "say_hi": "Welcome to my page!!!",
    "name": "I am Ngân Ngân",
    "work": "Đang làm việc ở Vietnam Airlines",
    "school": "Đã từng học ở mái trường NEU",
    "hobbies": "Thích ngủ, ngủ, ngủ",
    "dog": "Muốn nuôi một em chó shiba inu >.<"
    }

    return render_template('index.html', post=post)

@app.route('/school')
def school():
    return redirect('http://techkids.vn')

if __name__ == '__main__':
  app.run(debug=True)
