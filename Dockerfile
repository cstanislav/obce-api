FROM python:latest

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the code
COPY . .

# Run uvicorn
CMD ["uvicorn", "obec-api.main:app", "--host", "0.0.0.0"]