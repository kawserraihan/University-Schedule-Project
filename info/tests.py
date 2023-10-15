from django.test import TestCase
from info.models import *
from django.urls import reverse
from django.test.client import Client


# Create your tests here.


class InfoTest(TestCase):

    def create_user(self, username='testuser', password='12345678@'):
        self.client = Client()
        return User.objects.create(username=username, password=password)

    def test_user_creation(self):
        us = self.create_user()
        ut = self.create_user(username='teacher')
        t = Teacher(user=ut, id='CS01', name='test')
        t.save()
        self.assertTrue(isinstance(us, User))
        self.assertEqual(ut.is_teacher, hasattr(ut, 'teacher'))

    def create_dept(self, id='CS', name='CS'):
        return Dept.objects.create(id=id, name=name)

    def test_dept_creation(self):
        d = self.create_dept()
        self.assertTrue(isinstance(d, Dept))
        self.assertEqual(d.__str__(), d.name)

    def create_class(self, id='CS5A', sem=5, section='A'):
        dept = self.create_dept()
        return Class.objects.create(id=id, dept=dept, sem=sem, section=section)

    def test_class_creation(self):
        c = self.create_class()
        self.assertTrue(isinstance(c, Class))
        self.assertEqual(c.__str__(), "%s : %d %s" % (c.dept.name, c.sem, c.section))

    def create_course(self, id='CS510', name='Data Struct', shortname='DS'):
        dept = self.create_dept(id='CS2')
        return Course.objects.create(id=id, dept=dept, name=name, shortname=shortname)

    def test_course_creation(self):
        c = self.create_course()
        self.assertTrue(isinstance(c, Course))
        self.assertEqual(c.__str__(), c.name)

   


    def create_teacher(self, id='CS01', name='teacher'):
        dept = self.create_dept(id='CS3')
        return Teacher.objects.create(id=id, name=name, dept=dept)

    def test_teacher_creation(self):
        s = self.create_teacher()
        self.assertTrue(isinstance(s, Teacher))
        self.assertEqual(s.__str__(), s.name)


    # views
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('test_user', 'test@test.com', 'test_password')

    def test_index_admin(self):
        self.client.login(username='test_user', password='test_password')
        response = self.client.get(reverse('index'))
        self.assertContains(response, "you have been logged out")
        self.assertEqual(response.status_code, 200)

  

    def test_index_teacher(self):
        self.client.login(username='test_user', password='test_password')
        s = Teacher.objects.create(user=User.objects.first(), id='test', name='test_name')
        response = self.client.get(reverse('index'))
        self.assertContains(response, s.name)
        self.assertEqual(response.status_code, 200)






