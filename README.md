# Library Management System - Microservices Architecture

## Project Overview
This project is a **Library Management System** developed using a **microservices architecture**.
The system is divided into four independent services and one API Gateway.

## Identified Microservices
- **Book Service** - Manages book records and availability.
- **Member Service** - Manages library member details and roles.
- **Borrowing Service** - Handles book borrowing and return transactions.
- **Reservation Service** - Manages reservations for unavailable books.

## API Gateway
A **FastAPI-based API Gateway** is used to provide a **single entry point** for all services.


This reduces complexity and provides a cleaner integration point.


---

## Database Configuration
The following MySQL databases are used:
- `library_books_db`
- `library_members_db`
- `library_borrowings_db`
- `library_reservations_db`

---

## How to Run the Project

### Step 1 - Start MySQL
Make sure **MySQL Server** is running.

### Step 2 - Run Each Microservice
Open separate terminals for each service.

#### Book Service
```bash
cd book-service
venv\Scripts\activate
uvicorn app.main:app --reload --port 8001
```

#### Member Service
```bash
cd member-service
venv\Scripts\activate
uvicorn app.main:app --reload --port 8002
```

#### Borrowing Service
```bash
cd borrowing-service
venv\Scripts\activate
uvicorn app.main:app --reload --port 8003
```

#### Reservation Service
```bash
cd reservation-service
venv\Scripts\activate
uvicorn app.main:app --reload --port 8004
```

### Step 3 - Run API Gateway
```bash
cd api-gateway
venv\Scripts\activate
uvicorn main:app --reload --port 8000
```

---

## Swagger Documentation

### Direct Service Access
- Book Service -> `http://127.0.0.1:8001/books/docs`
- Member Service -> `http://127.0.0.1:8002/members/docs`
- Borrowing Service -> `http://127.0.0.1:8003/borrowings/docs`
- Reservation Service -> `http://127.0.0.1:8004/reservations/docs`

### API Gateway Access
- Unified Gateway Swagger -> `http://127.0.0.1:8000/docs`



---

## Testing
The system was tested through:
- **Direct service access**
- **Gateway-based access**
- **Successful CRUD operations**
- **Swagger-based API testing**

---

## Conclusion
This project successfully demonstrates a **microservices-based backend solution** for a Library Management System.
It shows how microservices can improve **modularity**, **maintainability**, and **scalability**, while the **API Gateway** simplifies client communication through a single entry point.
