# Automated Log Analyzer & Error Detection System

## Overview
The **Automated Log Analyzer** is a lightweight web application that helps analyze server log files and categorize log entries into **Errors, Warnings, and Informational messages**.

This tool is useful for **system monitoring, debugging, and troubleshooting**, which are important tasks in **Site Reliability Engineering (SRE)** and **IT Operations** roles.

The application allows users to upload a log file and automatically processes it to identify critical issues in the system logs.

---

## Key Features

- Upload and analyze server log files
- Automatic detection of **ERROR**, **WARNING**, and **INFO** log messages
- Simple and clean **web-based dashboard**
- Organized display of log results for easy debugging
- Lightweight and fast log parsing
- Beginner-friendly monitoring tool for infrastructure logs

---

## Technologies Used

### Programming Language
- Python

### Backend Framework
- Flask

### Frontend
- HTML5  
- CSS3

### Tools
- Git  
- GitHub  
- VS Code

---

## Project Structure

```
log-analyzer
│
├── main.py
├── requirements.txt
├── Procfile
├── runtime.txt
│
├── templates
│   └── index.html
│
├── static
│   └── style.css
│
└── uploads
```

---

## File Description

### main.py
Contains the Flask application and the log analysis logic.

### requirements.txt
Lists Python dependencies required to run the application.

### templates/index.html
Frontend page for uploading log files and displaying results.

### static/style.css
Contains styling for the user interface.

### uploads/
Stores uploaded log files temporarily for analysis.

---

## How the System Works

1. The user uploads a **log file** through the web interface.
2. The backend Flask application reads the log file.
3. The system scans each line of the file.
4. Log entries are categorized based on keywords:
   - ERROR
   - WARNING
   - INFO
5. The categorized logs are displayed on the web dashboard.

---

## Log Analysis Logic

The analyzer checks each line of the uploaded log file and classifies entries using simple keyword detection.

| Log Keyword | Category |
|-------------|----------|
| ERROR | Critical system error |
| WARNING | Potential issue |
| INFO | General system information |

This helps quickly identify problems in system logs.

---

## Example Log File

Example of a log file that can be analyzed:

```
INFO Server started
INFO User logged in
WARNING Memory usage high
ERROR Database connection failed
INFO Request processed
ERROR Timeout error
```

After analysis, the system will separate the logs into different categories.

---

## How to Run the Project Locally

### 1. Clone the Repository

```
git clone https://github.com/yourusername/automated-log-analyzer.git
```

### 2. Navigate to the Project Folder

```
cd automated-log-analyzer
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Run the Application

```
python main.py
```

### 5. Open the Web Application

Open the browser and go to:

```
http://localhost:10000
```

Upload a log file to start analyzing logs.

---

## Use Cases

This tool can be used for:

- Server log analysis
- Application debugging
- System monitoring
- Learning basic log analysis techniques
- Understanding SRE monitoring concepts

---

## Future Improvements

Possible enhancements for the project include:

- Real-time log monitoring
- Log search functionality
- Error statistics dashboard
- Graph visualization of log data
- Support for large log files
- Alert notification system

---

## Author

**Saurabh Kishan Butale**

Computer Engineering Student  
Interested in Software Development, Monitoring Systems, and Cloud Applications.

---

## License

This project is for educational and demonstration purposes.

© All Rights Reserved  
Copyright Saurabh Kishan Butale 2026
