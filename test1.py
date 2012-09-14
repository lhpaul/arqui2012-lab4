import unittest

class TestRequests(unittest.TestCase):

    def setUp(self):
        self.old_dir = os.path.abspath(os.curdir) # save old directory
        self.cwd = tempfile.mkdtemp() # new current working directory
        os.chdir(self.cwd)
        
    def tearDown(self):
        os.chdir(self.old_dir)      # restore working directory
        shutil.rmtree(self.cwd)     # delete temp directory
    
    def test_get_no_db(self):
        request = webapp2.Request.blank('/')
        request.method = 'GET'
        response = request.get_response(main.app)      
        self.assertEqual(response.status_int, 404)


if __name__ == '__main__':
    unittest.main()