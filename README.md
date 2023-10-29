# wagwanians

## BACK END:

## Running the Server
To run the server locally, execute the following command in a terminal from the root directory of the repository:

```
python3 -m src.server
```

The server will start running on the port specified in the src/config.py file.

## Running Tests
To run tests, open two terminals. In the first terminal, start the server by executing:

```
python3 -m src.server
```

In the second terminal, run the command:

```
python3 -m pytest (specific test file)
```

## FRONT END:
To test frontend run the backend simultaneously in a separate terminal.
Then use the following command to start npm:

```
npm start
```

Use the following command to start the frontend:

```
npm run build
```
