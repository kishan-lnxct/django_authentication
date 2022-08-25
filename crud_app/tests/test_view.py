from django.test import TestCase, Client
from django.urls import reverse
from crud_app.models import Employee

class viewsTest(TestCase):

    def setUp(self):
        
        self.client = Client()
        self.home_url = reverse('home')
        self.login_url = reverse('login')
        # self.logout_url = reverse('logout')
        self.edit_url = reverse('edit', kwargs={"emp_id": 1})
        self.employee_test = Employee.objects.create(first_name="kishan", last_name="gondaliya", email="kishan@gmail.com", job_role="django", salary=50000)
        

    def test_home_view(self):

        data = self.client.get(self.home_url) 
        self.assertEquals(data.status_code, 200)
        self.assertTemplateUsed(data, 'crud_app/index.html')

    def test_edit_view(self):

        data1 = self.client.get(self.edit_url) 
        self.assertEquals(data1.status_code, 200)
        self.assertTemplateUsed(data1, 'crud_app/update.html')

    def test_login_view_sucsess(self):

        data = self.client.post(self.login_url, {'email': 'kishan@gmail.com'}) 
        self.assertEquals(data.status_code, 302)
        self.assertRedirects(data, '/otp_verify/') 

        # self.assertTrue(data.context['user'].is_active)


    def test_login_view_fail(self):
    
        data = self.client.post(self.login_url, {'email': 'test@gmail.com'}) 
        print(data.status_code)
        self.assertEquals(data.status_code, 404)
        self.assertTemplateUsed(data, 'crud_app/login.html')