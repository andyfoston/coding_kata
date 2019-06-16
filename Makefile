build:
	python3 setup.py sdist
clean:
	rm -r ./dist/
clean-all: clean
	find . -name ".coverage" -exec rm {} \;
	find . -name "*.pyc" -exec rm {} \;
lint:
	pylint basic_arithmetic.py
test:
	python3 test_basic_arithmetic.py
test-coverage:
	coverage run test_basic_arithmetic.py
	coverage report
docker-run:
	docker build \
	  --file=./Dockerfile \
	  --tag=coding_kata ./
	docker run --rm \
	  --detach=false \
	  --name=coding_kata \
	  coding_kata ${ARGS}