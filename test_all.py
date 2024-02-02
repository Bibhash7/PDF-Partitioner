import unittest
import app as api

class StatusCodeCheck(unittest.TestCase):
    def test_home_status(self):
        tester = api.app.test_client(self).get('/')
        response = tester.status_code
        self.assertEqual(response,200)

    def test_crop_status(self):
        tester = api.app.test_client(self).get('/crop')
        response = tester.status_code
        self.assertEqual(response, 200)

    def test_merge_status(self):
        tester = api.app.test_client(self).get('/merge')
        response = tester.status_code
        self.assertEqual(response, 200)

    def test_word_status(self):
        tester = api.app.test_client(self).get('/word')
        response = tester.status_code
        self.assertEqual(response, 200)

    def test_success_status(self):
        tester = api.app.test_client(self).post('/success')
        response = tester.status_code
        self.assertEqual(response, 200)

    def test_download_status(self):
        tester = api.app.test_client(self).get('/download')
        response = tester.status_code
        self.assertEqual(response, 200)

    def test_convert_status(self):
        tester = api.app.test_client(self).get('/convert')
        response = tester.status_code
        self.assertEqual(response, 200)

    def test_error_status(self):
        tester = api.app.test_client(self).get('/p')
        response = tester.status_code
        self.assertEqual(response, 200)

if __name__ == '__main__':
    unittest.main()
