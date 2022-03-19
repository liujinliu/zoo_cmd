all:
	@echo "do nothing"

clean:
	rm -f `find . -type f -name '*.py[co]' `
	rm -fr */*.egg-info build dist

build: clean
	python setup.py build_py bdist_wheel

install: build
	pip install dist/*.whl -U

install_whl: install

uninstall: clean
	pip uninstall -y zoo_cmd 

upload:
	twine upload -r testpypi dist/*.whl

uploadpypi:
	twine upload -r pypi dist/*.whl

install-test:
	pip install zoo_cmd==${TEST_VERSION} --index-url https://test.pypi.org/simple/

.PHONY : all clean build install install_whl
