# Task 2 — Backend API
REST API built with **Node.js**, **Express.js**, and **MongoDB Atlas**.
## Requirements
- Node.js v18+
- npm
- MongoDB Atlas account

## Setup

### 1. Install dependencies
```bash
npm install
```

### 2. Configure environment
Create a `.env` file in this folder:

### 3. Start the server
```bash
node server.js
```
Server runs on http://localhost:3000

## API Endpoints

| Method |    Endpoint    |    Description    |
|--------|----------------|-------------------|
| POST   |   /api/users   | Add new user      |
| GET    |   /api/users   | Get all users     |
| GET    | /api/users/:id | Get user by ID    |
| DELETE | /api/users/:id | Delete user by ID |

## Validation Rules
- All fields (fullName, email, password) are required
- Request body must be JSON format
- Email must be unique per user
- Password must be minimum 8 characters

## Test with curl

Add user:
```bash
curl -X POST http://localhost:3000/api/users \
  -H "Content-Type: application/json" \
  -d '{"fullName":"Figo Pratama","email":"mymail.figo@gmail.com","password":"password123"}'
```

Get all users:
```bash
curl http://localhost:3000/api/users
```

Get by ID:
```bash
curl http://localhost:3000/api/users/<id>
```

Delete by ID:
```bash
curl -X DELETE http://localhost:3000/api/users/<id>
```
