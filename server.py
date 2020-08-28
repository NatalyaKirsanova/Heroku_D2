# импортируем необходимые сущности библиотеки bottle
import sentry_sdk
from bottle import route
from bottle import run
import os

from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://2dd79c753bbb4bed9a9a21fca350997d@o438463.ingest.sentry.io/5406686",
    integrations=[BottleIntegration()]
)
# app = Bottle()
@route("/success")
def hello_world():
        return "Success World!"  # Возвращаем приветственное сообщение
@route("/fail")
def fail_word():
    raise RuntimeError("There is an error!")
    return

if __name__ == "__main__":

    if os.environ.get("APP_LOCATION") == "heroku":
        run(
            host="0.0.0.0",
            port=int(os.environ.get("PORT", 5000)),
            server="gunicorn",
            workers=3,
        )
    else:
        run(host="localhost", port=8080, debug=True)