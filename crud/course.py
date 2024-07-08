from sqlalchemy.orm import Session

from models import course as models
from schemas import course as schemas


def get_Course(db: Session, course_id: int):
    return db.query(models.course).filter(models.course.id == course_id).first()


def create_course(db: Session, course: schemas.course):
    db_course = models.course(CID=course.CID,
                              CName=course.CName,
                              Department=course.Department,
                              Credit=course.Credit)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


def delete_course(db: Session, course_id: int):
    course = db.query(models.course).filter(models.course.id == course_id).first()
    if course:
        db.delete(course)
        db.commit()
        return True


def update_course(db: Session, course_id: int, course_update: schemas.courseUpdate):
    course = db.query(models.course).filter(models.course.id == course_id).first()
    if not course:
        return None

    update_data = course_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(course, key, value)

    db.add(course)
    db.commit()
    db.refresh(course)
    return course
