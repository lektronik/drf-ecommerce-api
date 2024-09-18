import requests
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Make an authenticated request to the API'

    def handle(self, *args, **kwargs):
        # Obtain the token
        login_url = 'http://127.0.0.1:8000/api/auth/login/'
        login_data = {
            'username': 'your_username',  # Replace with the correct username
            'password': 'your_password'   # Replace with the correct password
        }
        response = requests.post(login_url, data=login_data)
        if response.status_code != 200:
            self.stdout.write(self.style.ERROR(f'Failed to obtain token: {response.status_code} {response.text}'))
            return

        token = response.json().get('key')
        if not token:
            self.stdout.write(self.style.ERROR('Token not found in response'))
            return

        # Make an authenticated request
        api_url = 'http://127.0.0.1:8000/api/printify/products/'
        headers = {
            'Authorization': f'Token {token}'
        }
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            self.stdout.write(self.style.SUCCESS('Authenticated request successful'))
            self.stdout.write(self.style.SUCCESS(response.json()))
        else:
            self.stdout.write(self.style.ERROR(f'Authenticated request failed: {response.status_code} {response.text}'))
