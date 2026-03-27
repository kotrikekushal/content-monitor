# Content Monitoring & Flagging System

A Django REST Framework-based backend system that scans content against keywords, assigns relevance scores, and supports a review workflow with suppression logic.

---

## Tech Stack

* Python
* Django
* Django REST Framework
* SQLite

---

## Project Structure

```
content_monitor/
├── manage.py
├── db.sqlite3
└── monitor/
    ├── models.py        # Data models
    ├── serializers.py   # API serializers
    ├── views.py         # API endpoints
    ├── services.py      # Business logic (scan & matching)
    ├── admin.py         # Admin configuration
    ├── urls.py          # Routes
```

---

## Setup Instructions

```bash
git clone https://github.com/kotrikekushal/content-monitor.git
cd content_monitor

pip install -r requirements.txt
```

---

## How to Run the Application

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## Access the Application

* Home: http://127.0.0.1:8000/
* Admin: http://127.0.0.1:8000/admin/

---

## API Endpoints

* POST /keywords/
* POST /scan/
* GET /flags/
* PATCH `/flags/<id>/`

---

## Data Models

* **Keyword** → stores keywords to monitor
* **ContentItem** → title, body, source, last_updated
* **Flag** → keyword, content_item, score, status

---

## Matching Logic

* Exact keyword match in title → **100**
* Partial keyword match in title → **70**
* Keyword appears only in body → **40**

---

## Suppression Logic

If a flag is marked as **irrelevant**, it is not shown again unless the content is updated.

* If `content.last_updated <= flag.last_reviewed_at` → skip
* If content is updated → flag becomes `pending` again

---

## Content Source

Mock data is used (manually added via Django admin).

---

## Sample API Requests

### Create Keyword

```json
POST /keywords/
{
  "name": "python"
}
```

### Trigger Scan

```bash
POST /scan/
```

### Get Flags

```bash
GET /flags/
```

### Update Flag

```json
PATCH /flags/20/
{
  "status": "irrelevant"
}
```

---

## Assumptions

* Case-insensitive keyword matching
* Deterministic scoring logic
* No frontend (admin + API based interaction)
* SQLite used for simplicity

---
