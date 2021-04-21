from flask import Flask,request,render_template,jsonify
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/retirement',methods= ['POST'])
def retirement():
  age  = float(request.form['age'])
  salary = float(request.form['salary'])
  percentage  = float(request.form['percentage'])
  goal = float(request.form['goal'])
  annual_savings = (percentage / 100) * salary  # without employer matching
  total_annual_savings = 1.35 * annual_savings  # with 35% employer matching

  # find years
  years = round(goal / total_annual_savings, 2)

  # check if goals can be met
  if (age + years > 100):
      return jsonify({'result': "Your goals can't be met"})
  else:
      return jsonify({'result': "It'll take about {} years to reach your goal".format(years)})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)