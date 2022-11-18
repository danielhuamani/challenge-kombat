build:
	docker-compose build
up:
	docker-compose up
down:
	docker-compose down
build-test:
	docker-compose -f docker-compose-test.yml build
run-test:
	docker-compose -f docker-compose-test.yml run --rm talana-kombat-test pytest tests/${route} 
