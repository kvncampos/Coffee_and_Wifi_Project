from dataclasses import dataclass
from pprint import pp
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, TimeField
from wtforms.validators import InputRequired, URL


class CafeForm(FlaskForm):
    coffee_shop = StringField('Cafe name', validators=[InputRequired()])

    location = StringField("Location", validators=[InputRequired(), URL()])

    open_time = TimeField('Open Time', validators=[InputRequired()])

    close_time = TimeField('Close Time', validators=[InputRequired()])

    coffee_rank = SelectField(u'Coffee Rank', choices=['☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'],
                         validators=[InputRequired()])

    wifi_speed = SelectField(u'Wifi Strength', choices=['🛜', '🛜🛜', '🛜🛜🛜', '🛜🛜🛜🛜', '🛜🛜🛜🛜🛜'],
                       validators=[InputRequired()])

    power_outlets = SelectField(u'Power Outlet Availability',
                        choices=['🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'], validators=[InputRequired()])

    submit = SubmitField('Submit')

@dataclass(init=True, repr=True, slots=True)
class CoffeeData:
    coffee_shop: str
    location: str
    open_time: str
    close_time: str
    coffee_rank: str
    wifi_speed: str
    power_outlets: str

    def data_to_dict(self):
        data = {
            'Cafe Name': self.coffee_shop,
            'Location': self.location,
            'Open': self.open_time,
            'Close': self.close_time,
            'Coffee': self.coffee_rank,
            'Wifi': self.wifi_speed,
            'Power': self.power_outlets
        }
        return data


def main():
    structure = CoffeeData(coffee_shop='Stabucks', location='Texas', open_time='8am', close_time='10pm',
                           coffee_rank='☕️', wifi_speed='🛜', power_outlets='🔌')
    pp(structure.data_to_dict())


if __name__ == '__main__':
    main()
