# HNGx CRUD Person REST API
This HNGx CRUD Person REST API. This API allows you to manage
and interact with a "Person" resource, performing CRUD (Create, Read, Update, Delete)
operations on individuals' data.
## Table of Contents
- [API Endpoints](#api-endpoints)
- [Create a Person](#create-a-person)
- [Retrieve a Person](#retrieve-a-person)
- [Update a Person](#update-a-person)
- [Delete a Person](#delete-a-person)
- [Request/Response Formats](#requestresponse-formats)
- [Sample Usage](#sample-usage)
- [Limitations](#limitations)
- [Setup Instructions](#setup-instructions)
## API Endpoints
### Create a Person
- **Endpoint:** `POST /api`
- **Description:** Create a new person.
- **Request Format:**
- Content-Type: `application/json`
- Body:
```json
{
"name": "John Doe",
"email": "john@example.com"
}
```
- **Response Format:**
- Status Code: 201 (Created)
- Body:
```json
{
"id": 1,
"name": "John Doe",
"email": "john@example.com"
}
```
### Retrieve a Person
- **Endpoint:** `GET /api/<user_id>`
- **Description:** Retrieve details of a person by their ID.
- **Request Format:** None required.
- **Response Format:**
- Status Code: 200 (OK)
- Body:
```json
{
"id": 1,
"name": "John Doe",
"email": "john@example.com"
}
```
### Update a Person
- **Endpoint:** `PUT /api/<user_id>`
- **Description:** Update details of an existing person.
- **Request Format:**
- Content-Type: `application/json`
- Body:
```json
{
"name": "Updated John Doe",
"email": "updated_john@example.com"
}
```
- **Response Format:**
- Status Code: 200 (OK)
- Body:
```json
{
"id": 1,
"name": "Updated John Doe",
"email": "updated_john@example.com"
}
```
### Delete a Person
- **Endpoint:** `DELETE /api/<user_id>`
- **Description:** Remove a person.
- **Request Format:** None required.
- **Response Format:** No content (204 No Content)
## Request/Response Formats
- **Request Format:**
- Content-Type: `application/json`
- All API endpoints accept and return data in JSON format.
- **Response Format:**
- Successful responses return data in JSON format.
- Errors are returned with appropriate HTTP status codes and error messages in JSON format.
## Sample Usage
Here are some example API requests:
- Create a new person:
```http
POST https://hngx-backend-track-task2.onrender.com/api
Content-Type: application/json
{
"name": "John Doe",
"email": "john@example.com"
}
```
- Retrieve details of a person:
```http
GET https://hngx-backend-track-task2.onrender.com/api/2
```
- Update details of a person:
```http
PUT https://hngx-backend-track-task2.onrender.com/api/2
Content-Type: application/json
{
"name": "Updated John Doe",
"email": "updated_john@example.com"
}
```
- Remove a person:
```http
DELETE https://hngx-backend-track-task2.onrender.com/api/2
```
## Limitations
- This API is a simple example and may not cover all possible use cases.
- Error handling is limited to basic validation checks.
## Setup Instructions
For detailed instructions on how to set up, run, and use this API, please refer to the
[README](README.md) file.