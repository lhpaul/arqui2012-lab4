import sys
import unittest
import os
import main
import webapp2
import json

class FunctionalTests(unittest.TestCase):

    def setUp(self):
        import tempfile
        self.old_dir = os.path.abspath(os.curdir) # save old directory
        self.cwd = tempfile.mkdtemp() # new current working directory
        os.chdir(self.cwd)
        
    def tearDown(self):
        import shutil
        os.chdir(self.old_dir)      # restore working directory
        shutil.rmtree(self.cwd)     # delete temp directory
    
    def test_post_text(self):
        request = webapp2.Request.blank('/')
        request.method = 'POST'
        request.headers['Content-Type'] = 'application/text'
        request.body = 'prueba'
        request.get_response(main.app)
        request2 = webapp2.Request.blank('/')
        request2.method = 'GET'
        response = request2.get_response(main.app)
        data = json.loads(response.body)
        self.assertEqual(data['mensajes'][-1], 'prueba')
        
    def test_post_json(self):
        request = webapp2.Request.blank('/')
        request.method = 'POST'
        request.headers['Content-Type'] = 'application/json'
        prueba = json.dumps('{"algo":"prueba"}')
        request.body = prueba
        request.get_response(main.app)
        request2 = webapp2.Request.blank('/')
        request2.method = 'GET'
        response = request2.get_response(main.app)
        data = json.loads(response.body)
        self.assertEqual(json.dumps(data['mensajes'][-1]), prueba)
        
if __name__ == '__main__':
    unittest.main()