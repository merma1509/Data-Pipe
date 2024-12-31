FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    openjdk-11-jre \
    libpq-dev \
    && pip install pyspark kafka-python tensorflow pandas boto3 scikit-learn

# Set environment variables
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Copy scripts
WORKDIR /app
COPY . /app

# Command to run
CMD ["python", "main.py"]
