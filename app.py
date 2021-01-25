from flask import Flask, render_template, request, redirect, url_for, session
from flask.templating import render_template
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, DecimalField, validators
from wtforms.validators import DataRequired
from config import secret_key
import calculations 

app = Flask(__name__)

app.config['SECRET_KEY'] = secret_key

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

class CalcForm(FlaskForm):
    financialGoal = DecimalField('Financial Goal', validators=[DataRequired()])
    invested = DecimalField('Invested', validators=[DataRequired()])
    annualRate = DecimalField("Annual Rate %", validators=[DataRequired()])
    # Do I need data required if automatic default?
    compoundFreq = SelectField('Compound Frequency', choices=[(365, 'Daily (365/year)'), 
                                (360, 'Daily (360/year)'), (52, 'Weekly (52/year)'), 
                                (26, 'Bi-Weekly (26/year)'), (24, 'Semi-Monthly (24/year)'), 
                                (12, 'Monthly (12/year)'), (6, 'Bi-Monthly (6/year)'),
                                (4, 'Quarterly (4/year)'), (2, 'Semi-Annually (2/year)'), (1, 'Annually (1/year)')])
    oneTimeInvestment = DecimalField('One-Time Investment')
    continuousInvestment = DecimalField("Continuous Investment")
    investmentFreq = SelectField("Investment Frequency", choices=[(365, 'Daily (365/year)'), 
                                (360, 'Daily (360/year)'), (52, 'Weekly (52/year)'), 
                                (26, 'Bi-Weekly (26/year)'), (24, 'Semi-Monthly (24/year)'), 
                                (12, 'Monthly (12/year)'), (6, 'Bi-Monthly (6/year)'),
                                (4, 'Quarterly (4/year)'), (2, 'Semi-Annually (2/year)'), (1, 'Annually (1/year)')])
    submit = SubmitField("Calculate Time Saved")

@app.route("/calculator", methods=['GET', 'POST'])
def calculator():
    form = CalcForm()
    if request.method=="POST":
        a = form.financialGoal.data
        session['Goal'] = a
        p = form.invested.data
        session['Principal'] = p
        r = form.annualRate.data
        session['Annual Rate'] = r
        n = form.compoundFreq.data
        session['Compound Frequency'] = n
        oneTimeSaving = form.oneTimeInvestment.data
        session['One Time Savings'] = oneTimeSaving
        contSaving = form.continuousInvestment.data
        session['Continuous Savings'] = contSaving
        freq = form.investmentFreq.data
        session['Investment Frequency'] = freq
        # if saving != None:
            
        return redirect(url_for('results'))
    else:
        return render_template("calculator.html", form=form)

@app.route("/results")
def results():
    a = session.get('Goal', None)

    return render_template("results.html")


if __name__ == '__main__':
    app.run(debug=True)