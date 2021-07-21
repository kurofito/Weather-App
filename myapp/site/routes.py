from flask import Blueprint, render_template, request, redirect, flash
from myapp.weather_api import city
from myapp.models import City
from myapp.extensions import db

site = Blueprint('site', __name__)


@site.route('/')
def index():
    city_data = City.query.order_by(City.name).all()
    weather_data = []

    if city_data:
        for data in city_data:
            weather_data.append(city.weather(data.name))
        return render_template('index.html', weather=weather_data)
    else:
        return render_template('index.html')


@site.route('/add', methods=['POST'])
def add_city():
    if request.method == 'POST':
        city_name = request.form['city_name'].capitalize()
        info = city.city_id(city_name)
        present = City.query.filter_by(name=info[1]).first()

        if info is None:
            flash("The city doesn't exist!")
            return redirect('/')
        elif present:
            flash("The city has already been added to the list!")
            return redirect('/')
        elif info:
            weather = City(id=info[0], name=info[1])
            db.session.add(weather)
            db.session.commit()
            return redirect('/')
    else:
        return redirect('/')


@site.route('/delete/<data_id>', methods=['GET', 'POST'])
def delete(data_id):
    city_num = City.query.filter_by(id=int(data_id)).first()
    db.session.delete(city_num)
    db.session.commit()
    return redirect('/')
