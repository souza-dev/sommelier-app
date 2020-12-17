import joblib
import os 

from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import FloatField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY']='wP4xQ8hUljJ5oI1c'
bootstrap = Bootstrap(app)

class InputForm(FlaskForm):
    alcohol = FloatField('Alcohol', validators=[DataRequired()])
    malic_acid = FloatField('Malic acid', validators=[DataRequired()])
    ash = FloatField('Ash', validators=[DataRequired()])
    alcalinity_of_ash = FloatField('Alcalinity of ash', validators=[DataRequired()])
    magnesium = FloatField('Magnesium', validators=[DataRequired()])
    total_phenols = FloatField('Total phenols', validators=[DataRequired()])
    flavanoids = FloatField('Flavanoids', validators=[DataRequired()])
    nonflavanoid_phenols = FloatField('Nonflavanoid phenols', validators=[DataRequired()])
    proanthocyanins = FloatField('Proanthocyanins', validators=[DataRequired()])
    color_intensity = FloatField('Color intensity', validators=[DataRequired()])
    hue = FloatField('Hue', validators=[DataRequired()])
    od280 = FloatField('OD280/OD315 of diluted wines', validators=[DataRequired()])
    proline = FloatField('Proline', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
    form   = InputForm(request.form)
    wine_class = 'Unknow'
    if form.validate_on_submit():
       x = [[form.alcohol.data, form.malic_acid.data, form.ash.data, form.alcalinity_of_ash.data, form.magnesium.data, form.total_phenols.data, form.flavanoids.data, form.nonflavanoid_phenols.data, form.proanthocyanins.data, form.color_intensity.data, form.hue.data, form.od280.data, form.proline.data]]
       wine_class = make_prediction(x)
    
    return render_template('index.html', form=form, wine_class=wine_class)

def make_prediction(x):
    filename = os.path.join('model', 'finalized.sav')
    model = joblib.load(filename)
    return model.predict(x)[0]