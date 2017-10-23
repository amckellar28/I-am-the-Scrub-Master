from django.test import TestCase

from libraries.models import Library

class librariesModelTest(TestCase):

##    @classmethod
##    def setUpTestData(cls):
##        #Set up non-modified objects used by all test methods
##        Library.objects.create(first_name='Big', last_name='Bob')



    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Library.objects.create(title='library', address='13', number='0456',
                               emailaddress='library@website.com', home_page='www.website.com',
                               description='items')

    def test_title_label(self):
        item = Library.objects.get(id=1)
        field_label = item.title
        self.assertEquals(field_label,'library')
        
    def test_address_label(self):
        item = Library.objects.get(id=1)
        field_label = item.address
        self.assertEquals(field_label,'13')

    def test_number_label(self):
        item = Library.objects.get(id=1)
        field_label = item.number
        self.assertEquals(field_label,'0456')

    def test_emailaddress_label(self):
        item = Library.objects.get(id=1)
        field_label = item.emailaddress
        self.assertEquals(field_label,'library@website.com')

    def test_home_page_label(self):
        item = Library.objects.get(id=1)
        field_label = item.home_page
        self.assertEquals(field_label,'www.website.com')

    def test_description_label(self):
        item = Library.objects.get(id=1)
        field_label = item.description
        self.assertEquals(field_label,'items')

