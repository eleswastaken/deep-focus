
from flask_restful import Resource, reqparse
from models.user import Users
from helpers.jwt import createJWT

def bcrypt(p):
    return p

class LogIn(Resource):
    # def get(self):
    #     return {'message': 'this is a log-in route!'}

    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument(name='email', required=True)
        parser.add_argument(name='password', required=True)
        args = parser.parse_args()
        try:
            user = Users.objects(email=args['email'])[0]
        except:
            return 

        if bcrypt(user.password) == args['password']:
            # signed in
            return {'token': createJWT(username=user.username, email=user.email)}

        return 