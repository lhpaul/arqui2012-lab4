import sys
import unittest
import os
import main
import webapp2
import json

class UnitTests(unittest.TestCase):

    def setUp(self):
        import tempfile
        self.old_dir = os.path.abspath(os.curdir) # save old directory
        self.cwd = tempfile.mkdtemp() # new current working directory
        os.chdir(self.cwd)
        
    def tearDown(self):
        import shutil
        os.chdir(self.old_dir)      # restore working directory
        shutil.rmtree(self.cwd)     # delete temp directory
    
    def test_get_no_db(self):
        request = webapp2.Request.blank('/')
        request.method = 'GET'
        response = request.get_response(main.app)      
        self.assertEqual(response.status_int, 404)
        
    def test_get_with_db(self):
        with open('datos.json', 'w') as f:
            f.write(json.dumps('{"mensajes":[]}'))
        request = webapp2.Request.blank('/')
        request.method = 'GET'
        response = request.get_response(main.app)      
        self.assertEqual(response.status_int, 200)
    
    def test_post_text_no_db(self):
        request = webapp2.Request.blank('/')
        request.method = 'POST'
        request.headers['Content-Type'] = 'application/text'
        request.body = 'hola'
        response =request.get_response(main.app)
        self.assertEqual(response.status_int, 201)
        
    def test_post_text_with_db(self):
        with open('datos.json', 'w') as f:
            f.write(json.dumps('{"mensajes":[]}'))
        request = webapp2.Request.blank('/')
        request.method = 'POST'
        request.headers['Content-Type'] = 'application/text'
        request.body = 'hola'
        response =request.get_response(main.app)
        self.assertEqual(response.status_int, 201)
        
    def test_post_json_no_db(self):
        request = webapp2.Request.blank('/')
        request.method = 'POST'
        request.headers['Content-Type'] = 'application/json'
        request.body = json.dumps('{"filo":"algo"}')
        response =request.get_response(main.app)
        self.assertEqual(response.status_int, 201)
        
    def test_post_json_with_db(self):
        with open('datos.json', 'w') as f:
            f.write(json.dumps('{"mensajes":[]}'))
        request = webapp2.Request.blank('/')
        request.method = 'POST'
        request.headers['Content-Type'] = 'application/json'
        request.body = json.dumps('{"filo":"algo"}')
        response =request.get_response(main.app)
        self.assertEqual(response.status_int, 201)
    

        
if __name__ == '__main__':
    unittest.main()