# Dockerized Multi-Service Web App with Logging and Database Dashboard

Project Structure
      project/
      │── docker-compose.yml
      │── init.sql
      │── nginx/
      │   └── default.conf
      │── app/
      │   ├── Dockerfile
      │   ├── requirements.txt
      │   └── app.py


# 🚀 Running the Setup
Step 1: Start services
docker-compose up -d --build

Step 2: Verify containers
docker ps
{ You should see: mysql-db, flask-app, nginx-proxy, adminer-ui. }

Step 3: Test Flask app
curl -A "MyClientTest" http://localhost:8080

Output:
✅ Logged access from 172.20.0.1 with UA: MyClientTest

Step 4: Access Adminer (DB dashboard)
Open → http://localhost:8081
System: MySQL
Server: db
Username: user
Password: userpass
Database: mydb

👉 You’ll see the access_logs table with all logged requests.


✅ Final Setup
Nginx (port 8080) → reverse proxy to Flask.
Flask inserts access logs into MySQL.
MySQL stores logs in access_logs.
Adminer (port 8081) provides a GUI to query and manage DB.

