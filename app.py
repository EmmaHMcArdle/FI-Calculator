from flask import Flask, render_template, request, redirect
from flask.templating import render_template
from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField, SubmitField, DecimalField, validators
from wtforms.validators import DataRequired
from config import secret_key

app = Flask(__name__)

app.config['SECRET_KEY'] = secret_key

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/calculator", methods=['GET', 'POST'])
def calculator():
    form = CalcForm()
    if request.method=="POST":
        a = form.financialGoal.data
        p = form.invested.data
        r = form.annualRate.data
        n = form.compoundFreq.data
        saving = form.oneTimeInvestment.data

        print(a)
        return redirect('/')
    else:
        return render_template("calculator.html", form=form)

class CalcForm(FlaskForm):
    financialGoal = FloatField('Financial Goal', validators=[DataRequired()])
    invested = FloatField('Invested', validators=[DataRequired()])
    annualRate = FloatField("Annual Rate %", validators=[DataRequired()])
    # Do I need data required if automatic default?
    compoundFreq = SelectField('Compound Frequency', choices=[(365, 'Daily (365/year)'), 
                                (360, 'Daily (360/year)'), (52, 'Weekly (52/year)'), 
                                (26, 'Bi-Weekly (26/year)'), (24, 'Semi-Monthly (24/year)'), 
                                (12, 'Monthly (12/year)'), (6, 'Bi-Monthly (6/year)'),
                                (4, 'Quarterly (4/year)'), (2, 'Semi-Annually (2/year)'), (1, 'Annually (1/year)')])
    oneTimeInvestment = FloatField('One-Time Investment')
    continuousInvestment = FloatField("Continuous Investment")
    investmentFreq = SelectField("Investment Frequency", choices=[(365, 'Daily (365/year)'), 
                                (360, 'Daily (360/year)'), (52, 'Weekly (52/year)'), 
                                (26, 'Bi-Weekly (26/year)'), (24, 'Semi-Monthly (24/year)'), 
                                (12, 'Monthly (12/year)'), (6, 'Bi-Monthly (6/year)'),
                                (4, 'Quarterly (4/year)'), (2, 'Semi-Annually (2/year)'), (1, 'Annually (1/year)')])
    annRate = DecimalField("Annual Rate", [validators.NumberRange(min=0, max=10)])
    submit = SubmitField("Calculate Time Saved")



if __name__ == '__main__':
    app.run(debug=True)