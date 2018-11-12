.SILENT:

install: migrate seed test server

migrate:
	./manage.py makemigrations
	./manage.py migrate

seed:
	./manage.py loaddata resources/seeds/seed_user.json
	./manage.py loaddata resources/seeds/seed_radio.json
	./manage.py loaddata resources/seeds/seed_programa.json
	./manage.py loaddata resources/seeds/seed_grade.json
	./manage.py loaddata resources/seeds/seed_grade_programacao.json

test:
	./manage.py test

server:
	./manage.py runserver 127.0.0.1:8080 > /dev/null 2>&1 & echo 'Server Created on <http://127.0.0.1:8080>'

server_stop:
	kill `(lsof -t -i:8080)` & echo 'Server Stopped!'