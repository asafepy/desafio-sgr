

seed:
	./manage.py loaddata resources/seeds/seed_auth.json
	./manage.py loaddata resources/seeds/seed_radio.json
	./manage.py loaddata resources/seeds/seed_programa.json
	./manage.py loaddata resources/seeds/seed_programacao.json


migrate:
	./manage.py makemigrations
	./manage.py migrate