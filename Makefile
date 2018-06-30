shell:
	./manage.py shell

run:
	./manage.py runserver

install:
	~/.virtualenvs/djangogirls/bin/pip install $(pkgs)

test:
	./manage.py test $(apps)

