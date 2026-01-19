FROM python:3.10-slim-bullseye
WORKDIR /app
COPY . /app

# Install awscli with apt-get and clean up apt lists to reduce image size
RUN apt-get update \
	&& apt-get install -y --no-install-recommends awscli \
	&& rm -rf /var/lib/apt/lists/*

# Install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]