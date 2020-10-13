import random
from bottle import route, run, response, abort

@route("/healthz")
def healthz():
    if random.randint(1, 10) < 4:
        abort(500, "Internal Server Error")
    else:
        return "ok"


@route('<url:re:.*>')
def hello(url='/'):
    return "ok"


run(host='0.0.0.0', port=8081, debug=True)
