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
        self.employee_test = Employee.objects.create(first_name="kishan", last_name="gondaliya", email="kishanlnxct@gmail.com", job_role="django", salary=50000)
        self.employee_test = Employee.objects.create(first_name="bhavin", last_name="patel", email="bhavinlnxct@gmail.com", job_role="react", salary=45942)
        

    def test_home_post_data_view(self):

        data = self.client.post(self.home_url, {
            "first_name": "ram", 
            "last_name": "ramji",
            "email": "ram@gmail.com", 
            "job_role": "django", 
            "salary": 50560
        }) 
        self.assertEquals(data.status_code, 302)
        self.assertRedirects(data, '/login/')


    def test_home_page_view(self):
    
        data = self.client.get(self.home_url)
        self.assertEquals(data.status_code, 200)
        self.assertTemplateUsed(data, 'crud_app/index.html')
        

    def test_edit_view(self):

        data1 = self.client.get(self.edit_url) 
        self.assertEquals(data1.status_code, 200)
        self.assertTemplateUsed(data1, 'crud_app/update.html')

    def test_login_view_sucsess(self):

        data = self.client.post(self.login_url, {'email': 'kishanlnxct@gmail.com'})
        data2 = self.client.post(self.login_url, {'email': 'bhavinlnxct@gmail.com'})

        self.assertEquals(data.status_code, 302)
        self.assertEquals(data2.status_code, 302)

        self.assertRedirects(data, '/otp_verify/') 
        self.assertRedirects(data2, '/otp_verify/')

        # self.assertTrue(data.context['user'].is_active)


    def test_login_view_fail(self):

        data = self.client.post(self.login_url, {'email': 'test@gmail.com'}) 
        self.assertEquals(data.status_code, 302)
        self.assertRedirects(data, '/login/')


    def test_user_email_valid_or_not(self):
        user_email1 = Employee.objects.get(employee_id=1)
        user_email2 = Employee.objects.get(employee_id=2)

        self.assertEquals(user_email1.email, 'kishanlnxct@gmail.com')
        self.assertEquals(user_email2.email, 'bhavinlnxct@gmail.com')
 

    def test_user_exist_or_not(self):
        user_count = Employee.objects.count()
        self.assertGreaterEqual(user_count,1)
        self.assertNotEqual(user_count, 0)