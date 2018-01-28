"""Company - MODELS

"""
from sqlalchemy import Column, String, PickleType

from app.models.base import Base


class WebRequest(Base):

    __tablename__ = 'web_requests'

    uri = Column(String(10), nullable=False)
    data = Column(PickleType())
    ip = Column(String(50))

    def __init__(self, _id=None):
        if _id:
            self.id = _id
            c = self.query.filter(WebRequest.id == self.id).one()
            if c:
                self.__build_obj__(c)

    def __repr__(self):
        return '<WebRequest %r, %r>' % (self.id, self.uri)

    def __build_obj__(self, obj):
        self.id = int(obj.id)
        self.uri = obj.uri
        self.data = obj.data
        self.ip = obj.ip
        self.ts_created = obj.data
        self.ts_updated = obj.ts_updated
