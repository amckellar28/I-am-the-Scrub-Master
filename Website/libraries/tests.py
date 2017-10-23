from django.test import TestCase

from libraries.models import Library, Colleges, Hotels, Industries
from libraries.models import Parks, Zoos, Museums, Restaurants, Malls

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
        Colleges.objects.create(title='college', address = '23', departments = 'health',
                                emailaddress = 'library@website.com',
                                home_page='www.website.com',
                                description = 'school',
                                rank = '24')
        Hotels.objects.create(title='library', address='13', number='0456',
                              emailaddress='library@website.com',
                              home_page='www.website.com',
                              description='items')
        Parks.objects.create(title='library', address='13', number='0456',
                             emailaddress='library@website.com',
                             home_page='www.website.com',
                             description='items')
        Zoos.objects.create(title='library', address='13', number='0456',
                            emailaddress='library@website.com',
                            home_page='www.website.com',
                            description='items')
        Museums.objects.create(title='library', address='13',
                               number='0456',
                               emailaddress='library@website.com',
                               home_page='www.website.com',
                               description='items')
        Restaurants.objects.create(title='library', address='13',
                                   number='0456',
                                   emailaddress='library@website.com',
                                   home_page='www.website.com',
                                   description='items')
        Malls.objects.create(title='library', address='13', number='0456',
                             emailaddress='library@website.com',
                             home_page='www.website.com',
                             description='items')
        Industries.objects.create(title='library', address='13',
                                  industrytype='insurance',
                                  emailaddress='library@website.com',
                                  home_page='www.website.com',
                                  description='items')


##Testing library database
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

    def test_multiple_object(self):
        Library.objects.create(title='library', address='13', number='0456',
                               emailaddress='library@website.com', home_page='www.website.com',
                               description='iwow')
        item = Library.objects.get(id=2)
        field_label = item.description
        self.assertEquals(field_label,'iwow')

##Testing College database

    def test_college_title(self):
        item = Colleges.objects.get(id=1)
        field_label = item.title
        self.assertEquals(field_label,'college')

    def test_college_rank(self):
        item = Colleges.objects.get(id=1)
        field_label = item.rank
        self.assertEquals(field_label,'24')

    def test_college_description(self):
        item = Colleges.objects.get(id=1)
        field_label = item.description
        self.assertEquals(field_label,'school')

    def test_college_emailaddress(self):
        item = Colleges.objects.get(id=1)
        field_label = item.emailaddress
        self.assertEquals(field_label,'library@website.com')

    def test_college_home_page(self):
        item = Colleges.objects.get(id=1)
        field_label = item.home_page
        self.assertEquals(field_label,'www.website.com')

    def test_college_address(self):
        item = Colleges.objects.get(id=1)
        field_label = item.address
        self.assertEquals(field_label,'23')

    def test_college_departments(self):
        item = Colleges.objects.get(id=1)
        field_label = item.departments
        self.assertEquals(field_label,'health')

##Testing Hotel database

    def test_title_Hotels(self):
        item = Hotels.objects.get(id=1)
        field_label = item.title
        self.assertEquals(field_label,'library')

        
    def test_address_Hotels(self):
        item = Hotels.objects.get(id=1)
        field_label = item.address
        self.assertEquals(field_label,'13')

    def test_number_Hotels(self):
        item = Hotels.objects.get(id=1)
        field_label = item.number
        self.assertEquals(field_label,'0456')

    def test_emailaddress_Hotels(self):
        item = Hotels.objects.get(id=1)
        field_label = item.emailaddress
        self.assertEquals(field_label,'library@website.com')

    def test_home_page_Hotels(self):
        item = Hotels.objects.get(id=1)
        field_label = item.home_page
        self.assertEquals(field_label,'www.website.com')

    def test_description_Hotels(self):
        item = Hotels.objects.get(id=1)
        field_label = item.description
        self.assertEquals(field_label,'items')

##Testing Parks database
    def test_title_Parks(self):
        item = Parks.objects.get(id=1)
        field_label = item.title
        self.assertEquals(field_label,'library')

        
    def test_address_Parks(self):
        item = Parks.objects.get(id=1)
        field_label = item.address
        self.assertEquals(field_label,'13')

    def test_number_Parks(self):
        item = Parks.objects.get(id=1)
        field_label = item.number
        self.assertEquals(field_label,'0456')

    def test_emailaddress_Parks(self):
        item = Parks.objects.get(id=1)
        field_label = item.emailaddress
        self.assertEquals(field_label,'library@website.com')

    def test_home_page_Parks(self):
        item = Parks.objects.get(id=1)
        field_label = item.home_page
        self.assertEquals(field_label,'www.website.com')

    def test_description_Parks(self):
        item = Parks.objects.get(id=1)
        field_label = item.description
        self.assertEquals(field_label,'items')
##Testing Zoos database
    def test_title_Zoos(self):
        item = Zoos.objects.get(id=1)
        field_label = item.title
        self.assertEquals(field_label,'library')
        
    def test_address_Zoos(self):
        item = Zoos.objects.get(id=1)
        field_label = item.address
        self.assertEquals(field_label,'13')

    def test_number_Zoos(self):
        item = Zoos.objects.get(id=1)
        field_label = item.number
        self.assertEquals(field_label,'0456')

    def test_emailaddress_Zoos(self):
        item = Zoos.objects.get(id=1)
        field_label = item.emailaddress
        self.assertEquals(field_label,'library@website.com')

    def test_home_page_Zoos(self):
        item = Zoos.objects.get(id=1)
        field_label = item.home_page
        self.assertEquals(field_label,'www.website.com')

    def test_description_Zoos(self):
        item = Zoos.objects.get(id=1)
        field_label = item.description
        self.assertEquals(field_label,'items')
##Testing Museums database

    def test_title_Museums(self):
        item = Museums.objects.get(id=1)
        field_label = item.title
        self.assertEquals(field_label,'library')
        
    def test_address_Museums(self):
        item = Museums.objects.get(id=1)
        field_label = item.address
        self.assertEquals(field_label,'13')

    def test_number_Museums(self):
        item = Museums.objects.get(id=1)
        field_label = item.number
        self.assertEquals(field_label,'0456')

    def test_emailaddress_Museums(self):
        item = Museums.objects.get(id=1)
        field_label = item.emailaddress
        self.assertEquals(field_label,'library@website.com')

    def test_home_page_Museums(self):
        item = Museums.objects.get(id=1)
        field_label = item.home_page
        self.assertEquals(field_label,'www.website.com')

    def test_description_Museums(self):
        item = Museums.objects.get(id=1)
        field_label = item.description
        self.assertEquals(field_label,'items')
##Testing Restaurants database
    def test_title_Restaurants(self):
        item = Restaurants.objects.get(id=1)
        field_label = item.title
        self.assertEquals(field_label,'library')
        
    def test_address_Restaurants(self):
        item = Restaurants.objects.get(id=1)
        field_label = item.address
        self.assertEquals(field_label,'13')

    def test_number_Restaurants(self):
        item = Restaurants.objects.get(id=1)
        field_label = item.number
        self.assertEquals(field_label,'0456')

    def test_emailaddress_Restaurants(self):
        item = Restaurants.objects.get(id=1)
        field_label = item.emailaddress
        self.assertEquals(field_label,'library@website.com')

    def test_home_page_Restaurants(self):
        item = Restaurants.objects.get(id=1)
        field_label = item.home_page
        self.assertEquals(field_label,'www.website.com')

    def test_description_Restaurants(self):
        item = Restaurants.objects.get(id=1)
        field_label = item.description
        self.assertEquals(field_label,'items')
##Testing Malls database
    def test_title_Malls(self):
        item = Malls.objects.get(id=1)
        field_label = item.title
        self.assertEquals(field_label,'library')
        
    def test_address_Malls(self):
        item = Malls.objects.get(id=1)
        field_label = item.address
        self.assertEquals(field_label,'13')

    def test_number_Malls(self):
        item = Malls.objects.get(id=1)
        field_label = item.number
        self.assertEquals(field_label,'0456')

    def test_emailaddress_Malls(self):
        item = Malls.objects.get(id=1)
        field_label = item.emailaddress
        self.assertEquals(field_label,'library@website.com')

    def test_home_page_Malls(self):
        item = Malls.objects.get(id=1)
        field_label = item.home_page
        self.assertEquals(field_label,'www.website.com')

    def test_description_Malls(self):
        item = Malls.objects.get(id=1)
        field_label = item.description
        self.assertEquals(field_label,'items')
##Testing Industries database
    def test_title_Industries(self):
        item = Industries.objects.get(id=1)
        field_label = item.title
        self.assertEquals(field_label,'library')
        
    def test_address_Industries(self):
        item = Industries.objects.get(id=1)
        field_label = item.address
        self.assertEquals(field_label,'13')

    def test_type_Industries(self):
        item = Industries.objects.get(id=1)
        field_label = item.industrytype
        self.assertEquals(field_label,'insurance')

    def test_emailaddress_Industries(self):
        item = Industries.objects.get(id=1)
        field_label = item.emailaddress
        self.assertEquals(field_label,'library@website.com')

    def test_home_page_Industries(self):
        item = Industries.objects.get(id=1)
        field_label = item.home_page
        self.assertEquals(field_label,'www.website.com')

    def test_description_Industries(self):
        item = Industries.objects.get(id=1)
        field_label = item.description
        self.assertEquals(field_label,'items')

  
