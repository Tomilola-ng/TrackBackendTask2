from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api.models import Person 

class PersonAPITest(TestCase):
    print("=============================")
    print("This script has 5 tests and it all starts by creating a person instance with parsed data, some correct others incorrect for testing purpose.")
    print("=============================")
    
    def setUp(self):
        self.client = APIClient()
        self.person_data = {'name': 'John Doe', 'email': 'john@example.com'}
        self.url = reverse('person-list-create') 
    
    def test_create_person(self):
        response = self.client.post(self.url, self.person_data, format='json')
        print(f"Attempted to create a person using valid data {response}")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_person(self):
        person = Person.objects.create(name='Alice', email='alice@example.com')
        response = self.client.get(reverse('person-detail', args=[person.id]))
        print(f"Attempted to fetch a person with valid id  {response}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update_person(self):
        person = Person.objects.create(name='Bob', email='bob@example.com')
        updated_data = {'name': 'Updated Bob', 'email': 'updated_bob@example.com'}
        response = self.client.put(reverse('person-detail', args=[person.id]), updated_data,
        format='json')
        print(f"Attempted to update a person with valid id {response}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete_person(self):
        person = Person.objects.create(name='Charlie', email='charlie@example.com')
        response = self.client.delete(reverse('person-detail', args=[person.id]))
        print(f"Attempted to delete a person with valid ID {response}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_invalid_data(self):
        invalid_data = {'name': 123, 'email': 'invalid-email'} 
        response = self.client.post(self.url, invalid_data, format='json')
        print(f"Attempted to create person with invalid data  {response}")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)