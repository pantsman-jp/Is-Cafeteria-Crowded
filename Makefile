build:
	docker build -t is-cafe-crowded .

run:
	docker run --rm -p 5004:5004 \
		-v $(PWD)/cafeteria_status.db:/app/cafeteria_status.db \
		is-cafe-crowded

devrun:
	docker run --rm -p 5004:5004 \
		-v $(PWD):/app \
		is-cafe-crowded

init:
	python init_db.py

clean:
	docker rmi is-cafe-crowded || true
