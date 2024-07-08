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


@app.get("/GetStudent/{student_id}")
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student


@app.post("/RegStu/")
def create_student(student: schemas.Student, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student.vaild_ID)
    if db_student:
        raise HTTPException(status_code=400, detail="Student already rejistered")
    return crud.create_student(db=db, student=student)


@app.put("/updateStu/{STID}")
def update_student(STID: int, student: schemas.Student, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=STID)
    if not db_student:
        raise HTTPException(status_code=400, detail="Student is not found!")
    return crud.update_student(db=db, student_id=STID, student=student)


@app.delete("/deleteStu/{STID}")
def delete_student(STID: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=STID)
    if not db_student:
        raise HTTPException(status_code=400, detail="Student not found!")
    return crud.delete_student(db=db, student_id=STID)

