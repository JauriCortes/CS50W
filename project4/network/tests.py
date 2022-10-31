from urllib import response
from django.test import TestCase, Client
from django.urls import reverse

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
        response = c.post(reverse('register'), {
            'username': {self.name2},
            'email': {self.mail2},
            'password': {self.password}, 
            'confirmation': {self.password}})
        
        self.assertEqual(response.status_code, 302)

    def test_register_wrongPassword(self):

        c = Client()
        response = c.post(reverse('register'), {
            'username': {self.name2},
            'email': {self.mail2},
            'password': {self.password}, 
            'confirmation': {self.wrongPassword}})
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['message'], "Passwords must match.")
    
    def test_register_takenUsername(self):

        c = Client()
        response = c.post(reverse('register'), {
            'username': {self.TakenName},
            'email': {self.mail2},
            'password': {self.password}, 
            'confirmation': {self.password}})
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['message'], "Username already taken.")

# there should be a new post box on all post page
