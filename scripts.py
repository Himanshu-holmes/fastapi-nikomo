import pymongo
import json
import os
from dotenv import load_dotenv

load_dotenv()

mongo_url = os.getenv("MONGO_URL")

# Connect to MongoDB
client = pymongo.MongoClient(mongo_url)
db = client["courses"]
collection = db["courses"]

# Read courses from courses.json
with open("courses.json", "r") as f:
    courses = json.load(f)

# Create index for efficient retrieval
collection.create_index("name")

# add rating field to each course
for course in courses:
    course['rating'] = {'total': 0, 'count': 0}

# add rating field to each chapter
for course in courses:
    for chapter in course['chapters']:
        chapter['rating'] = {'total': 0, 'count': 0}

# Add courses to collection
for course in courses:
    collection.insert_one(course)

# Close MongoDB connection
client.close()