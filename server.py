import cv2
import base64
import asyncio
from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse
from proctor import check

app = FastAPI()

@app.get("/")
async def index():
    return FileResponse("templates/index.html")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    cap = cv2.VideoCapture(0)

    try:
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                break

            processed_frame, status = check(frame)
            _, buffer = cv2.imencode(".jpg", processed_frame)
            frame_b64 = base64.b64encode(buffer).decode("utf-8")

            await websocket.send_text(frame_b64)
            await asyncio.sleep(0.05)  

    except Exception as e:
        print(f"WebSockets closed with error {e}")

    finally:
        cap.release()
        try:
            await websocket.close()
        except Exception:
            pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)