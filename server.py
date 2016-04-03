import falcon
import json
from sebastian.src.ChoraleAnalysis.ChoraleAnalysis import XMLChoraleAnalysis

class SebastianResource:

	def on_post(self, req, resp):
		print "Sebastian request recieved"

		resp.status = falcon.HTTP_200
		params = json.loads(req.stream.read())
		analysis = XMLChoraleAnalysis(params['chorale'])
		analysis.analyze()
		error_list = analysis.get_error_list_all()
		annotated_chorale_xml_path = analysis.get_annotated_chorale().score.write('musicxml')
		annotated_chorale_xml = open(annotated_chorale_xml_path, 'rb').read()

		out = {'errors': [], 'chorale': annotated_chorale_xml}
		for error in error_list:
			out['errors'].append(error.message)

		resp.body = json.dumps(out)

class MockResource:

	def on_post(self, req, resp):
		print "Mock request recieved"	
		resp.status = falcon.HTTP_200
		resp.body = "hello!"

	def on_get(self, req, resp):
		print "Mock request recieved"	
		resp.status = falcon.HTTP_200
		resp.body = "hello!"

application = falcon.API()

mock = MockResource()
checker = SebastianResource()

application.add_route('/', mock)
application.add_route('/check', checker)
