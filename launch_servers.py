import os
import threading
import subprocess
import signal
import sys

shutdown_flag = threading.Event()

def start_django_server():
    django_command = "python Backend/JobBoard/manage.py runserver 0.0.0.0:8000"

    django_process = subprocess.Popen(django_command, shell=True)

    django_process.wait()
    if not shutdown_flag.is_set():
        print("\033[91mDjango server closed unexpectedly...")
    else:
        print("\033[92mDjango server closed...")


def start_svelte_server():
    os.chdir("Frontend/jobboard")
    svelte_command = "npm run dev"

    svelte_process = subprocess.Popen(svelte_command, shell=True)

    svelte_process.wait()
    if not shutdown_flag.is_set():
        print("\033[91mServer Svelte closed unexpectedly...")
    else:
        print("\033[92mServer Svelte closed...")

def handle_signal(signum, frame):
    global shutdown_flag
    print("\033[92mArrêt en cours...")
    shutdown_flag.set()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, handle_signal)

    django_thread = threading.Thread(target=start_django_server)
    svelte_thread = threading.Thread(target=start_svelte_server)

    django_thread.start()
    svelte_thread.start()

    try:
        django_thread.join()
        svelte_thread.join()
    except KeyboardInterrupt:
        pass
