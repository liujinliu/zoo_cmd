all:
	@echo "do nothing"

clean:
	rm -f `find . -type f -name '*.py[co]' `
	rm -fr */*.egg-info build dist

build: clean
	python setup.py build_py bdist_wheel
	cp Makefile dist

install: build
	pip install dist/*.whl -U

install_whl: install

deploy:
	pip install *.whl -U

release-major:
	python setup.py release major

release-minor:
	python setup.py release minor

release-patch:
	python setup.py release patch

.PHONY : all clean build install install_whl release-major release-minor release-patch
