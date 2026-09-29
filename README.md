# Intelligent Exam Seating Arrangement Generator

## Overview

The Intelligent Exam Seating Arrangement Generator is a Python-based application designed to automate the process of allocating seats to students during examinations. The system reduces manual effort, improves seating organization, and helps maintain fairness by distributing students systematically across the available classroom seats.

The project demonstrates the use of Object-Oriented Programming, algorithm design, data validation, and modular software development concepts.

## Problem Statement

Manual exam seating arrangement is a time-consuming process and can lead to inefficient classroom utilization and improper student distribution. Educational institutions require a simpler and more reliable method to generate seating arrangements automatically.

## Objectives

- Automate the seating arrangement process.
- Reduce administrative workload.
- Improve classroom seat utilization.
- Generate transparent and fair seating plans.

## Features :-

### Student Management
- Register student details.
- Validate student information.
- Organize students for seat allocation.

### Seating Allocation Engine
- Automatically assign seats.
- Generate seating matrix.
- Prevent seat duplication.
- Efficiently utilize available classroom space.

### Analytics and Reporting
- Display seating arrangement.
- Generate occupancy statistics.
- Show classroom utilization percentage.
- Produce final allocation reports.

---
## Technologies Used

- Python 3.x
- Object-Oriented Programming (OOP)
- Data Structures
- Modular Programming

---

## Project Structure

│
├── main.py
├── student.py
├── classroom.py
├── allocator.py
├── validator.py
├── display.py
├── report.py
│
├── README.md
└── statement.md
```

---

## Functional Requirements

1. Student Registration Module
2. Seating Allocation Module
3. Reporting and Analysis Module

---

## Non-Functional Requirements

- Performance
- Reliability
- Maintainability
- Usability
- Scalability
- Error Handling

---

## Installation

1. Clone the repository

```bash
git clone <repository-link>
```

2. Navigate to project folder

```bash
cd ExamSeatingGenerator
```

3. Run the application

```bash
python main.py
```


## Sample Execution

```text
Number of Students: 4

Register No: 22BCE101
Name: Rahul
Section: A

Register No: 22BCE102
Name: Aman
Section: B

Rows: 2
Columns: 2
```

Output:

```text
22BCE101    22BCE102
EMPTY       EMPTY
```

## System Architecture

User → Main Module → Student Module → Allocation Engine → Seating Matrix → Display Module → Report Module


## Future Enhancements

- Multiple classroom support
- Section-wise intelligent distribution
- GUI using Tkinter
- Export seating arrangements to PDF
- Invigilator assignment system
- Advanced optimization algorithms


## Author
Developed by Kavya Reg number:26BCE10602
