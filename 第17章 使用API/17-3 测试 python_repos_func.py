import unittest

import python_repos_func as prf


class PythonReposFucnTestCase(unittest.TestCase):
    def setUp(self):
        self.r = prf.get_response()
        self.repo_dicts = prf.get_repo_dicts(self.r)
        self.repo_dict = self.repo_dicts[0]

    def test_get_response(self):
        self.assertEqual(200, self.r.status_code)

    def test_get_repo_dicts(self):
        self.assertEqual(30, len(self.repo_dicts))
        required_keys = ['name', 'owner', 'stargazers_count', 'html_url']
        for key in required_keys:
            # self.assertTrue(key in self.repo_dict.keys())
            self.assertIn(key, self.repo_dict.keys())


if __name__ == '__main__':
    unittest.main()
