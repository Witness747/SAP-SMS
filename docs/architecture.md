## Database Entities

### Student

A student can have many courses.

A student can have many tasks.

A student can have many events.

### Course

Each course belongs to one student.

### Task

Each task belongs to one student.

### Event

Each event belongs to one student.

---

## Entity Relationships

Student (1) ---- (Many) Course

Student (1) ---- (Many) Task

Student (1) ---- (Many) Event



## DSA Applications

### Sorting

Used for:

* Sorting tasks by priority
* Sorting tasks by deadline
* Sorting events by date and time

### Searching

Used for:

* Searching tasks
* Searching events
* Searching courses

### Hash Maps

Used for:

* Fast retrieval of student-related records

### Conflict Detection

Used for:

* Detecting overlapping events

Example:

Event A:
10:00 - 11:00

Event B:
10:30 - 12:00

Result:

Schedule Conflict Detected
