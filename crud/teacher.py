from sqlalchemy.orm import Session

from models import teacher as models
from crud import teacher as schemas


def get_teacher(db: Session, lid: str):
    return db.query(models.teacher).filter(models.teacher.lid == lid).first()


def create_teacher(db: Session, pmaster: schemas.pmaster):
    db_teacher = models.teacher(
        lid=pmaster.lid,
        fname=pmaster.fname,
        lname=pmaster.lname,
        id =pmaster.id,
        department=pmaster.department,
        major=pmaster.major,
        birth=pmaster.birth,
        borncity=pmaster.borncity,
        address=pmaster.address,
        postalcode=pmaster.postalcode,
        cphone=pmaster.cphone,
        hphone=pmaster.hphone,
        lcourseids=pmaster.lcourseids)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher


def delete_teacher(db: Session, lid: str):
    master = db.query(models.teacher).filter(models.teacher.lid == lid).first()
    if master:
        db.delete(master)
        db.commit()
        return True


def update_master(db: Session, lid: str, updated_data: schemas.teacherupdate):
    db_teacher = db.query(models.teacher).filter(models.teacher.lid == lid).first()
    if db_teacher:
        for field, value in updated_data.dict(exclude_unset=True).items():
            setattr(db_teacher, field, value)
        db.commit()
        db.refresh(db_teacher)
        return db_teacher
    return None
