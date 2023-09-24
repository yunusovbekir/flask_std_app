# STD finder


### Build and run app
Follow the steps below to run the app in your local

```shell
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

flask run
```

In order to run the app in Docker, follow the below steps

```shell
docker build -t flask_app .
docker run --rm --name app -p 5000:5000 flask_app
```

### Test
After running the application, it'll be available at http://localhost:5000

There are 2 ways the application accepts and returns response.
1) Webpage - http://localhost:5000
2) API - http://localhost:5000/api

Example API request: 

```shell
curl -X POST http://localhost:5000/api -H 'Content-Type: application/json' -d '{"array": "[(1, 2), (-1, 2), (2, 3), (-2, 3), (3, 4), (-3, 4), (4, 5), (-4, 5)]"}'
```