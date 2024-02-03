from pprint import pp
from time import sleep
from flask import Flask, render_template, redirect, flash
from flask_bootstrap import Bootstrap5
from utilities import read_csv, find_shop, add_shop, format_time
from data_structure import CoffeeData, CafeForm

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():

        structure = CoffeeData(coffee_shop=form.coffee_shop.data, location=form.location.data,
                               open_time=format_time(form.open_time.data),
                               close_time=format_time(form.close_time.data),
                               coffee_rank=form.coffee_rank.data, wifi_speed=form.wifi_speed.data,
                               power_outlets=form.power_outlets.data)

        data = read_csv('cafe-data.csv')
        # pp(structure.data_to_dict())
        if not find_shop(data, new_coffee_data=structure.data_to_dict()):
            add_shop('cafe-data.csv', structure.data_to_dict())
            flash('Coffee Shop Added Successfully.', 'success')
        else:
            flash('Duplicate Entry, Discarding.', 'error')

        sleep(2)
        return redirect('/cafes')

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    data = read_csv('cafe-data.csv')
    return render_template('cafes.html', cafes=data)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
