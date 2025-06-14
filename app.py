import os
import webbrowser
import threading
import time

def open_browser():
    time.sleep(2)
    webbrowser.open_new("http://localhost:8501")

if __name__ == "__main__":
    threading.Thread(target=open_browser).start()
    os.system("streamlit run main.py")
