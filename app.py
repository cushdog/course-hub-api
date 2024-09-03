from PL import retrieve_assignments, retrieve_all
from flask import Flask, request, jsonify
from dateCat import retrieve_events
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from canvasapi import Canvas
from flask_cors import CORS
import requests
import os

load_dotenv('.env.local')

API_URL = "https://canvas.illinois.edu/"
API_KEY = os.getenv('CANVAS_API_KEY')

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

def init_canvas_obj(access_token):
    canvas = Canvas(API_URL, access_token)
    user = canvas.get_current_user()
    return user

@app.route('/canvasCourse', methods=['GET'])
def profSearch():
    query = request.args.get('query')

    user = init_canvas_obj(query)
    courses = user.get_courses(enrollment_state='active')

    return jsonify(courses)

@app.route('/canvasAssignments', methods=['GET'])
def profSearch():
    query = request.args.get('query')

    user = init_canvas_obj(query)
    courses = user.get_courses(enrollment_state='active')

    assignments_final = []

    # Iterate through each course
    for course in courses:
        print(f"Course: {course.name}")
        
        # Get all assignments for the course
        assignments = course.get_assignments()
        
        # Iterate through each assignment
        for assignment in assignments:
            print(f"    Assignment: {assignment.name}")
            print(f"    Due: {assignment.due_at}")
            print(f"    Points: {assignment.points_possible}")
            print(f"    Submission type: {assignment.submission_types}")
            assignment_info = {
                "course": course.name,
                "name": assignment.name,
                "due": assignment.due_at,
                "points": assignment.points_possible,
                "submission_type": assignment.submission_types
            }
            assignments_final.append(assignment_info)

            
        print("\n")  # Add a new line between courses
    
    return jsonify(assignments_final)

@app.route('/plAssignments-search', methods=['GET'])
def plAssignments():
    query = request.args.get('query')
    assignments = retrieve_assignments(query)
    return jsonify(assignments)

@app.route('/plAssignments-all', methods=['GET'])
def plAssignmentsAll():
    assignments = retrieve_all()
    return jsonify(assignments)

@app.route('/dateCat', methods=['GET'])
def dateCat():
    date_cat_assignments = retrieve_events()
    return jsonify(date_cat_assignments)

if __name__ == '__main__':
    app.run(debug=True)
