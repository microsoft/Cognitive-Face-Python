.PHONY: clean deps install lint pep8 pyflakes pylint test

clean:
	find . -name '*.pyc' -print0 | xargs -0 rm -f
	find . -name '*.swp' -print0 | xargs -0 rm -f
	find . -name '__pycache__' -print0 | xargs -0 rm -rf
	-rm -rf build dist *.egg-info

deps:
	pip install -r requirements.txt

install:
	python setup.py install

lint: pep8 pyflakes pylint

pep8:
	-pep8 --statistics --count cognitive_face setup.py

pyflakes:
	-pyflakes cognitive_face setup.py

pylint:
	-pylint --rcfile=.pylintrc cognitive_face setup.py

test:
	python setup.py test
