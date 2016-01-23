import falcon
import json
import sebastian

class SebastianResource:
	def on_get(self, req, resp):
		resp.status = falcon.HTTP_200
		resp.body = ('Some text')

	def on_post(self, req, resp):


app = falcon.API()

checker = SebastianResource()

app.add_route('/check', checker)