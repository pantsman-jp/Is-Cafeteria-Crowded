# Is_Cafeteria_Crowded / pantsman

## Overview
Kyushu Institute of Technology's cafeteria is known for having extremely crowded periods.
If possible, you would prefer to use the cafeteria during less busy times.

Therefore, I developed a web application that allows cafeteria users to vote on crowding levels,
enabling real-time and predicted crowding status checks for each time slot.

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
