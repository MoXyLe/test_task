from .database import Base
from sqlalchemy import Column, String, Integer, DateTime


class Question(Base):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer)
    question_text = Column(String)
    answer_text = Column(String)
    value = Column(Integer)
    time_created = Column(DateTime(timezone=True))
