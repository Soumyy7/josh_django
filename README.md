# Task Management System

![image](https://github.com/user-attachments/assets/abea3167-199f-4a40-8e0d-96386f210f48)


## Overview
This is a Django-based Task Management System that allows users to create, assign, and track tasks. It includes both a web interface and a REST API.

## Features
1. Task creation, and status tracking using apis /tasks/create & /tasks/assign
2. Task assignment, many to many. One task can be assigned to multiple users and a user can be assigned to multiple tasks.
3. User-based task filtering using apis /tasks/user/<username>
4. Admin panel for managing users and tasks (sudo admin credentials and login process given below)

---

## Setup Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/Soumyy7/josh_django.git
cd task-management
```

 ### Or download the zip file, extract the files, open the repository in VS Code or any other editor and follow the below given steps

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Development Server
```bash
python manage.py runserver
```
Access the application at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## API Endpoints
### 1. Get All Tasks
**Request:**
```http
GET /tasks/
```
**Response:**
```json
[
  {
    "id": 1,
    "name": "Complete Report",
    "status": "Pending",
    "assigned_users": ["user1", "user2"]
  }
]
```
![image](https://github.com/user-attachments/assets/83d6a236-6091-486e-a4c3-fef866478a70)


### 2. Get Tasks for a Specific User
**Request:**
```http
GET /tasks/user/<username>/
```

![image](https://github.com/user-attachments/assets/d51c24c3-757f-499c-8b21-23365bf883cb)


the list of users created are: 
vishal
sidharth
george
jason
varun
sudo_user
soumy

### 3. Create a Task
**Request:**
```http
POST /tasks/create/
Content-Type: application/json

{
  "name": "New Task",
  "status": "Pending",
  "task_type": "Development",
  "assigned_to": "soumy",
}
```
![image](https://github.com/user-attachments/assets/1af0a307-722f-4ff2-af0f-d87a53e7646e) ![image](https://github.com/user-attachments/assets/9b43c4ec-8168-4ffe-b905-e7418ff92ce8)


### 4. Assign a Task to a User
**Request:**
```http
POST /tasks/assign/
Content-Type: application/json

{
  "task_id": 1,
  "user_id": 2
}
```

![image](https://github.com/user-attachments/assets/388d612d-9d22-4526-8ae3-6e46197277c1)


---

## Test Credentials
- **Username:** `sudo_user`
- **Password:** `India@9090`

---

## Accessing the Admin Panel
URL: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

Login using the test credentials above or your create your own superuser.

---

## Notes
- Ensure `APPEND_SLASH = True` in `settings.py` to avoid routing issues.
- For API testing, use [Postman](https://www.postman.com/) or `curl`.
- If needed, install and configure CORS for cross-origin API requests.

---
