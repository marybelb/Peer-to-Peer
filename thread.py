import threading
import time

class HeartbeatThread(threading.Thread):
    def __init__(self, ip, port):
        super().__init__()
        self.ip = ip
        self.port = port
        self.active = True

    def run(self):
        while self.active:
            print(f"Sending heartbeat to {self.ip}:{self.port}")
            time.sleep(10)  # Sleep for 10 seconds between heartbeats

if __name__ == "__main__":
    thread = HeartbeatThread('localhost', 5000)
    thread.start()
    thread.join()  # Wait here for the thread to end
