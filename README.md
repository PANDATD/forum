# Forum Project Requirements

## 🎯 Goal
A responsive, lightweight forum application where users can create categories, start discussion threads, and post replies.

---

## ✅ Core Features (Phase 1)
1. View Categories and Threads.
2. Add new Threads under Categories.
3. Add Posts (replies) inside Threads.
4. Store data in SQLite (with migration support).
5. Responsive UI using Bootstrap.

---

## 🚀 Extended Features (Phase 2+)
- User Registration & Authentication.
- User Profiles with avatar, bio.
- Likes/Reactions on posts.
- Markdown support in posts.
- Search functionality (threads & posts).
- Moderation tools (delete/edit posts).
- Private Messages.
- Notifications.

---

## 🗄 Database Design (Phase 1)

### Tables:
- **User**
  - id (PK, Auto Increment)
  - username (unique)
  - email
  - password (hashed)

- **Category**
  - id (PK, Auto Increment)
  - name (unique)

- **Thread**
  - id (PK, Auto Increment)
  - title
  - category_id (FK → Category.id)
  - posts (relationship)

- **Post**
  - id (PK, Auto Increment)
  - content
  - created_at
  - user_id (FK → User.id)
  - thread_id (FK → Thread.id)

---

## 🛠 Tech Stack
- **Backend:** Flask (Python)
- **Database:** SQLite (SQLAlchemy ORM)
- **Frontend:** HTML + Bootstrap
- **Forms:** Flask-WTF
- **Migrations:** Flask-Migrate
- **Version Control:** Git + GitHub

---

## 📅 Development Roadmap

### Day 1
- Setup project structure
- Initialize Flask app
- Base template with Bootstrap
- GitHub repo created

### Day 2
- Define models
- Database migration setup
- Seed default categories

### Day 3
- List threads on homepage

### Day 4
- Create new thread form

### Day 5
- Add posts to threads

### Day 6
- User authentication (register/login)

### Day 7+
- Profiles, likes, search, moderation
