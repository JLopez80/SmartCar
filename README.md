# SmartCar
This project enables Elegoo's Smart Robot Car V4.0 to move based on voice commands, using OpenAI's Whisper model for speech-to-text transcription. The V4.0 kit includes an onboard ESP32 module, which creates a Wi-Fi access point—allowing wireless communication with the car without needing a USB connection.

The project responds to simple voice commands such as: *move forward*, *turn left*, *turn right*, *move backward*, and *stop*. Feel free to customize or expand the list of commands as needed.

## Hardware Requirements  
The following hardware components from the **Elegoo Smart Robot Car V4.0** kit are used in this project:

- **Car Components:**
  - **ESP32-CAM Module** (ESP32-WROVER or ESP32-S3-WROOM-1)  
    - Includes a built-in camera, but in this project it's used solely for Wi-Fi communication.
  - **Motor Driver Module**  
    - Controls the movement of the car by driving the motors based on received commands.
  - **DC Motors with Wheels**  
    - Provide forward, backward, and turning motion.
  - **Chassis Frame**  
    - Structural base for all mounted components.
  - **Rechargeable Battery Pack**  
    - Powers the car and all onboard electronics.
  - **Jumper Wires**  
    - Used for connecting the ESP32 to the motor driver.

- **External Components (not part of the car):**
  - **Computer with Microphone Input**  
    - Runs the Python program and captures voice commands.
  - **Microphone** (USB or built-in)  
    - Used to record voice commands for transcription via Whisper.



## Python Libraries  
- **Python 3.x** (for running the speech recognition and controlling the Arduino)
  - Install Python from: [python.org](https://www.python.org/downloads/)
    
  - **Whisper** (for speech-to-text transcription)
    ```bash
       pip install openai-whisper
  - **SpeechRecognition** (for capturing audio)
    ```bash
       pip install SpeechRecognition
  - **Socket** (for communication with the ESP32)
    - Does not need to be installed since it is a built-in Python library.
  - **JSON** (for sending commands in JSON format)
    - Does not need to be installed since it is a built-in Python library.
  - **Time** (for time-related functions, such as delays)
    - Does not need to be installed since it is a built-in Python library.

## Getting Started

1. **Build the car according to Elegoo's V4.0 kit manual.**  
   - **NOTE:** Make sure the following motor connections are correct:
     - Upper left motor → **M1** on the motor shield  
     - Upper right motor → **M2** on the motor shield  
     - Rear left motor → **M4** on the motor shield  
     - Rear right motor → **M3** on the motor shield  

   > ⚠️ These details are mentioned in the manual but can be easily overlooked. If any motors are connected incorrectly, the car may move in the wrong direction when executing commands.

2. **Turn on the car and connect to the ESP32 access point.**
  - If the access point doesn't appear, ensure the car is powered on. Without power, the ESP32 won’t be able to broadcast the access point.

3. **After assembling the car and connecting to the ESP32 access point, run this [Python script](SmartCar.py).**
   - The car’s default IP address is `192.168.4.1`  
   - Communication with the car is handled over **port 100**
4. **Test the commands.**
   -  


    
## Credits / Acknowledgements
- **Whisper** by OpenAI for the speech-to-text model.
- **SpeechRecognition** by Anthony Zhang for handling audio recording and recognition.
- **ESP32** by Espressif for providing Wi-Fi and Bluetooth capabilities for wireless communication.
- **Elegoo Smart Robot Car V4** for the base hardware and integration with the ESP32 board.

## Demonstration video  
This [video](https://youtu.be/0AbyosnZ-v8) demonstrates how the project works. 


     
