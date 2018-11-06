

loaddata:
	./manage.py loaddata resources/seeds/seed_auth.json


migrate:
	./manage.py makemigrations
	./manage.py migrate