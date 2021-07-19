from flask.helpers import flash
from server import result
from mysqlconnection import connectToMySQL
import re

class Dojo():

    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def new_ninja(cls, data):
        query = 'INSERT INTO dojos(name, location, language, comment) VALUES( %(name)s, %(location)s, %(language)s, %(comment)s);'

        new_ninja = connectToMySQL('dojo_survey_schema').query_db(query,data)

        return new_ninja

    @classmethod
    def get_ninja_by_id(cls,data):
        query = 'SELECT * FROM dojos WHERE id = %(id)s;'

        result = connectToMySQL('dojo_survey_schema').query_db(query,data)

        single_ninja = cls(result[0])
        

        return single_ninja

    @staticmethod
    def validate_name(user):
        name_regex = re.compile(r"^[a-zA-Z '-]{1,45}$")
        is_valid = True
        if not name_regex.match(user['name']):
            flash('Your name must be between 1 and 45 characters')
            is_valid = False
        return is_valid

