# Need to use tabs instead of spaces for indentation ??

.PHONY: build
build: clean frontend pypi

.PHONY: format
format:
	@black streamlit_auth0_component/ setup.py
	@npm run format --prefix ./streamlit_auth0_component/frontend/

.PHONY: frontend
frontend:
	@cd ./streamlit_auth0_component/frontend/ && npm run build

.PHONY: pypi
pypi:
	@python setup.py sdist bdist_wheel

.PHONY: clean
clean:
	@rm -rf ./streamlit_auth0_component/frontend/dist/
	@rm -rf dist/
	@rm -rf build/
	@rm -rf *.egg-info/