from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "The orangutans are three extant species of great apes native to Indonesia and Malaysia."}

@app.get('/hello/{who}')
async def hey(who):
    return f'Hello {who}?'