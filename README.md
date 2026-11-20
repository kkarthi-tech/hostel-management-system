# Hostel Management System

A simple Python and SQLite application to register hostel students, allocate rooms, search student records, vacate rooms, and view room availability.

## Features
- Register students and allocate rooms
- View and search student records
- Vacate room by removing student
- View room capacity, occupancy and availability
- Summary of total students and available spaces
- Input validation

## Technologies
Python 3, SQLite, Git

## Prerequisites
Python 3.8+; no external packages required.

## Run
```bash
python main.py
```

## Test
```bash
python -m unittest -v
```

## Room setup
Five sample rooms are created automatically: 101-103 (2 spaces each), 104-105 (3 spaces each).

## Limitations and future work
CLI-only; basic student records; no authentication. Future improvements could include fees, guardian details, web interface and reporting.
