from sqlalchemy.orm import Session
from . import schema, models


def save_question(db: Session, question: schema.QuestionCreate):
    question_model = models.Question(**question.dict())
    db.add(question_model)
    db.commit()
    db.refresh(question_model)
    return question_model


def get_question(db: Session, id: int = None, last: bool = False):
    if last:
        return db.query(models.Question).order_by(models.Question.id.desc()).first()
    if id is None:
        return db.query(models.Question).order_by(models.Question.id.desc()).all()
    else:
        return db.query(models.Question).filter(models.Question.question_id == id).first()
