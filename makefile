down:
	curl -o htmlJinja.py https://raw.githubusercontent.com/Falape/onto2HTML/main/htmlJinja.py
	curl -o onto2HTML https://raw.githubusercontent.com/Falape/onto2HTML/main/onto2HTML
	chmod 755 onto2HTML

bin:
	sudo mv onto2HTML /usr/local/bin/
	sudo mv htmlJinja.py /usr/local/bin/

install:
	pip3 install -U pathlib rdflib

onto2HTML-install: down bin install

onto2HTML-remove:
	sudo rm /usr/local/bin/onto2HTML
	sudo rm /usr/local/bin/htmlJinja.py
