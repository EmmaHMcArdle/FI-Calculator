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
        # Turn from unicode (from .data) to string
        goal = str(form.financialGoal.data)
        principal = form.invested.data
        annualRate = form.annualRate.data
        compFreq = form.compoundFreq.data
        # Grab the value from the SelectField to pass into Results
        nFreqLabel = dict(form.compoundFreq.choices).get(int(compFreq))
        oneTimeSaving = form.oneTimeInvestment.data
        contSaving = form.continuousInvestment.data
        if contSaving != None:
            freq = form.investmentFreq.data
            # Get the invest frequency label to pass into HTML in results
            investFreqLabel = dict(form.investmentFreq.choices).get(int(freq))
         
         # Calculate original timeline 
        originalTimelineInYears = calculations.calcTimeline(float(goal),float(principal),float(compFreq),float(annualRate))
        originalTimelineStr = calculations.yearsToTotal(originalTimelineInYears)
        
        
        # Depending on whether or not adding a one time or continuous payment
        if oneTimeSaving != None and contSaving != None:
            postSavingsTimelineInDays = calculations.continuousPaymentTimeline(float(goal),float(float(principal)+float(oneTimeSaving)),float(compFreq),float(annualRate), float(contSaving), int(freq))
            postSavingsTimelineStr = calculations.daysToTotal(postSavingsTimelineInDays)
            postSavingsTimelineInYears = calculations.daysToYears(postSavingsTimelineInDays)
            differenceInTime = calculations.calculate_diff(originalTimelineInYears, postSavingsTimelineInYears)
        elif oneTimeSaving != None:
            postSavingsTimelineInYears = calculations.calcTimeline(float(goal),float(float(principal)+float(oneTimeSaving)),float(compFreq),float(annualRate))
            postSavingsTimelineStr = calculations.yearsToTotal(postSavingsTimelineInYears)
            differenceInTime = calculations.calculate_diff(originalTimelineInYears, postSavingsTimelineInYears)
        elif contSaving != None:
            postSavingsTimelineInDays = calculations.continuousPaymentTimeline(float(goal),float(principal),float(compFreq),float(annualRate), float(contSaving), int(freq))
            postSavingsTimelineStr = calculations.daysToTotal(postSavingsTimelineInDays)
            postSavingsTimelineInYears = calculations.daysToYears(postSavingsTimelineInDays)
            differenceInTime  = calculations.calculate_diff(originalTimelineInYears, postSavingsTimelineInYears)
        else:
            postSavingsTimelineStr = None
            differenceInTime = None
        return render_template("calculator.html", form=form, goal=goal, principal=principal, 
                            annualRate=annualRate, nFreqLabel=nFreqLabel, originalTimelineStr=originalTimelineStr,
                            originalTimelineInYears=round(originalTimelineInYears, 2), 
                            postSavingsTimelineStr=postSavingsTimelineStr, differenceInTime = differenceInTime,
                            oneTimeSaving=oneTimeSaving, contSaving=contSaving, investFreqLabel=investFreqLabel)
    else:
        return render_template("calculator.html", form=form)



if __name__ == '__main__':
    app.run(debug=True)