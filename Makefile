build:
	docker-compose build
up:
	docker-compose up
down:
	docker-compose down
run-test:
	docker-compose run --rm talana-kombat pytest tests/${route} 
