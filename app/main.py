from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
from .database import SessionLocal, engine
from sqlalchemy.orm import Session
from .schema import QuestionCreate
from . import crud, models
import requests
import pydantic
from typing import Optional

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post('/questions')
async def post_questions(question_num: int, background_tasks: BackgroundTasks, db: Session = Depends(db)):
    background_tasks.add_task(get_new_questions, question_num=question_num, db=db)
    last_question = crud.get_question(db=db, last=True)
    return last_question


@app.get('/questions')
async def get_questions(question_id: Optional[int] = None, db: Session = Depends(db)):
    if question_id is not None:
        question = crud.get_question(db=db, id=int(question_id))
        if question:
            return question
        raise HTTPException(status_code=400, detail="Question with specified id not found")
    all_questions = crud.get_question(db=db)
    if all_questions:
        return all_questions
    raise HTTPException(status_code=400, detail="Question with specified id not found")


def get_new_questions(question_num: int, db: Session):
    json = requests.get("https://jservice.io/api/random?count=" + str(question_num)).json()
    new_questions = 0
    for i in json:
        new_questions = new_question_to_db(db=db, i=i, new_questions=new_questions)
    while new_questions < question_num:
        json = requests.get("https://jservice.io/api/random?count=" + str(question_num - new_questions)).json()
        for i in json:
            new_questions = new_question_to_db(db=db, i=i, new_questions=new_questions)


def new_question_to_db(db: Session, i: dict, new_questions: int):
    if crud.get_question(db=db, id=i['id']) is None:
        try:
            db_question = QuestionCreate(question_id=i['id'], question_text=i['question'], answer_text=i['answer'],
                                         value=i['value'], time_created=i['created_at'])
            crud.save_question(db=db, question=db_question)
            new_questions += 1
        except pydantic.error_wrappers.ValidationError:
            print("Can't save new question")
    return new_questions
