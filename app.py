import random
from bottle import get, route, run, response, abort


@get('/favicon.ico')
def get_favicon():

    response.content_type = 'image/x-icon'

    return "data:image/x-icon;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQEAYAAABPYyMiAAAABmJLR0T///////8JWPfcAAAACXBIWXMAAABIAAAASABGyWs+AAAAF0lEQVRIx2NgGAWjYBSMglEwCkbBSAcACBAAAeaR9cIAAAAASUVORK5CYII="


@route("/healthz")
def healthz():

    if random.randint(1, 10) < 4:
        abort(500, "Internal Server Error")
    else:
        return "ok"


@route("/liveness/<num:int>")
@route("/readiness/<num:int>")
@route("/startup/<num:int>")
def probe(num=10):

    r = random.randint(1, 100)
    if r < num:
        abort(500, f"Internal Server Error - {r=}")
    else:
        return f"ok - {r=}"


@route('<url:re:.*>')
def hello(url='/'):
    return "ok"


run(host='0.0.0.0', port=8081, debug=True)
