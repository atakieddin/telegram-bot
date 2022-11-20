CONTAINER_NAME := telegram_bot
build:
	docker-compose -f docker/docker-compose.yml build
up: build
	docker-compose -f docker/docker-compose.yml up -d
down:
	docker-compose -f docker/docker-compose.yml down
lint:
	docker exec -it ${CONTAINER_NAME} /bin/bash -c 'black telegram_bot && pylint telegram_bot'
shell:
	docker exec -it ${CONTAINER_NAME} /bin/bash