from fastapi import FastAPI
import uvicorn
from dblib.querydb import querydb

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello! Welcome to New York City and welcome to the Museum of Modern Art! This is one of the greates art galleries in the world. Before stepping into MoMA, which country's artists are you intereted in?"}



@app.get("/query")
async def query():
    """Execute a SQL query from artist database to find artists of a certain country"""

    result = querydb()
    return {"THE ARTISTS": result}

@app.get("/Canadian")
async def query():
    """Execute a SQL query from artist database to find artists of a certain country"""

    result = querydb(Canadian)
    return {"THE ARTISTS": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")