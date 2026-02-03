# 🚀 Playto Community Feed

A high-performance Reddit-style community feed with threaded comments, dynamic karma leaderboard, and concurrency-safe like system.

## 🧠 Tech Stack
- Backend: Django + Django REST Framework
- Frontend: React
- Database: PostgreSQL
- Containerization: Docker

---

## ⚙️ Features

✔ Threaded nested comments (no N+1 queries)  
✔ Concurrency-safe Like system  
✔ Dynamic leaderboard (last 24h karma)  
✔ Transaction-based karma calculation  

---

## ▶ Run Locally (Docker)

```bash
docker-compose up --build
