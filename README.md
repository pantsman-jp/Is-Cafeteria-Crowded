# Is_Cafeteria_Crowded / pantsman

Users on Kyutech campus can vote on how crowded the cafeteria is.
And users can see real-time and predicted congestion by time of day.

## Installation
Download from https://github.com/pantsman-jp/Is-Cafeteria-Crowded.

## Usage
### 0. Require
You need
- Docker
- Make

### 1. Initialize DB
When starting up for the first time (or you want to initialize the database),
the database must be initialized. Execute the following command.
```
% make init
```

### 2. Build Docker Image
```
% make build
```

### 3. Run App
To specify a port number, change the port number in `Makefile` and `app.py`.
Default port is `5004`.

Makefile
```Makefile
run:
	docker run --rm -p port:port \
		-v $(PWD)/cafeteria_status.db:/app/cafeteria_status.db \
		is-cafe-crowded
```

app.py
```Python app.py
port = 5004
if __name__ == "__main__":
    start_server(port=port)
```

Then run app.
```
% make run
```

## License
Copyright © 2025 pantsman