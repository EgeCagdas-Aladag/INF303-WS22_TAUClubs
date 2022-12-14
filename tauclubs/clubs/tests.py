from django.test import Client, TestCase
from accounts.models import User
from .models import Club
from rest_framework.test import APIClient


# Create your tests here.

class ClubTestCase(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(email="student4@hotmail.com", password="pass@123", first_name="user", last_name="user")

        self.club = Club.objects.create(name="Informatix", manager=User.objects.create(email = "student3@hotmail.com"))

    def test_membership(self):

        self.response = self.client.login(email='student4@hotmail.com',
            password='pass@123')

        self.assertEqual(self.response, True)

        self.response = self.client.get("/clubs/" + str(self.club.id) + "/membership/")
        
        self.assertEqual(201, self.response.status_code)
        self.assertEqual(self.user in self.club.pending_members.all(), True)

    def test_follow(self):
        
        self.response = self.client.login(email='student4@hotmail.com',
            password='pass@123')

        self.assertEqual(self.response, True)
        
        self.response = self.client.get("/clubs/" + str(self.club.id) + "/follow/")

        self.assertEqual(200, self.response.status_code)
        self.assertEqual(self.user in self.club.followers.all(), True)

    def test_unfollow(self):

        self.response = self.client.login(email='student4@hotmail.com',
            password='pass@123')

        self.assertEqual(self.response, True)
        
        self.response = self.client.get("/clubs/" + str(self.club.id) + "/unfollow/")

        self.assertEqual(200, self.response.status_code)
        self.assertEqual(self.user not in self.club.followers.all(), True)

class CreatePostTestCase(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(email="student4@hotmail.com", password="pass@123", first_name="user", last_name="user")

        self.club = Club.objects.create(name="Informatix", manager=User.objects.create(email = "student3@hotmail.com"))


    #Manager Kontroll

    def test_membership(self):

        self.response = self.client.login(email='student4@hotmail.com',password='pass@123')

        self.assertEqual(self.response, True)

        self.response = self.client.get("/clubs/" + str(self.club.id) + "/membership/")
        
        self.assertEqual(201, self.response.status_code)
        self.assertEqual(self.user in self.club.Post.objects.all(), True)

    #Post teilen in der Clubseite

    def test_create_post(self):

        client = APIClient()
        client.force_authenticate(user=self.user) ## 

        self.response = self.client.post('/PostViewSet/', {'postId': '1', 'name': 'konser' , 'postdate' :'22.1.23' , 'clubname': 'Müzik'}, format='json') ###

        self.assertEqual(201, self.response.status_code)
        self.assertEqual(self.user in self.club.Post.objects.all(), True)
    
    def test_edit_post(self):
        
       data = {'postId': '2', 'name': 'Etkinkik' , 'postdate' :'22.1.23' , 'clubname': 'EMK'}
       self.response = self.client.put('/posts/1', "data")
        #serializer = PostSerializer(post, data=request.data)
        
       self.assertEqual(201, self.response.status_code)
       self.assertEqual(self.user in self.club.Post.objects.all(), True)

    def test_newInfo(self):
        
        # Checking new member information
        self.response = self.client.get("/clubs/" + str(self.club.id) + "/membership/")
        
        self.assertEqual(201, self.response.status_code)
        self.assertEqual(self.user in self.club.pending_members.all(), True)

    # Club manager delete and chance members
    