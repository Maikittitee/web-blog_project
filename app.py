#Server Side

from flask import Flask #for runing server
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)

mydata = {
	0 :{"name":"admin","bio":"i'm very hungry right now."},
	1 :{"name":"Mai","bio":"My name is Mai,Nice to meet you."}
}

#design Resource
class blog_post(Resource): # Used for display data
	def	get(self, id):
		return ("Hello " + mydata[id]["name"]+ " --> bio: " + mydata[id]["bio"])

	def post(self, id): # Used for create data
		return {"msg":f"Hello {id} This is Response from POST"}



#call Resource
api.add_resource(blog_post,"/blog/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)
