FROM continuumio/anaconda3:latest

# Copy app source code
COPY . /app
WORKDIR /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Entrypoint
CMD ["python", "flask_api_copy.py"]