# Python Debugger Exercise

## Introduction

Alex and Iury were trying to finish off a Python quotes server written in Flask for a client... but, as is always the case, deadlines were looming, and they may have accidentally left a few bugs in it. 

Your mission: **Find and fix the bugs before their client does!** 🕵️‍♂️🐛

---

## Setup

1. **Clone this repository**  
   ```sh
   git clone <repo-url>
   ```
   
2. **Navigate to the correct folder**  
   ```sh
   cd <repo-folder>
   ```
   When you run `ls` (or `dir` on Windows), you should see `server.py`.

3. **Install Flask**  
   ```sh
   pip3 install flask
   ```
   This installs Flask globally. If you’re using a virtual environment, activate it first.

4. **Open this folder in VS Code**  
   - Launch VS Code and open the project folder.
   - Open `server.py`.

5. **Run the Python server**  
   - Start the Flask server by running `server.py`.  
   - Ideally, **run it using the debugger** for the "Task" step.

6. **Test the GET `/get` route**  
   - Open your browser or use Postman/Insomnia.  
   - Visit: `http://localhost:5000/get`.  
   - You should see a JSON response with the list of quotes.

7. **Test the POST `/post` route**  
   - Use Postman/Insomnia to send a **POST request** to:  
     ```
     http://localhost:5000/post
     ```
   - With the following JSON payload:
     ```json
     {
       "quote": "Code is like humor. When you have to explain it, it’s bad. - Cory House"
     }
     ```
   - If the server works correctly, the new quote should be added.

---

## Task: Debugging the Flask App 🔍

0. **Pair up with a partner.**  
   - One person shares their screen.
   - Together, **review the code** and try to understand what each route does.

1. **Set breakpoints**  
   - Put breakpoints in **every route handler** except `GET /get` (since it has no bugs).
   - In VS Code, click on the left margin to set breakpoints.

2. **Step through the code using the debugger**  
   - Trigger each route (e.g., visit `/average_length` in the browser).
   - Use **"Step Over"** in the debugger to track values and find where things go wrong.

---

## Hints 🧐

- Some functions return incorrect values even though they don't crash.  
- One function may have an **off-by-one error** in a loop.  
- Another function may use **incorrect arithmetic inside a loop**.  
- A **random selection bug** may cause a crash sometimes.  

---

Happy debugging! 🔧🐞 Let us know if you solve all the bugs! 😃
