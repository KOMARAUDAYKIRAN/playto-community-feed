# 🚀 Playto Community Feed

A **high-performance Reddit-style community feed** built to demonstrate scalable backend design, optimized database queries, and concurrency-safe operations.

This project was developed as part of the **Playto Engineering Challenge** to showcase real-world backend engineering, API architecture, and frontend integration.

---

## 🧠 Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Django, Django REST Framework |
| **Frontend** | React.js |
| **Database** | PostgreSQL |
| **Containerization** | Docker & Docker Compose |
| **API Architecture** | RESTful APIs |
| **ORM Optimization** | select_related, prefetch_related |

---

## ✨ Features

### 🧵 Threaded Nested Comments
- Infinite-level nested comments
- Optimized queries (no N+1 issue)
- Recursive comment tree structure

### ❤️ Concurrency-Safe Like System
- Prevents race conditions during simultaneous likes
- Uses atomic database transactions
- Ensures accurate like counts under load

### 🏆 Dynamic Karma Leaderboard
- Ranks users based on:
  - Post likes
  - Comment likes
- Shows top contributors in last 24 hours
- Uses aggregation queries for performance

### 🔁 Transaction-Based Karma Calculation
- All karma updates wrapped in DB transactions
- Ensures data consistency
- No partial updates or corruption

---

## 🏗 System Architecture
React Frontend → Django REST API → PostgreSQL Database
↑
Business Logic Layer


- Frontend handles UI rendering and API consumption
- Backend manages authentication, posts, comments, likes, and leaderboard logic
- Database optimized for relational queries

---

## 🐳 Running Locally (Docker)

### 1️⃣ Build & Start Containers

```bash
docker-compose up --build



## 🐳 Running Locally (Docker)

```bash
docker-compose up --build
```

---

## 🌐 Access Services

| Service     | URL                     |
|-------------|--------------------------|
| Frontend    | http://localhost:3000    |
| Backend API | http://localhost:8000    |

---

## 🔌 API Endpoints

| Method | Endpoint                   | Description          |
|--------|----------------------------|----------------------|
| GET    | `/api/posts/`              | Fetch community feed |
| POST   | `/api/posts/{id}/like/`    | Like a post          |
| GET    | `/api/comments/{post_id}/` | Get nested comments  |
| POST   | `/api/comments/`           | Add comment          |
| GET    | `/api/leaderboard/`        | Top karma users      |

---

## ⚡ Performance Optimizations

- Eliminated N+1 query problem  
- Query optimization using `select_related` and `prefetch_related`  
- Indexed foreign keys  
- Atomic transactions for safe concurrent updates  

---

## 🧪 Assumptions

- Authentication simplified for demo purposes  
- Karma calculated only from likes  
- Focus prioritized on backend scalability  

---

## 📂 Project Structure

```
backend/
  ├── playto/
  ├── manage.py
frontend/
  ├── src/
docker-compose.yml
README.md
```

---

## 🎯 Engineering Concepts Demonstrated

- Scalable API design  
- Concurrency handling  
- Query optimization  
- Transaction management  
- Dockerized deployment  
- Frontend–backend integration  

---

## 👨‍💻 Author

**Komara Uday Kiran**  
Developer Intern Applicant – Playto
