collectstatic:
	@python manage.py collectstatic --no-input

migrate:
	@python manage.py migrate

migrations:
	@python manage.py makemigrations

sync_roles:
	@python manage.py sync_roles

superuser:
	@python manage.py createsuperuser

runserver:
	@python manage.py runserver