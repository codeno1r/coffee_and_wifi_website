from flask import Blueprint, render_template, redirect, url_for
from .extensions import db
from .models import Cafe
from .forms import CafeForm

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/cafes')
def cafes():
    cafe_list = db.session.execute(db.select(Cafe).order_by(Cafe.id)).scalars().all()
    return render_template('cafes.html', cafes=cafe_list)


@main.route('/add', methods=['GET', 'POST'])
def add():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name=form.name.data,
            location=form.location.data,
            opening_time=form.open_time.data,
            closing_time=form.close_time.data,
            coffee=form.coffee_rating.data,
            wifi=form.wifi_rating.data,
            power=form.power_rating.data
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('add.html', form=form)
