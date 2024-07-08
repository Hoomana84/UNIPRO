from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from fast1 import models, schemas, crud
from fast1.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/GetTeacher/{LID}")
def read_teacher(teacher_id: int, db: Session = Depends(get_db)):
    db_teacher = crud.get_teacher(db, teacher_id=teacher_id)
    if db_teacher is None:
        raise HTTPException(status_code=404, detail=" Teacher not found")
    return db_teacher


@app.post("/RegTeacher/")
def create_teacher(teacher: schemas.Teacher, db: Session = Depends(get_db)):
    db_teacher = crud.get_teacher(db, teacher_id=teacher.id)
    if db_teacher:
        raise HTTPException(status_code=400, detail=" teacher already exists")
    return crud.create_teacher(db=db, teacher=teacher)


@app.put("updateteacher/{LID}")
def update_teacher(LID: int, teacher: schemas.Teacher, db: Session = Depends(get_db)):
    db_teacher = crud.get_teacher(db, teacher_id=teacher_id)
    if not db_teacher:
        raise HTTPException(status_code=400, detail="This teacher not founded!")
    return crud.update_teacher(db=db, teacher_id=LID, teacher=teacher)


@app.delete("/deleteTeacher/{LID}")
def delete_teacher(LID: int, teacher_id= teacher_id, db: Session = Depends(get_db)):
    db_teachers = crud.get_teacher(db, teacher_id=teacher_id)
    if not db_teachers:
        raise HTTPException(status_code=400, detail="This teacher not founded!")
    return delete.db_teacher(db=db, teacher_id=teacher_id)
