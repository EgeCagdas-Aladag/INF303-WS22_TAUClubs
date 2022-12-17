import json
from django.test import Client, TestCase
from accounts.models import User
from .models import Club
from rest_framework.test import APIClient


# Create your tests here.

class ClubTestCase(TestCase):

    def setUp(self):

        self.admin = User.objects.create_superuser(email="admin@stud.tau.edu.tr", password="admin@123", first_name="Admin", last_name="Super")

        self.user = User.objects.create_user(email="student4@hotmail.com", password="pass@123", first_name="user", last_name="user")

        self.club = Club.objects.create(name="Informatix", manager=User.objects.create(email = "student3@hotmail.com"))
    
    def test_create_club(self):
        response_ = self.client.get('/admin/', follow=True)
        self.response = self.client.login(email="admin@stud.tau.edu.tr", password="admin@123")
   
        self.assertTrue(self.response)
        print("client.login(): " + str(self.response))

        club_data = {
            "name": "Test Club",
            "manager": self.user.id,
            "members": [],
            "pending_members": [],
            "responsibleLecturer": "Test Lecturer",
            "clubMail": "testclub@stud.tau.edu.tr",
            "followers": []
        }

        self.response = self.client.post("/clubs/", data=club_data)
        self.assertEqual(201, self.response.status_code)
        print("POST-Request: " + str(self.response.status_code))

        clubs = Club.objects.all()
        control = [True for id in range(0,len(clubs)) if clubs[id].name == "Test Club"]
        self.assertTrue(True in control)
        print("Neue Club erstellt: " + str(control[0]) + ": " + str(clubs[0]))

    def test_update_club_infos_byadmin(self):
        
        response_ = self.client.get('/admin/', follow=True)
        self.response = self.client.login(email="admin@stud.tau.edu.tr", password="admin@123")

        self.assertTrue(self.response)
        print("client.login(): " + str(self.response))

        data = {"name" : "INFX"}

        self.response = self.client.patch("/clubs/" + str(self.club.id) + "/", data=data, format='json', content_type='application/json')
        clubs = Club.objects.all()
   
        self.assertEqual(200, self.response.status_code)
        print("PATCH-Request: " + str(self.response.status_code))

        self.assertEqual(clubs[self.club.id - 1].name, data['name'])
        print("Aktualisiert: " + str(clubs[self.club.id - 1]))

        
    def test_membership(self):

        self.response = self.client.login(email='student4@hotmail.com',
            password='pass@123')

        self.assertEqual(self.response, True)
        print("client.login(): " + str(self.response))

        self.response = self.client.get("/clubs/" + str(self.club.id) + "/membership/")
        
        self.assertEqual(201, self.response.status_code)
        print("GET-Request: " + str(self.response.status_code))
        self.assertEqual(self.user in self.club.pending_members.all(), True)
        print("Membership Request: " + str(self.user in self.club.pending_members.all()))

    def test_follow(self):
        
        self.response = self.client.login(email='student4@hotmail.com',
            password='pass@123')

        self.assertEqual(self.response, True)
        print("clint.login(): " + str(self.response))

        self.response = self.client.get("/clubs/" + str(self.club.id) + "/follow/")
        print("GET-Request: " + str(self.response.status_code))

        self.assertEqual(200, self.response.status_code)
        self.assertEqual(self.user in self.club.followers.all(), True)
        print("Followed: " + str(self.user in self.club.followers.all()))

    def test_unfollow(self):

        self.response = self.client.login(email='student4@hotmail.com',
            password='pass@123')

        self.assertEqual(self.response, True)
        print("clint.login(): " + str(self.response))
        
        self.response = self.client.get("/clubs/" + str(self.club.id) + "/unfollow/")
        print("GET-Request: " + str(self.response.status_code))

        self.assertEqual(200, self.response.status_code)
        self.assertEqual(self.user not in self.club.followers.all(), True)
        print("Unfollowed: " + str(self.user not in self.club.followers.all()))

class CreatePostTestCase(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(email="student4@hotmail.com", password="pass@123", first_name="user", last_name="user")

        self.club = Club.objects.create(name="Informatix", manager=User.objects.create(email = "student3@hotmail.com"))


    #Manager Kontroll

    def test_managerKontrol(self):

        self.response = self.client.login(email='student4@hotmail.com',password='pass@123')

        self.assertEqual(self.response, True)

        self.response = self.client.get("/clubs/" + str(self.club.id) + "/manager/")
        
        self.assertEqual(201, self.response.status_code)
        self.assertEqual(self.user in self.club.manager.all(), True)

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
        self.response = self.client.get("/clubs/" + str(self.club.id) + "/pending_members/")
        
        self.assertEqual(201, self.response.status_code)
        self.assertEqual(self.user in self.club.pending_members.all(), True)

    # Club manager delete and chance members
    
    