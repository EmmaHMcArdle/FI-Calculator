from flask import Flask, render_template
from flask.templating import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/calculator")
def calculator():
    return render_template("one_time.html")

@app.route("/reoccuring_calculator")
def reoccuring_calculator():
    return render_template("reoccuring_calc.html")

class OneTimeForm(FlaskForm):
    financialGoal = FloatField('Finacial Goal', validators=[DataRequired()])
    currentlyInvested = FloatField('Invested', validators=[DataRequired()])
    annualRate = FloatField("Annual Rate", validators=[DataRequired()])
    # Do I need data required if automatic default?
    compoundFrequency = SelectField('Compound Frequency', choices=[(365, 'Daily (365/year)'), 
                                    (360, 'Daily (360/year)'), (52, 'Weekly (52/year)'), 
                                    (26, 'Bi-Weekly (26/year)'), (24, 'Semi-Monthly (24/year)'), 
                                    (12, 'Monthly (12/year)'), (6, 'Bi-Monthly (6/year)'),
                                    (6, 'Bi-Monthly (6/year)'), (4, 'Quarterly (4/year)'),
                                    (2, 'Semi-Annually (2/year)'), (1, 'Annually (1/year)')])
    oneTimeInvestment = FloatField('One Time Investment', validators=[DataRequired()])
    submit = SubmitField("Calculate Time Saved")

if __name__ == '__main__':
    app.run(debug=True)