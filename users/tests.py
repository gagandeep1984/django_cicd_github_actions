from django.test import TestCase
from django.contrib.auth.models import User

class UserTestCase(TestCase):

	def test_dummy(self):
		self.assertTrue(True)

	'''
	def test_user(self):
		username = 'David'
		password = 'some#password'
	
		u = User(username = username)
		u.setPassword(password)
		u.save()
	
		self.assertEqual(u.username, username)
		self.assertTrue(u.check_password(password))
	'''

