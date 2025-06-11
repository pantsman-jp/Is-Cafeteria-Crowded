build:
	docker build -t is-cafe-crowded .

run:
	docker run --rm -p 5050:5050 \
		-v $(PWD)/cafeteria_status.db:/app/cafeteria_status.db \
		is-cafe-crowded

clean:
	docker rmi is-cafe-crowded || true
