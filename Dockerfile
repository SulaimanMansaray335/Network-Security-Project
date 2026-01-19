FROM python:3.10-slim-bullseye
WORKDIR /app
COPY . /app

# Install awscli via apt-get and clean apt lists to reduce image size
RUN apt-get update \
	&& apt-get install -y --no-install-recommends awscli \
	&& rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]