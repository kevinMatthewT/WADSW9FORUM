from fastapi import FastAPI, Cookie ,Header

app=FastAPI()

@app.get('/todos')
def gettodo(cookie_id: str | None= Cookie(None)):
    return {"cookie_id":cookie_id}
