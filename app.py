import random
from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()


@app.get('/favicon.ico')
def get_favicon():
    return {
        "favicon": "data:image/x-icon;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQEAYAAABPYyMiAAAABmJLR0T///////8JWPfcAAAACXBIWXMAAABIAAAASABGyWs+AAAAF0lEQVRIx2NgGAWjYBSMglEwCkbBSAcACBAAAeaR9cIAAAAASUVORK5CYII="
    }


@app.get("/healthz")
def healthz():
    if random.randint(1, 10) < 4:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    else:
        return {"status": "ok"}


@app.get("/liveness/{num}")
@app.get("/readiness/{num}")
@app.get("/startup/{num}")
def probe(num: int = 10):
    r = random.randint(1, 100)
    if r < num:
        raise HTTPException(
            status_code=500, detail=f"Internal Server Error - {r=}"
        )
    else:
        return {"status": f"ok - {r=}"}


@app.get("/{url:path}")
def hello(url: str = ""):
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
