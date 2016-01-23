import falcon
import json
from sebastian.src.ChoraleAnalysis.ChoraleAnalysis import XMLChoraleAnalysis

class SebastianResource:

	def on_post(self, req, resp):
		resp.status = falcon.HTTP_200
		params = json.loads(req.stream.read())
		analysis = XMLChoraleAnalysis(params['chorale'])
		analysis.analyze()
		error_list = analysis.get_error_list_all()

		out = {'errors': []}
		for error in error_list:
			out['errors'].append(error.message)

		resp.body = json.dumps(out)


application = falcon.API()

checker = SebastianResource()

application.add_route('/check', checker)
