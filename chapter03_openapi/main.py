from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello":"world"}


items = {
    0: {"name":"bread", "price":1000},
    1: {"name":"milk", "price":500},
    2: {"name":"water", "price":100}    
}

@app.get("/item/{item_id}")
def read_item(item_id:int):
    item = items[item_id]
    return item

