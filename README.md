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

## Credits / Acknowledgements
- **Whisper** by OpenAI for the speech-to-text model.
- **SpeechRecognition** by Anthony Zhang for handling audio recording and recognition.
- **ESP32** by Espressif for providing Wi-Fi and Bluetooth capabilities for wireless communication.
- **Elegoo Smart Robot Car V4** for the base hardware and integration with the ESP32 board.

## Demonstration video  
This [video](https://youtu.be/0AbyosnZ-v8) demonstrates the project works. 


     
