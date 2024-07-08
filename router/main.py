from fastapi import Depends, FastAPI, HTTPException,APIRouter
from sqlalchemy.orm import Session

from fast1 import models, schemas, crud
from fast1.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/GetCou/{course_id}")
def read_course(course_id: str, cousre_id = course_id, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id =course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course


@router.post("/RegCou/")
def create_course(course: schemas.Course, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=course.id)
    if db_course:
        raise HTTPException(status_code=400, detail="Course already exists")
    return crud.create_course(db=db, course=course)


@router.put("/UpdCou/{cid}")
def update_course(cid: int, course: schemas.Course, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=cid)
    if not db_course:
        raise HTTPException(status_code=400, detail="student does not exist")
    return crud.update_course(db=db, course=cid)


@router.delete("/deleteCou/{cid}")
def delete_course(cid: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=delete_course)
    if not db_course:
        raise HTTPException(status_code=400, detail="Course not found")
    return crud.delete_course(db=db, course_id=cid)


# student

@router.get("/GetStudent/{student_id}")
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="This Student not found")
    return db_student


@router.post("/RegStu/")
def create_student(student: schemas.Student, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student.vaild_ID)
    if db_student:
        raise HTTPException(status_code=400, detail="This student already rejistered")
    return crud.create_student(db=db, student=student)


@router.put("/updateStu/{STID}")
def update_student(STID: int, student: schemas.Student, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=STID)
    if not db_student:
        raise HTTPException(status_code=400, detail="student is not found!")
    return crud.update_student(db=db, student_id=STID, student=student)


@router.delete("/deleteStu/{STID}")
def delete_student(STID: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=STID)
    if not db_student:
        raise HTTPException(status_code=400, detail="student not found!")
    return crud.delete_student(db=db, student_id=STID)


# Teacher


@router.get("/GetTeacher/{LID}")
def read_teacher(teacher_id: int, db: Session = Depends(get_db)):
    db_teacher = crud.get_teacher(db, teacher_id=teacher_id)
    if db_teacher is None:
        raise HTTPException(status_code=404, detail=" Teacher not found")
    return db_teacher


@router.post("/RegTeacher/")
def create_teacher(teacher: schemas.Teacher, db: Session = Depends(get_db)):
    db_teacher = crud.get_teacher(db, teacher_id=teacher.id)
    if db_teacher:
        raise HTTPException(status_code=400, detail=" teacher already exists")
    return crud.create_teacher(db=db, teacher=teacher)


@router.put("updateteacher/{LID}")
def update_teacher(LID: int, teacher: schemas.Teacher, db: Session = Depends(get_db)):
    db_teacher = crud.get_teacher(db, teacher_id=teacher_id)
    if not db_teacher:
        raise HTTPException(status_code=400, detail="This teacher not founded!")
    return crud.update_teacher(db=db, teacher_id=LID, teacher=teacher)


@router.delete("/deleteTeacher/{LID}")
def delete_teacher(LID: int, teacher_id= teacher_id, db: Session = Depends(get_db)):
    db_teachers = crud.get_teacher(db, teacher_id=teacher_id)
    if not db_teachers:
        raise HTTPException(status_code=400, detail="This teacher not founded!")
    return delete.db_teacher(db=db, teacher_id=teacher_id)
