# импортируем необходимые сущности библиотеки bottle
import sentry_sdk
from bottle import route
from bottle import run
from bottle import Bottle
import os

from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://2dd79c753bbb4bed9a9a21fca350997d@o438463.ingest.sentry.io/5406686",
    integrations=[BottleIntegration()]
)
app = Bottle()
@app.route("/success")
def hello_world():
        return "Success World!"  # Возвращаем приветственное сообщение
@app.route("/fail")
def fail_word():
    raise RuntimeError("There is an error!")
    return

@app.route("/")
def index():
    return("Ok")

if __name__ == "__main__":

    if os.environ.get("APP_LOCATION") == "heroku":
        app.run(
            host="0.0.0.0",
            port=int(os.environ.get("PORT", 5000)),
            server="gunicorn",
            workers=3,
        )
    else:
        app.run(host="localhost", port=8080, debug=True)