from django.test import TestCase
from crud_app.models import Employee


class ModelTestCase(TestCase):

    def test_model_employee(self):
        empl1 = Employee.objects.create(first_name="kishan", last_name="gondaliya", email="kishanlnxct@gmail.com", job_role="django", salary=50000)

        self.assertEquals(empl1, '1 (kishan)')


    # def test_model_count(self):
    #     emp_count = Employee.objects.count()
    #     self.assertGreaterEqual(emp_count, 1)
