import pymongo
import post
import sys
uri="mongodb://127.0.0.1:27017"
client= pymongo.MongoClient(uri)
database=client['fullstack']
collection= database['students']
students=[student['name'] for student in collection.find({})]
# print(students)
sys.module