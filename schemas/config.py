from fastapi import FastAPI
from routers import Course,student,teacher


app = FastAPI()
app.include_router(Course.router, tags=["Courses"])
app.include_router(student.router, tags=["Students"])
app.include_router(teacher.router, tags=["Teacheers"])