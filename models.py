from app import db

class Document(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    number = db.Column(db.String(20))
    instance = db.Column(db.SmallInteger)
    docname = db.Column(db.String(120))
    page=db.Column(db.String(7))
    case_number = db.Column(db.SmallInteger)
    case_tom = db.Column(db.SmallInteger)
    case = db.Column(db.String(120))
    date_doc=db.Column(db.Date)

    def __init__(self, *args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)
        self.set_case()

    def set_case(self):

        if self.case_number==1:
            self.case='case number 1'
        elif self.case_number==2:
            self.case='case number 2'
        elif self.case_number==3:
            self.case='case number 3'


    def __repr__(self):
        return 'id - {0}, nUmber - {2}, docname - {1}, instance - {6}, page - {7}, case_number - {3}, ' \
               'case - {4}, case_tom - {8}, date_doc - {5}'.format(self.id, self.docname, self.number,
                                    self.case_number, self.case, self.date_doc, self.instance, self.page, self.case_tom)


# class Opis(db.model):
#     id = db.Column(db.Integer, primary_key=True)
#     number_case = db.Column(db.String(20))
#     data_begin=db.Column(db.Date)
#     data_end=db.Column(db.Date)
#     arhive_number=db.Column(db.String(20))

#для записи информации в базу
# try:
#     aaa = Document(number='6666', docname='kjhksbf,mb ', case='sdfdf', case_tom=2)
#     db.session.add(aaa)
#     db.session.commit()
# except:
#     db.session.rollback()
#     raise
# finally:
#     db.session.close()