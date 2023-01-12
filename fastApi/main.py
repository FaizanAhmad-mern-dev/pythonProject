# import unicorn

# if __name__=='__main__':
#     unicorn.run('app.app:app', host= '127.0.0.1', port = 8000, reload= True )


from fastapi import FastAPI

from typing import Union


app = FastAPI()

print('main file called')
print('__name__')
print(__name__)

@app.get('/')
def index():
    return 'hey'





# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}