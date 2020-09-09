from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

to_do_list = {
    1: 'learn how to use flask better',
    2: 'find some way to make money off coding',
    3: 'disappear into the woods'
}

class Todo(Resource):

    def get(self):
        return to_do_list
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('task', type=str)
        args =  parser.parse_args()
        id = len(to_do_list) + 1
        task = args.get('task')
        new_entry = {id : task}

        to_do_list.update(new_entry)
        return new_entry
    
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        parser.add_argument('task', type=str)
        args =  parser.parse_args()
        id = args.get('id')
        task = args.get('task')
        updated_entry = {id : task}


        if id in to_do_list.keys():
            to_do_list[id] = task
            return updated_entry
        else:
            return 404

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        args = parser.parse_args()
        id = args.get('id')

        if id in to_do_list:
            del to_do_list[id]
            return 204
        else:    
            return 404


api.add_resource(Todo, '/to_do_list/')

if __name__ == "__main__":
    app.run()
