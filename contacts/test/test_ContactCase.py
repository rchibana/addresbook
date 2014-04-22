'''
Created on Apr 9, 2014

@author: rchibana
'''

from django.test.testcases import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.utils.unittest.case import TestCase
from contacts.models import Contact


class ContactTests(TestCase):
    """Contact model tests."""

    def test_str(self):

        contact = Contact(first_name='John', last_name='Smith')

        self.assertEquals(
            str(contact),
            'John Smith',
        )


class ContactListIntegrationTests(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(ContactListIntegrationTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(ContactListIntegrationTests, cls).tearDownClass()

    def test_contact_listed(self):

        # create a test contact
        Contact.objects.create(first_name='foo', last_name='bar')

        # make sure it's listed as <first> <last> on the list
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.assertEqual(
            self.selenium.find_elements_by_css_selector('.contact')[0].text,
            'foo bar'
        )

        def test_add_contact_linked(self):

            self.selenium.get('%s%s' % (self.live_server_url, '/'))
            self.assert_(
                self.selenium.find_element_by_link_text('add_contact')
            )

        def test_add_contact(self):

            self.selenium.get('%s%s' % (self.live_server_url, '/'))
            self.selenium.find_element_by_link_text('add contact').click()

            self.selenium.find_element_by_id('id_first_name').send_keys('test')
            self.selenium.find_element_by_id('id_last_name').send_keys('contact')
            self.selenium.find_element_by_id('id_email').send_keys('test@example.com')

            self.selenium.find_element_by_id('save_contact').click()
            self.assertEqual(
                self.selenium.find_element_by_css_selector('.contact')[-1].text,
                'test contact'
            )
