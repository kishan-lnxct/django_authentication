from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.urls import resolve
from crud_app.views import *

class urlTest(SimpleTestCase):
    def test_home_url_resolve(self):
        url = reverse('home')
        # veriable_name = reverse('url_name')

        self.assertEquals(resolve(url).func, index)
        # resolve(veriable_name).func, view_name --> view_name of urls inside pass

    #     home_view_test = resolve('/')
    #     self.assertEquals(home_view_test.func, index)
    
    def test_login_url_resolve(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login_view)
    
    def test_logout_url_resolve(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout_view)

    def test_otp_verify_url_resolve(self):
        url = reverse('otp_verify')
        self.assertEquals(resolve(url).func, otp_verify)
    

    def test_show_url_resolve(self):
        url = reverse('show')
        self.assertEquals(resolve(url).func, show)


    def test_delete_url_resolve(self):
        url = reverse('delete', kwargs={"emp_id": 2})
        # veriable_name = reverse('url_name', kwargs={ same variable name that pass in url })

        self.assertEquals(resolve(url).func, delete_data)
        # resolve(veriable_name).func, view_name --> view_name of urls inside pass


        # delete_view_test = reverse('delete', kwargs={'emp_id': 1})
        # self.assertEquals('delete', resolve(delete_view_test))

    def test_edit_url_resolve(self):
        url = reverse('edit', kwargs={"emp_id": 2})
        self.assertEquals(resolve(url).func, edit_data)

    #     edit_view_test = resolve('/edit/<emp_id>/')
    #     self.assertEquals(edit_view_test.func, edit_data)