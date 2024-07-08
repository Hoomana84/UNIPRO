from sqlalchemy.orm import Session

from models import student as models
from schemas import teacher as schemas
from fast1 import schemas, models

def get_stu(db: Session, stid: str):
    return db.query(models.student).filter(models.student.STID== STID).first()


def create_student(db: Session, student: schemas.student):
    db_student = models.student(
        STID=student.stid,
        fname=student.fname,
        lname= student.lname,
        father=student.father,
        birth=student.birth,
        ids=student.ids,
        borncity=student.borncity,
        address=student.address,
        postalcode=student.postalcode,
        cphone=student.cphone,
        hphone=student.hphone,
        department=student.department,
        major=student.major,
        married=student.married,
        id=student.id,
        scourseids=student.scourseids,
        lids=student.lids)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def delete_student(db: Session, stid: str):
    student = db.query(models.student).filter(models.student.stid == stid).first()
    if student:
        db.delete(student)
        db.commit()
        return True


def update_student(db: Session, stid: str, updated_data: schemas.studentupdate):
    db_student = db.query(models.student).filter(models.student.stid == stid).first()
    if db_student:
        for field, value in updated_data.dict(exclude_unset=True).items():
            setattr(db_student, field, value)
        db.commit()
        db.refresh(db_student)
        return db_student
    return None