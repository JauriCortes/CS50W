from django.test import TestCase, Client
from .models import User

# Create your tests here.

# User should be able to registrate, sign in and sign out
class NetworkTestCAse(TestCase):
    def setUp(self):
        
        # create credentials
        self.TakenName = "Harry"
        self.name2 = "Ron"

        self.TakenMail = "harry@potter.com"
        self.mail2 = "ron@weasley.com"

        self.password = "123"
        self.wrongPassword = "alberto"

        user = User.objects.create_user(self.TakenName, self.TakenMail, self.password)
        user.save()
    
    def test_register(self):

        c = Client()
        response = c.post(f"//register/", {'username': {self.name2}, 'password': {self.password}, 'confirmation': {self.password}})
        print(get_user(self.client).is_authenticated())
        self.assertEqual(response.status_code, 200)

# there should be a new post box on all post page
