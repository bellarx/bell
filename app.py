from flask import Flask,request,render_template,jsonify
from configurations import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process',methods= ['POST'])
def process():
  weight  = float(request.form['weight'])
  height = float(request.form['height'])
  weight=0.45* float(weight)
  height=0.025* float(height)
  name = str(request.form['name'])
  output = str(weight / (height*height))
  bmi =float(output)
  if bmi <=18.5:
    return jsonify({'output': name + ' You are Under weight, your bmi is: ' + output})
  elif (bmi >=18.5) and (bmi <=24.9):
    return jsonify({'output': name + ' Perfect! You have normal weight and your bmi is : '+ output})
  elif bmi >=25 and bmi <=29.9:
   return jsonify({'output': name + ' You are Overweight, your bmi is: ' + output})
  elif bmi>=30:
   return jsonify({'output': name + ' You are highly obese, your bmi is: ' + output})
  else :
   return jsonify({'output': 'and your bmi is : '+ output})
  return jsonify({'error' : name + ' There is some Missing data!'})

@app.route('/retirement',methods= ['POST'])
def retirement():
  age  = float(request.form['age'])
  salary = float(request.form['salary'])
  percentage  = float(request.form['percentage'])
  goal = float(request.form['goal'])
  name = str(request.form['name'])
  annual_savings = (percentage / 100) * salary  # without employer matching
  total_annual_savings = 1.35 * annual_savings  # with 35% employer matching

  # find years
  years = round(goal / total_annual_savings, 2)

  # check if goals can be met
  if (age + years > 100):
      return jsonify({'result': name +" Your goals can't be met"})
  else:
      return jsonify({'result': name + " It'll take you about {} years to reach your goal".format(years)})

@app.route('/test')
def test():
    return "Works!"


if __name__ == "__main__":
    app.run()