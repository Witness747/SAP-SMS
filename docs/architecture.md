# SAP-SMS System Architecture

## Overview

Student Academic Planner & Student Management System (SAP-SMS) follows a modern full-stack architecture designed to manage academic activities, learning programs, tasks, and schedules.

The system consists of three major components:

- Frontend: User interface for student interaction
- Backend: Application logic and API services
- Database: Persistent storage of application data

---

# System Components

## 1. Frontend

Responsibilities:

- Provide user interface
- Display academic information
- Allow students to manage courses, tasks, and events
- Communicate with backend APIs

Technology:

- React
- Vite

Location:
frontend/


---

## 2. Backend

Responsibilities:

- Handle business logic
- Provide REST API endpoints
- Validate user requests
- Process DSA-based operations
- Communicate with the database

Technology:

- FastAPI (Python)

Location:
backend/


---

## 3. Database

Responsibilities:

- Store student information
- Store academic records
- Store tasks and schedules
- Maintain relationships between entities

Technology:

- PostgreSQL

Database Name:
sap_sms_db


---

# High-Level Data Flow
Student

↓

React Frontend

↓

FastAPI Backend

↓

PostgreSQL Database

↓

API Response

↓

Frontend Display


---

# Database Architecture

## Database Entities

The SAP-SMS database contains four main entities:

- Student
- Course
- Task
- Event

---

# Student Entity

Purpose:

Stores student profile information.


Table:
students

Columns:

| Column | Description |
|---|---|
| student_id | Primary Key |
| full_name | Student full name |
| email | Unique student email |
| program | Academic program |
| created_at | Record creation timestamp |

Relationship:

A student can have:

- Many courses
- Many tasks
- Many events

---

# Course Entity

Purpose:

Stores academic course information.


Table:
courses

Columns:

| Column | Description |
|---|---|
| course_id | Primary Key |
| student_id | Foreign Key referencing students |
| course_name | Name of course |
| course_code | Course identifier |
| semester | Academic semester |

Relationship:

Each course belongs to one student.

---

# Task Entity

Purpose:

Stores academic and personal tasks.


Table:
tasks

Columns:

| Column | Description |
|---|---|
| task_id | Primary Key |
| student_id | Foreign Key referencing students |
| title | Task name |
| priority | Task importance level |
| status | Task completion state |
| due_date | Deadline |
| created_at | Creation timestamp |

Relationship:

Each task belongs to one student.

---

# Event Entity

Purpose:

Stores scheduled academic and personal activities.

Table:
events


Columns:

| Column | Description |
|---|---|
| event_id | Primary Key |
| student_id | Foreign Key referencing students |
| title | Event name |
| event_type | Category of event |
| start_time | Event starting time |
| end_time | Event ending time |
| created_at | Creation timestamp |

Relationship:

Each event belongs to one student.

---

# Entity Relationship Diagram
             Student

                |

    ----------------------------

    |             |            |

    ↓             ↓            ↓

Courses        Tasks        Events

 (Many)       (Many)       (Many)

 
Formal relationship:
Student (1) ---- (Many) Courses

Student (1) ---- (Many) Tasks

Student (1) ---- (Many) Events


---

# Data Structures and Algorithms Applications

SAP-SMS applies Data Structures and Algorithms to solve practical student management problems.

---

## Sorting Algorithms

Purpose:

Organizing academic information efficiently.

Applications:

- Sorting tasks by priority
- Sorting tasks by deadline
- Sorting events by date and time

Possible algorithms:

- Merge Sort
- Quick Sort

Example:

Before sorting:
Task A - Low Priority
Task B - High Priority
Task C - Medium Priority


After sorting:
Task B - High Priority
Task C - Medium Priority
Task A - Low Priority


---

## Searching Algorithms

Purpose:

Efficient retrieval of stored information.

Applications:

- Searching tasks
- Searching courses
- Searching events

Possible approaches:

- Linear Search
- Binary Search (when data is sorted)

---

## Hash Maps

Purpose:

Fast data lookup.

Applications:

- Retrieving student-related records
- Mapping student information with tasks, courses, and events

Example:
Student ID → Student Information


---

## Schedule Conflict Detection

Purpose:

Identify overlapping events.

Example:
Event A:

10:00 - 11:00

Event B:

10:30 - 12:00


Comparison:
10:30 overlaps with 11:00


Result:
Schedule Conflict Detected


The algorithm compares event time intervals to identify conflicts.

---

# Future Architecture Enhancements

Future versions may include:

- AI-powered schedule recommendations
- Automatic timetable optimization
- Time-zone conversion engine
- Calendar synchronization
- Academic analytics
- Institution-level management



