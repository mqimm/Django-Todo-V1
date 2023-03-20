Python 3.8 o higher

# ubuntu package
sudo apt install -y python3-venv python-is-python3

# Installation
pip install -r requirements.txt

# Generate Private Key
python manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())

Copy the key and add to app/setting.py
SECRET_KEY = 'KEY'

# Migrate
./manage.py migrate

# Run Application
./manage.py runserver

