# Smart Proctor

This is a real-time AI-powered proctoring solution that analyzes a user's face orientation to detect any suspicious activity during an exam or assessment. It uses **FastAPI** for the backend, **WebSockets** for real-time communication, and **OpenCV + Mediapipe** for face tracking and analysis.

## Features
- **Live Face Orientation Analysis**  using OpenCV & Mediapipe to detect suspicious activity
- **Real-time Streaming** via WebSockets

## Setup
Clone the repository:

```sh
> https://github.com/Armaan457/Smart-Proctor.git
```
Create and activate a virtual environment:

```sh
> python -m venv env
> env\Scripts\activate
  ```
Install dependencies:

```sh
> pip install -r requirements.txt
```

Run the server:

```sh
> python server.py
```


