from fastapi import FastAPI, Path, Query
import uvicorn


app = FastAPI() #FastAPI物件

@app.get("/users/")
async def get_user(page_index: int = Query(1,
                                       alias="page-index",
                                       title = "page index",
                                       ge = 1,
                                       le = 10000)):
    return {"page_index": f"index {page_index}"}
# ge >= gt> le<= lt<

@app.get("/users/{user_id}")
async def get_user(user_id: int = Path(...,
                                       title = "the user id",
                                       ge = 1,
                                       le = 10000)):
    return {"user_id": f"this is a user for {user_id}"}

@app.get('/books/{book_name}')
async def get_book_name(book_name: str = Path(...,
                                            title = "book name",
                                            min_length = 3,
                                            max_length = 10)):
    return {'student': f'This is a book for {book_name}'}

@app.get('/items/{items_number}')
async def get_items(items_number: str = Path(...,
                                           title = "items number",
                                            regex = '^[a|b|c]-[\\d]*$'
                                           )):
    return {'student': f'This is a item for {items_number} '}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)