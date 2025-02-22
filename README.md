# Shipping Ships API Server

A lightweight HTTP server implementing a RESTful API for managing shipping ship orders, styles, sizes, and metals. Built using Python's `http.server` module with custom JSON handling capabilities.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Running the Server](#running-the-server)
- [API Endpoints](#api-endpoints)
- [Usage Examples](#usage-examples)
- [Notes](#notes)

## Features

- Full CRUD operations for orders
- Resource management for styles, sizes, and metals
- JSON-based data exchange
- Query parameter support
- HTTP status code compliance
- Clean URL routing

## Installation

```bash
git clone [repository-url]
pipenv shell
pipenv install
```

## Running the Server

```bash
python server.py
```

The server will start on port 8000 and display the ASCII banner.

## API Endpoints

### Orders

- **GET /orders**: Retrieve all orders
  - Response: JSON array of order objects
  - Status: 200 OK

- **GET /orders?pk={id}**: Get specific order by primary key
  - Response: Single order object
  - Status: 200 OK

- **POST /orders**: Create new order
  - Request Body: Order data in JSON format
  - Response: Success message
  - Status: 201 Created

- **DELETE /orders?pk={id}**: Delete order by primary key
  - Response: Success message
  - Status: 200 OK

### Metals

- **GET /metals**: List all metals
  - Response: Array of metal objects
  - Status: 200 OK

- **GET /metals?pk={id}**: Get specific metal
  - Response: Single metal object
  - Status: 200 OK

### Styles

- **GET /styles**: List all styles
  - Response: Array of style objects
  - Status: 200 OK

- **GET /styles?pk={id}**: Get specific style
  - Response: Single style object
  - Status: 200 OK

### Sizes

- **GET /sizes**: List all sizes
  - Response: Array of size objects
  - Status: 200 OK

- **GET /sizes?pk={id}**: Get specific size
  - Response: Single size object
  - Status: 200 OK

## Usage Examples

```bash
# Get all orders
curl http://localhost:8000/orders

# Create new order
curl -X POST \
  http://localhost:8000/orders \
  -H "Content-Type: application/json" \
  -d '{"order_data": "your_order_details"}'

# Get specific order
curl http://localhost:8000/orders?pk=123

# Delete order
curl -X DELETE http://localhost:8000/orders?pk=123
```

## Notes

- All endpoints return JSON responses
- Error handling follows HTTP status codes
- Query parameters are used for filtering and specifying resources
- The server uses custom status codes for specific error conditions
- PUT endpoint for metals is partially implemented
