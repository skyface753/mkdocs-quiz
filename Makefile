
install:
	python3 -m pip install --upgrade .

build-plugin:
	python3 -m build

upload:
	python3 -m twine upload dist/*

clean:
	rm -rf build dist mkdocs_quiz.egg-info

build-and-upload: clean build-plugin upload

run-example:
	mkdocs serve -f example/mkdocs.yml

dev: test install run-example

test: 
	python -m mkdocs_quiz.plugin