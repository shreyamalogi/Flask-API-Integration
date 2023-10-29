# Flask API Integration 🚀


### Table of Contents 📑

  - [Introduction 🚀](#introduction)
  - [Project Details: 💻🌐📅✍️](#project-details-%EF%B8%8F)
  - [Description](#description)
  - [Installation 🛠️](#installation-️)
  - [Usage 🚀](#usage-)
  - [API Endpoints 🌐](#api-endpoints-)
  - [Contributions 🌟](#contributions-)
  - [License 📜](#license-)

---

## Introduction

Welcome to the Flask API Integration project! This simple Flask application taught by **Shreya Malogi** demonstrates basic API integration using the Flask framework.

[![GitHub stars](https://img.shields.io/github/stars/shreyamalogi/flask-api-integration.svg?style=social)](https://github.com/shreyamalogi/flask-api-integration/stargazers)

### Project Details: 💻🌐📅✍️

- **Functionality:** Demonstrates basic API integration using Flask.
- **Tech Stack:** `Flask`, `Python`
- **Author:** [@shreyamalogi](https://github.com/shreyamalogi/)
- **Year of Project:** 2022

---

## Description

Flask API Integration is a beginner-friendly project showcasing API integration using the Flask framework. The application provides two endpoints: the home page and a user-specific page. Each endpoint returns a JSON response indicating the successful loading of the respective page.

## Installation 🛠️

1. Install Flask:

   ```bash
   pip install flask
   ```

2. Run the application:

   ```bash
   python <filename>.py
   ```

   Replace `<filename>` with the name of your Python file.

## Usage 🚀

- **Home Page:** Access the home page at `http://localhost:2000/` to receive a JSON response indicating the successful loading of the home page.

- **User Request:** Access the user page at `http://localhost:2000/user/?user=<username>` to receive a JSON response indicating the successful loading of a user-specific page. Replace `<username>` with the desired username.

## API Endpoints 🌐

1. **Home Page:**
   - Endpoint: `http://localhost:2000/`
   - Method: `GET`
   - Response Format: JSON
   - Sample Response:
     ```json
     {
       "page": "Home",
       "Message": "successfully loaded the home page",
       "Timestamp": <current_timestamp>
     }
     ```

2. **User Request:**
   - Endpoint: `http://localhost:2000/user/?user=<username>`
   - Method: `GET`
   - Parameters:
     - `user`: The username for which the request is made.
   - Response Format: JSON
   - Sample Response:
     ```json
     {
       "page": "request",
       "Message": "successfully loaded the request for <username> pages",
       "Timestamp": <current_timestamp>
     }
     ```

## Contributions 🌟

Contributions are welcome! If you find any issues or have suggestions, feel free to create a pull request or open an issue.

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

© 2022 Shreya Malogi

Happy Coding! 🚀👩‍💻
