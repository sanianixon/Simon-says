# Gesture-Controlled Simon Says

An interactive Simon Says memory game controlled through real-time hand gestures.

Instead of using a keyboard or mouse, players perform Rock, Paper and Scissors gestures in front of their webcam. The game detects each gesture using OpenCV and MediaPipe and checks whether the player correctly repeats the generated sequence.

## Features

- Real-time webcam input
- Hand tracking using MediaPipe
- Rock, Paper and Scissors gesture recognition
- Gesture-based gameplay without keyboard controls
- Randomly generated gesture sequences
- Increasing difficulty after every successful level
- Real-time correct and incorrect feedback
- Automatic game-over detection
- Interactive interface built with Pygame

## How the Game Works

1. The player clicks the game window to begin.
2. The game generates the first gesture in the sequence.
3. The player performs the displayed gesture in front of the webcam.
4. MediaPipe detects the hand landmarks.
5. The application classifies the gesture as Rock, Paper or Scissors.
6. If the gesture is correct, the sequence becomes one step longer.
7. The player must repeat the complete sequence.
8. The game ends when an incorrect gesture is detected.

Example:

```text
Level 1: Rock
Level 2: Rock → Paper
Level 3: Rock → Paper → Scissors
```

## Gesture Recognition

The application uses MediaPipe to identify hand landmarks through the webcam.

Finger positions are then analysed to classify three gestures:

- **Rock:** All fingers are closed
- **Paper:** All fingers are open
- **Scissors:** Index and middle fingers are open

The recognised gesture is compared with the current gesture expected by the game.

## Technology Stack

- Python
- OpenCV
- MediaPipe
- Pygame
- Threading
- Computer vision

## Project Structure

```text
Simon-says/
├── main.py
└── README.md
```

The current implementation is contained in a single Python file. It handles:

- Webcam access
- Hand landmark detection
- Gesture classification
- Sequence generation
- Game progression
- Pygame interface and feedback

## Installation

Clone the repository:

```bash
git clone https://github.com/sanianixon/Simon-says.git
```

Open the project directory:

```bash
cd Simon-says
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install pygame opencv-python mediapipe
```

Run the game:

```bash
python main.py
```

## Requirements

- Python
- A working webcam
- Permission for Python to access the camera
- A well-lit environment for more reliable gesture detection

## What This Project Demonstrates

- Real-time computer vision
- Hand landmark detection
- Gesture classification
- Webcam processing with OpenCV
- Human-computer interaction
- Event-driven game development
- Multithreading
- Sequence and memory-game logic
- Pygame interface development

## Current Limitations

- Gesture recognition depends on lighting and camera quality
- Only Rock, Paper and Scissors gestures are supported
- Hand orientation may affect recognition accuracy
- The application currently supports one hand at a time
- The game must be run locally because it requires webcam access

## Future Improvements

- Add a live camera preview
- Improve gesture-classification accuracy
- Support left- and right-handed users more reliably
- Add more gesture types
- Add difficulty levels
- Include sound effects and animations
- Display the current score and highest level
- Add a restart button
- Separate camera, gesture and game logic into different modules
- Package the application as a desktop executable

## Author

Sania Nixon

- GitHub: [sanianixon](https://github.com/sanianixon)
- LinkedIn: [Sania Nixon](https://linkedin.com/in/sania-nixon)
