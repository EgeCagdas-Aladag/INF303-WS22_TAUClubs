from django.test import TestCase
from .models import User

# Create your tests here.


class CreateUserTestCase(TestCase):
    
    def setUp(self):

        self.user = User.objects.create_user(email="student4@hotmail.com", password="pass@123", first_name="user", last_name="user")


    def test_sign_up_user(self):
        
        userdata=  {
            "email": [
                "testuser@stud.tau.edu.tr"
            ],
            "password1": [
                "pass@123"
            ],
            "password2": [
                "pass@123"
            ]
        }

        self.response = self.client.post("/dj-rest-auth/registration/", data=userdata)
        self.assertEqual(201, self.response.status_code)
        print("POST-Request Status Code: " + str(self.response.status_code))
        users = User.objects.all()
        control = [True for id in range(0,len(users)) if users[id].email == "testuser@stud.tau.edu.tr"]
        self.assertTrue(True in control)
        print("Erstellte User: "+ str(users[1].email))

    def test_login(self):

        self.response = self.client.login(email="student4@hotmail.com", password="pass@123")
   
        self.assertTrue(self.response)
        print("Logged-in: "+ str(self.response))

    def test_update_user(self):

        self.response = self.client.login(email="student4@hotmail.com", password="pass@123")

        self.assertTrue(self.response)
        print("Logged-in: "+str(self.response))
        data = {"first_name" : "Test1"}

        self.response = self.client.patch("/users/" + str(self.user.id) + "/", data=data, format='json', content_type='application/json')
        
        users = User.objects.all()
   
        self.assertEqual(200, self.response.status_code)
        print("PATCH-Request Status Code: "+str(self.response.status_code))
        self.assertEqual(users[self.user.id - 1].first_name, data['first_name'])
        print("Created User: "+ str(data["first_name"]))
