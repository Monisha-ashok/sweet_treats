# Sweet Treats Management System

## Overview
This application is designed for a confectionery business to manage specialty treats, stock inventory, and customer requests. It uses SQLite for database management and Flask for the web framework.

## Features
- Manage specialty treats and their availability
- Track stock inventory
- Record customer requests and dietary restrictions

## Prerequisites
- Python 3.12 or higher
- pip
- Docker (for containerization)

## Project Structure
```plaintext
sweet_treats/
├── app.py                  # The main application file with Flask app definition
├── database.py             # Database management using SQLite
├── requirements.txt        # List of project dependencies
├── Dockerfile              # Instructions for building a Docker image
├── templates/              # Folder containing HTML templates
│   └── index.html          # Main webpage template
└── README.md               # Project documentation

## Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Monisha-ashok/sweet_treats.git
   cd sweet_treats
   ```
2. Install Required Packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Application:
   ```bash
   python app.py
   ```
The application will start at http://127.0.0.1:5000

## API Endpoints

### Treats
- GET `/treats`: List all treats
- POST `/treats`: Add a new treat
- DELETE `/treats/<id>`: Remove a treat

### Stock
- GET `/stock`: List all stock items
- POST `/stock`: Add a new stock item
- PUT `/stock/<id>`: Update stock amount
- DELETE `/stock/<id>`: Remove stock item

### Customer Requests
- GET `/requests`: List all customer requests
- POST `/requests`: Log a new request

## Testing the Application
1. Adding a Treat
   ```bash
   curl -X POST http://127.0.0.1:5000/treats -H "Content-Type: application/json" -d '{"treat_name": "Chocolate Truffle", "availability": "All Year"}'
   ```
2. Getting All Treats
   ```bash
   curl http://127.0.0.1:5000/treats
   ```
3. Deleting a Treat
   ```bash
   curl -X DELETE http://127.0.0.1:5000/treats/1
   ```
4. Adding a Stock Item
   ```bash
   curl -X POST http://127.0.0.1:5000/stock -H "Content-Type: application/json" -d '{"item_name": "Cocoa Powder", "amount": 100}'
   ```
5. Getting all Stock Items
   ```bash
   curl http://127.0.0.1:5000/stock
   ```
6. Adding a Customer Request
   ```bash
   curl -X POST http://127.0.0.1:5000/requests -H "Content-Type: application/json" -d '{"treat_name": "Vanilla", "requester": "Ashok", "dietary_restrictions": "No-peanuts"}'
   ```
7. Getting all Requests
   ```bash
   curl http://127.0.0.1:5000/requests
   ```

## Docker Setup
1. Build the Docker Image:
   ```bash
   docker build -t sweet_treats .
   ```
2. Run the Docker Container:
   ```bash
   docker run -p 5000:5000 sweet_treats
   ```

The application will be accessible at http://127.0.0.1:5000

## Web Interface
The application provides a simple web interface accessible through a web browser:

- Navigate to http://127.0.0.1:5000 in your web browser
- The main page displays lists of treats, stock items, and customer requests
- Use the provided forms to add new treats, stock items, or customer requests
- The page automatically refreshes to show updated data after submissions