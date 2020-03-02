all: clean build clean

build:
	python setup.py sdist bdist_egg bdist_wheel

test-deploy: clean build
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

deploy: clean build
	twine upload dist/*

install: build
	python setup.py install


clean:
	rm -rf *.zip
	rm -rf *.tar.gz
	rm -rf *.7z
	rm -rf *.rar
	rm -rf *.exe
	rm -rf build/
	rm -rf dist/
	rm -rf _book/
	rm -rf *.egg-info