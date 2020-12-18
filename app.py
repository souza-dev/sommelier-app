import joblib
import os 

from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import FloatField
from wtforms.validators import DataRequired, NumberRange

app = Flask(__name__)
app.config['SECRET_KEY']='wP4xQ8hUljJ5oI1c'
bootstrap = Bootstrap(app)

class InputForm(FlaskForm):
    alcohol = FloatField('Alcohol', validators=[DataRequired(), NumberRange(min=11, max=14, message='The value must be between 11 and 14')])
    malic_acid = FloatField('Malic acid', validators=[DataRequired(), NumberRange(min=0.5, max=6, message='The value must be between 0.5 and 6')])
    ash = FloatField('Ash', validators=[DataRequired(), NumberRange(min=1, max=4, message='The value must be between 1 and 4')])
    alcalinity_of_ash = FloatField('Alcalinity of ash', validators=[DataRequired(), NumberRange(min=10, max=35, message='The value must be between 10 and 35')])
    magnesium = FloatField('Magnesium', validators=[DataRequired(), NumberRange(min=60, max=170, message='The value must be between 60 and 170')])
    total_phenols = FloatField('Total phenols', validators=[DataRequired(), NumberRange(min=0.5, max=4, message='The value must be between 0.5 and 4')])
    flavanoids = FloatField('Flavanoids', validators=[DataRequired(), NumberRange(min=0, max=6, message='The value must be between 0 and 6')])
    nonflavanoid_phenols = FloatField('Nonflavanoid phenols', validators=[DataRequired(), NumberRange(min=0, max=1, message='The value must be between 0 and 1')])
    proanthocyanins = FloatField('Proanthocyanins', validators=[DataRequired(), NumberRange(min=0, max=5, message='The value must be between 0 and 5')])
    color_intensity = FloatField('Color intensity', validators=[DataRequired(), NumberRange(min=1, max=15, message='The value must be between 1 and 15')])
    hue = FloatField('Hue', validators=[DataRequired(), NumberRange(min=0, max=2, message='The value must be between 0 and 2')])
    od280 = FloatField('OD280/OD315 of diluted wines', validators=[DataRequired(), NumberRange(min=1, max=5, message='The value must be between 1 and 5')])
    proline = FloatField('Proline', validators=[DataRequired(), NumberRange(min=200, max=1700, message='The value must be between 200 and 1700')])

@app.route('/', methods=['GET', 'POST'])
def index():
    form   = InputForm(request.form)
    wine_class = 'unknow'
    if form.validate_on_submit():
       x = [[form.alcohol.data, form.malic_acid.data, form.ash.data, form.alcalinity_of_ash.data, form.magnesium.data, form.total_phenols.data, form.flavanoids.data, form.nonflavanoid_phenols.data, form.proanthocyanins.data, form.color_intensity.data, form.hue.data, form.od280.data, form.proline.data]]
       wine_class = make_prediction(x)
    
    return render_template('index.html', form=form, wine_class=wine_class)

def make_prediction(x):
    filename = os.path.join('model', 'finalized.sav')
    model = joblib.load(filename)
    return model.predict(x)[0]