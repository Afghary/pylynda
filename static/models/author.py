from static.common.database import Database
from static.models.course import Course


class Author(object):
    def __init__(self, name, img, link, description, _id=0):
        self.name = name
        self.description = description
        self.link = link
        self.img = img

    def get_courses(self):
        courses = Database.find(collection="authors", query={"author": self.name})
        return [Course(**course) for course in courses]