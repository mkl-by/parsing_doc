from models import Document
from sqlalchemy import func
import datetime
#from app import db

class Search_document():
    def __init__(self, name_doc=None, number_doc=None, page=None):
        self.name_doc=name_doc
        self.number_doc=number_doc
        self.page=page


    def paginate_err(self):
        #готовим пагинацию
        # if page and page.isdigit():
        #     page=int(page)
        # else:
        #     page=1
        self.pagint = self.post.paginate(page=self.page, per_page=10)
        return self.pagint

    def get_search_doc_pag(self, name, page):
        #достаем из базы по названию или по номеру
        self.name_doc=name
        self.page=page
        self.post = Document.query.filter(Document.docname.contains(self.name_doc))#.all()
        # post = Document.query.filter(Document.docname in self.name_doc)
        if self.post==[]:
            self.post = Document.query.filter(Document.number.contains(self.name_doc))#.all()
        self.posts=self.paginate_err()
        return self.posts

    def get_search_doc(self, name):
        #достаем из базы по названию или по номеру
        self.name_doc=name
        post = Document.query.filter(Document.docname.contains(self.name_doc)).all()
        # post = Document.query.filter(Document.docname in self.name_doc)
        if post==[]:
            post = Document.query.filter(Document.number.contains(self.name_doc)).all()

        return post

    def get_search_data(self, d):
        #ищем запись по дате
        post= Document.query.filter(Document.date_doc==d).all()
        return post

    def get_search_range_data(self, d1, d2):
        #ищем запись в диапазоне дат
        post= Document.query.filter(Document.date_doc>=d1, Document.date_doc<=d2).all()
        return post

    def get_all(self,page):
        self.page=page
        self.post=Document.query
        self.posts = self.paginate_err()
        return self.posts


