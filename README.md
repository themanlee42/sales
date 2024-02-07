# Sales

## Installation Guide

### Configuration

1. **Modify `.env` File:**

   - Enter your OpenAI key:
     ```
     DEV_OPENAI_API_KEY=your_openai_key_here
     ```
   - For production, enter the domain or IP:
     ```
     REACT_APP_PROD_API_URL=your_production_domain_or_ip_here
     ```

2. **Database Volume Path:**
   - For Windows, set your MongoDB volume path like this:
     ```
     DEV_MONGODB_VOLUME_PATH=c:/volumes/var/lib/mongodb
     ```
   - For Mac/Linux, use:
     ```
     DEV_MONGODB_VOLUME_PATH=mongodb_data
     ```

### Example `.env` Configuration

```plaintext
##################################################################################
# For Development
##################################################################################
# BACKEND
DEV_FLASK_ENV=DevelopmentConfig
DEV_OPENAI_API_KEY=[YOUR OPENAI API KEY]
DEV_NGINX_CONF=./nginx.dev.conf
DEV_MONGO_URL=mongodb://jason:1234@mongodb:27017/sales?authSource=admin

# FRONTEND
REACT_APP_DEV_API_URL=http://localhost/api

# MONGODB
DEV_MONGO_INITDB_ROOT_USERNAME=jason
DEV_MONGO_INITDB_ROOT_PASSWORD=1234
DEV_MONGODB_VOLUME_PATH=c:/volumes/var/lib/mongodb  # For non-Windows, use: mongodb_data

##################################################################################
# For Production
##################################################################################
# BACKEND
PROD_FLASK_ENV=ProductionConfig
PROD_OPENAI_API_KEY=[YOUR OPENAI API KEY]
PROD_NGINX_CONF=./nginx.prod.conf
PROD_MONGO_URL=mongodb://jason:12341234@mongodb:27017/sales?authSource=admin

# FRONTEND
REACT_APP_PROD_API_URL=http://123.123.123.123

# MONGODB
PROD_MONGO_INITDB_ROOT_USERNAME=jason
PROD_MONGO_INITDB_ROOT_PASSWORD=12341234
```

### Installation

1. **Get Docker:**

   - Download from [Docker's official site](https://www.docker.com/).

2. **For Local Development:**

   - In the root directory, build using:
     ```
     docker-compose -f docker-compose.dev.yml build
     ```
   - And run:
     ```
     docker-compose -f docker-compose.dev.yml up
     ```
   - Use your browser and go to `http://localhost` to enjoy the application.

3. **For Production:**
   - **Important:** Open `nginx.prod.conf` and set SSL. Replace the following line with your domain:
     ```
     server_name [YOUR_SERVER_DOMAIN];
     ```
   - Build using:
     ```
     docker-compose -f docker-compose.prod.yml build
     ```
   - And run:
     ```
     docker-compose -f docker-compose.prod.yml up
     ```
   - Use your browser and go to `http://[YOUR_DOMAIN.COM]` to enjoy the application.
