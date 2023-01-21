from flask import Flask #for runing server
from flask_restful import Api,Resource


app = Flask(__name__)
api = Api(app)

#design Resource
class blog_post(Resource):
	def	get(self):
		return {"msg":"Hello from http://127.0.0.1:5000/"}

#call Resource
api.add_resource(blog_post,"/blog")

if __name__ == "__main__":
    app.run(debug=True)

