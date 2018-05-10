from flask import Flask, render_template
app = Flask(__name__)

@app.route('/bmi/<float:weight>/<float:height>')
def bmi(weight, height):
    bmi = weight / (height / 100) ** 2

    if bmi < 16:
        return "BMI = {0} - Severely underweight".format(bmi)
    elif 16 <= bmi < 18.5:
        return "BMI = {0} - Underweight".format(bmi)
    elif 18.5 <= bmi < 25:
        return "BMI = {0} - Normal".format(bmi)
    elif 25 <= bmi < 30:
        return "BMI = {0} - Overweight".format(bmi)
    elif bmi > 30:
        return "BMI = {0} - Obese".format(bmi)


@app.route('/bmi2/<float:weight>/<float:height>')
def bmi2(weight, height):
    bmi = weight / (height / 100) ** 2
    return render_template('index.html', bmi=bmi)

if __name__ == '__main__':
  app.run(debug=True)
