import sys
import unittest
import os
import main
import webapp2

class TestRequests(unittest.TestCase):

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
        
    def get_with_db(self):
        with open('datos.json', 'w') as f:
            f.write(json.dumps('{"mensajes":[]}'))
        request = webapp2.Request.blank('/')
        request.method = 'GET'
        response = request.get_response(main.app)      
        self.assertEqual(response.status_int, 200)
    
    def post_text_no_db(self):
        request = webapp2.Request.blank('/?mensaje=algo')
        request.method = 'Post'
        request.get_response(main.app)
        request2 = webapp2.Request.blank('/')
        request2.method = 'GET'
        response = request2.get_response(main.app)  
        import json
        data = json.loads(response)
        self.assertEqual(data['mensajes'][-1], 'algo')


if __name__ == '__main__':
    unittest.main()