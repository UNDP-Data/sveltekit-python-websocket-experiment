import websocket
import time
import threading
import json

def on_message(ws, message):
    print(f"Received: {message}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("Closed")

def on_open(ws):
    def run(*args):
        while True:
            for i in range(100):
                message = {
                    "user": "a85516c81c0b78d3e89d3f00099b8b15",
                    "url": "https://undpgeohub.blob.core.windows.net/userdata/a85516c81c0b78d3e89d3f00099b8b15/raw/wasac-rwasom-2-data-revised_20230912143433.gpkg",
                    "progress": i + 1,
                    "stage": 'Ingesting'
                }
                ws.send(json.dumps(message))
                time.sleep(1)

    run_thread = threading.Thread(target=run)
    run_thread.start()

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:5173/websocket",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
