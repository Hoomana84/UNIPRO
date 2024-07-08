from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from fast1 import models, schemas, crud
from fast1.database import SessionLocal, engine
from models import course as models
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/GetCou/{course_id}")
def read_course(course_id: str, cousre_id = course_id, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id =course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course


@app.post("/RegCou/")
def create_course(course: schemas.Course, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=course.id)
    if db_course:
        raise HTTPException(status_code=400, detail="Course already exists")
    return crud.create_course(db=db, course=course)


@app.put("/UpdCou/{cid}")
def update_course(cid: int, course: schemas.Course, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=cid)
    if not db_course:
        raise HTTPException(status_code=400, detail="student does not exist")
    return crud.update_course(db=db, course=cid)


@app.delete("/deleteCou/{cid}")
def delete_course(cid: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=delete_course)
    if not db_course:
        raise HTTPException(status_code=400, detail="Course not found")
    return crud.delete_course(db=db, course_id=cid)

