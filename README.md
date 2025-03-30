ecom-log-generator - A lightweight Docker image that generates random eCommerce-style logs for testing logging tools. Simulates operations like signups, orders, logins, and cart actions with realistic JSON-formatted output. Perfect for validating log collection, parsing, and monitoring setups in containerized environments.

**Note:** This is only for testing purposes. Do not use it for long periods to avoid unnecessary log storage costs.

The Docker image is available at: `quay.io/prateekjain/ecom-log-generator`. You can pull and run it directly without building locally, unless you want to modify the code.

## Overview
This repository contains a Dockerized application that generates random eCommerce-style logs, designed for testing and validating logging tools. It simulates common eCommerce operations such as user signups, order processing, logins, and cart actions, producing JSON-formatted logs with realistic data. The image is lightweight and intended for general-purpose use in testing log collection, parsing, and monitoring pipelines.

## Features
- Generates random logs for:
  - User signups
  - Order processing (success/failure with error messages)
  - Login attempts
  - Cart operations (add/remove/update)
- JSON-formatted output with timestamps, request IDs, and operation details
- Logs written to both stdout (for tools like CloudWatch) and a file (`/var/log/ecom_logs.log`)
- Configurable via environment variables
- Runs indefinitely, simulating continuous application activity

## Use Case
This Docker image is built for testing logging tools and setups. Whether you're validating a log aggregator, testing a monitoring dashboard, or debugging a log ingestion pipeline, this generator provides a steady stream of realistic eCommerce logs. It's particularly useful for:
- Verifying log collection and ingestion
- Testing log parsing rules in tools like ELK, Splunk, or Datadog
- Simulating application behavior for load testing logging infrastructure

## Prerequisites
- Docker installed locally
- A logging tool/system to test (e.g., CloudWatch, ELK, etc.)

## Getting Started

### Pull the Image from Quay.io
Run the container directly from the registry:
```bash
docker run -v /path/to/local/logs:/var/log quay.io/prateekjain/ecom-log-generator
```

### Building the Image (only if you want to modify it)
1. Clone this repository:
   ```bash
   git clone https://github.com/prateekjaindev/ecom-log-generator.git
   cd ecom-log-generator
   ```

2. Build the Docker image:
   ```bash
   docker build -t ecom-log-generator .
   ```

### Running Locally
Run the container to start generating logs:
```bash
docker run -v /path/to/local/logs:/var/log ecom-log-generator
```

Logs will be printed to stdout and written to /var/log/ecom_logs.log in the mounted volume.

Use Ctrl+C to stop the container.

### Sample Log Output
```json
{
  "timestamp": "2025-03-30T10:15:23.456789",
  "request_id": "550e8400-e29b-41d4-a716-446655440000",
  "user_id": "user_42",
  "service": "ecom-api",
  "operation": "order",
  "status": "success",
  "duration_ms": 845,
  "order_id": "123e4567-e89b-12d3-a456-426614174000",
  "items": [
    {
      "product": "Laptop",
      "quantity": 1,
      "price": 129.99
    }
  ],
  "total": 129.99
}
```

## Testing with a Logging Tool

### Local Testing
Pipe the output to your logging tool or monitor the log file:
```bash
docker run quay.io/prateekjain/ecom-log-generator | your-logging-tool --input stdin
```

### Remote Deployment
Tag and push the image to your own container registry (if needed):
```bash
docker tag quay.io/prateekjain/ecom-log-generator:latest [your-registry]/ecom-log-generator:latest
docker push [your-registry]/ecom-log-generator:latest
```
Deploy in any container orchestration environment with appropriate logging configuration to collect and process the logs.

## Configuration
You can customize the log output by setting environment variables:
- `LOG_FILE`: Path to the log file inside the container (default: `/var/log/ecom_logs.log`)

### Example with custom log file:
```bash
docker run -e LOG_FILE=/var/log/custom.log -v /path/to/local/logs:/var/log quay.io/prateekjain/ecom-log-generator
```

## Notes
- The generator runs indefinitely until stopped, making it suitable for long-running tests.
- Log frequency is randomized (0.1-2 seconds between events) to mimic real application behavior.
- Mount a volume to persist logs if needed for analysis.

## License
MIT License (LICENSE) - feel free to use and modify for your testing needs!