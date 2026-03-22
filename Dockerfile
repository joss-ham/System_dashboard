# 1. Start with a tiny version of Python
FROM python:3.11-slim


WORKDIR /app


COPY requirements.txt .

# 4. Install the libraries
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your code (app.py, templates/, etc.)
COPY . .

# 6. Tell the container which port to open
EXPOSE 5000

# 7. The command to run when the container starts
CMD ["python", "app.py"]