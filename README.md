# Is_Cafeteria_Crowded / pantsman

`This Project Is UNDER CONSTRUCTION`

Users on Kyutech campus can vote on how crowded the cafeteria is.
And users can see real-time and predicted congestion by time of day.

## Installation
Install from <https://github.com/pantsman-jp/Is-Cafeteria-Crowded>

## Usage
### Require
- Docker
- Make

### Build Docker image
```
make build
```

### Run app
To specify a port number, change the port number in `Makefile` and `app.py`.

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
make run
```

## License
Copyright © 2025 pantsman