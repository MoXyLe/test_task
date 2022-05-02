from pydantic import BaseModel


class QuestionCreate(BaseModel):
    question_id: int
    question_text: str
    answer_text: str
    value: int
    time_created: str

    class Config:
        orm_mode = True


class QuestionGet(QuestionCreate):
    id: int

    class Config:
        orm_mode = True