

seed:
	./manage.py loaddata resources/seeds/seed_auth.json
	./manage.py loaddata resources/seeds/seed_radio.json
	./manage.py loaddata resources/seeds/seed_programas.json


migrate:
	./manage.py makemigrations
	./manage.py migrate