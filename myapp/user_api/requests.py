from flask_restful import Resource, reqparse, inputs, fields, marshal_with
from flask import abort
from myapp.models import City


resource_fields = {
    'id': fields.Integer,
    'name': fields.String
}


class Weather(Resource):
    @marshal_with(resource_fields)
    def get(self):
        data = City.query.all()
        return data
