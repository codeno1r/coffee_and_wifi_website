from app.extensions import FlaskForm, StringField, SubmitField, URLField, SelectField, DataRequired


class CafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Google Map Location', validators=[DataRequired()],
                        render_kw={"placeholder": "e.g. https://www.google.com/maps/place/***"})
    open_time = StringField('Opening Time', validators=[DataRequired()], render_kw={"placeholder": "e.g. 9AM"})
    close_time = StringField('Closing Time', validators=[DataRequired()], render_kw={"placeholder": "e.g. 11PM"})
    coffee_rating = SelectField('Coffee Rating',
                                choices=[
                                    '☕',
                                    '☕☕',
                                    '☕☕☕',
                                    '☕☕☕☕',
                                    '☕☕☕☕☕'
                                ], validators=[DataRequired()])
    wifi_rating = SelectField('WiFi Rating',
                              choices=[
                                  '✘',
                                  '💪',
                                  '💪💪',
                                  '💪💪💪',
                                  '💪💪💪💪',
                                  '💪💪💪💪💪',
                              ], validators=[DataRequired()])
    power_rating = SelectField('Power Rating',
                               choices=[
                                   '✘',
                                   '🔌',
                                   '🔌🔌',
                                   '🔌🔌🔌',
                                   '🔌🔌🔌🔌',
                                   '🔌🔌🔌🔌🔌',
                               ], validators=[DataRequired()])
    submit = SubmitField('Submit', render_kw={'class': 'my-4'})
