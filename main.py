from fastapi import FastAPI

app = FastAPI()

@app.get("/values_for_GPT/")
async def read_items(val1: int, val2: int, val3: int | None):

    val = sum([val1, val2, val3])
    query_items = {"val": val}
    return query_items