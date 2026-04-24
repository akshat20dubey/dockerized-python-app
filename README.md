# 🐳 Dockerized Python Application

A Python script containerized with Docker and auto-built via GitHub Actions.

---

## 📌 What This Project Does

- Checks if websites are UP or DOWN
- Runs inside a Docker container
- Builds automatically on every `git push` using GitHub Actions

---

## 🐳 Dockerfile (Simple Explanation)

| Line | What it does |
|------|-------------|
| `FROM python:3.10-slim` | Use Python as base |
| `WORKDIR /app` | Set working folder |
| `COPY app.py .` | Copy my script in |
| `RUN pip install requests` | Install libraries |
| `CMD ["python", "app.py"]` | Run script on start |

---

## 🚀 Run It Yourself

```bash
docker build -t dockerized-python-app .
docker run dockerized-python-app
```

---

## 📚 What I Learned

- Writing a Dockerfile from scratch
- Containerizing a Python application
- Integrating Docker with GitHub Actions CI/CD

---

## 👨‍💻 Author
**Akshat Dubey** | [LinkedIn](https://www.linkedin.com/in/akshatautomates/) | [GitHub](https://github.com/akshat20dubey)
