setup:
	pip install -r requirements.txt

test:
	pytest tests

test-cov:
	pytest tests --cov=light_switch

lint:
	flake8 light_switch
