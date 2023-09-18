# Use image with both python and node installed
FROM nikolaik/python-nodejs:python3.11-nodejs18-alpine

WORKDIR /app/backend

# Install required libraries and Python dependencies
COPY ./backend/requirements.txt /app/backend
RUN  \
    apk update && \
    apk upgrade && \
    apk add --no-cache bash postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    pip3 install --upgrade pip -r requirements.txt && \
    apk --purge del .build-deps

# Add the rest of the code
COPY ./backend/ /app/backend

# Copy scripts to main directory
COPY ./backend/scripts/ /app/

# Install frontend dependencies
WORKDIR /app/frontend

COPY ./frontend/package.json ./frontend/package-lock.json /app/frontend/
RUN npm install

# Add the rest of the code
COPY ./frontend /app/frontend

# Build react static files
RUN npm run build

# Collect static files
RUN mkdir /app/staticfiles

WORKDIR /app

# Make port 8000 available for the app
ENV PORT 8000
EXPOSE 8000

# Be sure to use 0.0.0.0 for the host within the Docker container,
# otherwise the browser won't be able to find it
RUN ["chmod", "+x", "/app/entrypoint-hybrid.sh"]
ENTRYPOINT [ "/app/entrypoint-hybrid.sh" ]
