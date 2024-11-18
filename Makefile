PROJECT_DIR ?= UrbanDjango

run:
	cd $(PROJECT_DIR) && python manage.py migrate
	cd $(PROJECT_DIR) && python manage.py runserver