# Smart Unit Converter Microservice

A lightweight REST-based microservice that provides reusable unit conversion functionality for student projects. The service accepts a numeric value and source/target units and returns the converted result in JSON format.

## 1. Service Information

**Service Name:** Smart Unit Converter Microservice

**Description:**  
A reusable Flask-based REST API for converting distance, temperature, and weight units.

## 2. Technology Stack

- Python 3
- Flask
- REST API
- JSON
- Postman
- Microsoft Edge Developer Tools

## 3. Features

- Distance conversion
- Temperature conversion
- Weight conversion
- RESTful GET endpoint
- JSON responses
- Input validation
- Error handling
- No database dependency
- Lightweight and reusable

## 4. Supported Conversions

| From | To |
|---|---|
| km | miles |
| miles | km |
| m | ft |
| ft | m |
| celsius | fahrenheit |
| fahrenheit | celsius |
| kg | pounds |
| pounds | kg |

## 5. API Endpoint

### GET /api/convert

**URL:**

```text
http://localhost:5000/api/convert