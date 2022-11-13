migrate:
	@python testmanage.py migrate

admin:
	@echo "Creating superuser"
	@echo "from django.contrib.auth import get_user_model; get_user_model().objects.create_superuser('test', '', 'test')" | python testmanage.py shell

run:
	@python testmanage.py runserver 0.0.0.0:8000

test:
	@echo "Running tests..."
	@python testmanage.py test --deprecation all

setup:
	@echo "Setting up test environment..."
	@pip install -e ".[testing,dev]"
	@make migrate
	@make admin
