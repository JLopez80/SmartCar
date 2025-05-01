import socket
import json
import time
import whisper
import speech_recognition as sr

# ESP32 settings
esp32_ip = "192.168.4.1"
port = 100

# Load the Whisper model
model = whisper.load_model("base")

def send_command(direction, speed, duration=2):
    command = {"N": 102, "D1": direction, "D2": speed}
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((esp32_ip, port))
            json_command = json.dumps(command) + "\n"
            s.sendall(json_command.encode('utf-8'))
            print(f"Sent: {json_command} for {duration} seconds")
            time.sleep(duration)
            stop_command = {"N": 102, "D1": 9, "D2": 0}
            stop_json = json.dumps(stop_command) + "\n"
            s.sendall(stop_json.encode('utf-8'))
            print(f"Sent stop command: {stop_json}")
    except ConnectionRefusedError:
        print(f"Connection refused. Is the ESP32 listening on {esp32_ip}:{port}?")
    except socket.error as e:
        print(f"Socket error: {e}")

def listen_and_transcribe():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say a command...")
        audio = recognizer.listen(source)
        print("Processing...")

        # Save audio to file
        with open("command.wav", "wb") as f:
            f.write(audio.get_wav_data())

        # Transcribe using Whisper
        result = model.transcribe("command.wav")
        return result["text"].lower().strip()

def main():
    while True:
        command_text = listen_and_transcribe()
        print(f"You said: {command_text}")

        if "forward" in command_text:
            send_command(1, 100)
        elif "backward" in command_text:
            send_command(2, 100)
        elif "left" in command_text:
            send_command(3, 100)
        elif "right" in command_text:
            send_command(4, 100)
        elif "stop" in command_text:
            send_command(9, 0)
        else:
            print("Command not recognized.")

if __name__ == "__main__":
    main()
