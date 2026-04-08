## IS601 Module 9 – Working with Raw SQL in pgAdmin ##

A FastAPI-based calculator application extended with PostgreSQL and pgAdmin using Docker Compose to perform raw SQL operations and demonstrate database relationships.


# 🚀 Project Overview
This project builds on a FastAPI calculator application and integrates:
PostgreSQL database
pgAdmin for database management
Docker Compose for multi-container setup
The focus of this module is working with raw SQL queries to perform full CRUD operations and understand database relationships.


# 🛠️ Tech Stack
Backend: FastAPI, Python
Database: PostgreSQL
Database Tool: pgAdmin
Containerization: Docker, Docker Compose
Testing: Pytest, Playwright


# 🐳 Docker Setup
Run the full application using Docker Compose:
docker compose up --build
Access Services:
FastAPI App → http://localhost:8000
pgAdmin → http://localhost:5050


# 🗄️ Database Configuration
Connect pgAdmin using:
Host: db
Port: 5432
Database: fastapi_db
Username: postgres
Password: postgres

# 🧾 SQL Operations Performed

1. Create Tables
Created users table with primary key and unique constraints
Created calculations table with foreign key reference to users

2. Insert Data
Inserted multiple user records
Inserted calculation records linked using user_id

3. Query Data
Retrieved all users
Retrieved all calculations
Performed JOIN query to combine user and calculation data

4. Update Data
Updated a calculation record using SQL

5. Delete Data
Deleted a calculation record from the database

# 🔗 Database Relationship
This project demonstrates a one-to-many relationship:
One user → multiple calculations
Implemented using a foreign key (user_id)


# 📁 Key Files
docker-compose.yml – Multi-container setup for FastAPI, PostgreSQL, and pgAdmin
main.py – FastAPI application
requirements.txt – Project dependencies
tests/ – Unit, integration, and E2E tests


# 📝 Submission
Docker Compose environment successfully configured
PostgreSQL and pgAdmin running without errors
All SQL operations executed using pgAdmin
Reflection and documentation completed


# 👤 Author
Krupa Adulobo
GitHub: https://github.com/kdulobo12
Docker Hub: https://hub.docker.com/r/kdulobo12/is601_module8


# 📄 License 

This project is licensed under the MIT License. See the LICENSE file for details.
