# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# async def my_first_get_api():
#     return {"message":"First FastAPI example"}

from typing import List
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
import models

from fastapi import APIRouter
from fastapi import FastAPI
from database import get_db

app = FastAPI()

# router = APIRouter(
#     prefix='/books',
#     tags=['Books']
# )



@app.get('/')
# This api accepts search criteria and sends back book details for matched criteria
def test_books(book_id:int=None,book_title:str=None, author_name:str=None,page_n:int=0,page_count:int=10, db: Session = Depends(get_db)):

    query = db.query(models.Book).join(models.Book.books_author) 
    if book_id:
        query = query.filter_by(id=book_id)
    if book_title:
        query = query.filter_by(title=book_title)
    if author_name:
        query = query.filter(models.Author.name==author_name)
    start_index = page_n * page_count
    query = query [start_index:page_count]

    resp = {}
    books_rsp = []
    for book in query:
        book_dtls = { "title" : book.title, "download_count" : book.download_count }
        authors = []
        shelves = []
        languanges = []
        subjects = []
        formats = []
        for author in book.books_author:
            authors.append({"author_name" : author.name, "birth_year" : author.birth_year, "death_year" :author.death_year })
        for shelf in book.books_bookshelf:
            shelves.append({"shelf_id" : shelf.id, "shelf_name" : shelf.name})
        for language in book.books_language:
            languanges.append({"language_id" : language.id, "language_code" : language.code})
        for subject in book.books_subject:
            subjects.append({"subject_id" : subject.id, "subject_name" : subject.name})
        for format in book.books_format:
            formats.append({"format_id" : format.id, "mime_type" : format.mime_type, "url" : format.url})

        book_dtls["authors"] = authors
        book_dtls["languages"] = languanges
        book_dtls["shelves"] = shelves
        book_dtls["subjects"] = subjects
        book_dtls["formats"] = formats        
        books_rsp.append(book_dtls)
    resp ["book_list"] = books_rsp
    resp ["page_num"] = page_n
    # resp = { "title" : book.id, "download_count": book.book_id}
        
    return  resp