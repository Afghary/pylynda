class Course(object):
    def __init__(self, title, description, topTopic, topic, link, author, authorLink, img, duration, _id=0):
        self.title = title
        self.description = description
        self.topTopic = topTopic
        self.topic = topic
        self.link = link
        self.author = author
        self.authorLink = authorLink
        self.img = img
        self.duration = duration

    @classmethod
    def find_by_topTopic(cls, topTopic):
        courses = Database.find(
            "courses",
            {"topTopic": topTopic}
        )
        return [cls(**course) for course in courses]

    @classmethod
    def find_by_topic(cls,topic):
        courses = Database.find(
            "courses",
            {"topic": topic}
        )
        return [cls(**course) for course in courses]

    def 