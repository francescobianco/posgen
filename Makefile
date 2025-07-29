
init:
	@python3 -m venv .venv
	@. .venv/bin/activate
	@pip3 install -r requirements.txt

push:
	@git add .
	@git commit -am "New release!" || true
	@git push

test:
	python3 main.py