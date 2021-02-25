from decimal import DefaultContext
from flask import Flask, render_template, request, redirect, url_for, session
from flask.templating import render_template
from flask_wtf import FlaskForm
from wtforms import Form, Field, SelectField, SubmitField, DecimalField, validators, FloatField
from wtforms.validators import DataRequired
from config import secret_key
import calculations 

app = Flask(__name__)

app.config['SECRET_KEY'] = secret_key

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

class MyFloatField(FloatField):
    def process_formdata(self, valuelist):
        if valuelist:
            try:
                self.data = float(valuelist[0].replace(',', '').replace("$", ""))
            except ValueError:
                self.data = None
                raise ValueError(self.gettext('Not a valid float value'))

class CalcForm(FlaskForm):
    financialGoal = MyFloatField('Financial Goal', validators=[DataRequired()])
    invested = MyFloatField('Currently Invested', validators=[DataRequired()])
    annualRate = DecimalField("Annual Rate %", validators=[DataRequired()])
    # Do I need data required if automatic default?
    compoundFreq = SelectField('Compound Frequency', choices=[(365, 'Daily (365/year)'), 
                                (360, 'Daily (360/year)'), (52, 'Weekly (52/year)'), 
                                (26, 'Bi-Weekly (26/year)'), (24, 'Semi-Monthly (24/year)'), 
                                (12, 'Monthly (12/year)'), (6, 'Bi-Monthly (6/year)'),
                                (4, 'Quarterly (4/year)'), (2, 'Semi-Annually (2/year)'), (1, 'Annually (1/year)')], default=12)
    oneTimeInvestment = MyFloatField('One-Time Investment')
    continuousInvestment = MyFloatField('Continuous Investment')
    investmentFreq = SelectField("Investment Frequency", choices=[(365, 'Daily (365/year)'), 
                                (360, 'Daily (360/year)'), (52, 'Weekly (52/year)'), 
                                (26, 'Bi-Weekly (26/year)'), (24, 'Semi-Monthly (24/year)'), 
                                (12, 'Monthly (12/year)'), (6, 'Bi-Monthly (6/year)'),
                                (4, 'Quarterly (4/year)'), (2, 'Semi-Annually (2/year)'), (1, 'Annually (1/year)')], default=12)
    submit = SubmitField("Calculate Time Saved")

@app.route("/calculator", methods=['GET', 'POST'])
def calculator():
    form = CalcForm()
    form.investmentFreq.process_data(12)
    if request.method=="POST":
        session['Goal'] = str((form.financialGoal.data))
        session['Principal'] = str(form.invested.data)
        session['Annual Rate'] = str(form.annualRate.data)
        session['Compound Frequency'] = form.compoundFreq.data
        oneTimeSaving = form.oneTimeInvestment.data
        if oneTimeSaving != None:
            session['One Time Savings'] = str(oneTimeSaving)
            print(session['One Time Savings'])
        contSaving = form.continuousInvestment.data
        if contSaving != None:
            session['Continuous Savings'] = str(contSaving)
            freq = form.investmentFreq.data
            session['Investment Frequency'] = freq
        return redirect(url_for('results'))
    else:
        return render_template("calculator.html", form=form)

@app.route("/results")
def results():
    a = session.get('Goal', None)
    p = session.get('Principal', None)
    r = session.get('Annual Rate', None)
    n = session.get('Compound Frequency', None)
    oneTimeSaving = session.get('One Time Savings', None)
    contSaving = session.get("Continuous Savings", None)
    freq = session.get("Investment Frequency", None)
    print("frequency: " + freq)
    if oneTimeSaving != None and contSaving != None:
        after = calculations.continuousPaymentTimeline(float(a),float(float(p)+float(oneTimeSaving)),float(n),float(r), float(contSaving), int(freq))
        afterTimelineStr = calculations.daysToTotal(after)
        after = calculations.daysToYears(after)
    elif oneTimeSaving != None:
        after = calculations.calcTimeline(float(a),float(float(p)+float(oneTimeSaving)),float(n),float(r))
        afterTimelineStr = calculations.yearsToTotal(after)
    elif contSaving != None:
        after = calculations.continuousPaymentTimeline(float(a),float(p),float(n),float(r), float(contSaving), int(freq))
        afterTimelineStr = calculations.daysToTotal(after)
        after = calculations.daysToYears(after)
    else:
        afterTimelineStr = None
    original = calculations.calcTimeline(float(a),float(p),float(n),float(r))
    timelineStr = calculations.yearsToTotal(original)
    diff = calculations.calculate_diff(original, after)
    return render_template("results.html", a=a, p=p, r=r, n=n, 
                            timelineStr=timelineStr, original=round(original, 2), 
                            after=round(after, 2), afterTimelineStr=afterTimelineStr, diff = diff)


if __name__ == '__main__':
    app.run(debug=True)