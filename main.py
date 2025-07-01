import pygame
import cv2
import mediapipe as mp
import random
import time
import threading

# Init Pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Gesture Simon Says")
font = pygame.font.SysFont('Arial', 36)

# Setup for MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Global state
gestures = ["Rock", "Paper", "Scissors"]
stop_game = False
camera_gesture = None

def get_gesture_from_camera():
    global camera_gesture, stop_game
    cap = cv2.VideoCapture(0)
    start_time = time.time()

    while time.time() - start_time < 10 and not stop_game:
        success, frame = cap.read()
        if not success:
            continue
        rgb = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand in result.multi_hand_landmarks:
                landmarks = hand.landmark
                camera_gesture = classify_gesture(landmarks)
                if camera_gesture != "Unknown":
                    cap.release()
                    return
    cap.release()

def classify_gesture(landmarks):
    fingers = []
    fingers.append(landmarks[4].x < landmarks[3].x)
    tips = [8, 12, 16, 20]
    for tip in tips:
        fingers.append(landmarks[tip].y < landmarks[tip - 2].y)

    if fingers == [False, False, False, False, False]:
        return "Rock"
    elif fingers == [True, True, True, True, True]:
        return "Paper"
    elif fingers[1] and fingers[2] and not fingers[3] and not fingers[4]:
        return "Scissors"
    return "Unknown"

def draw_text(text, color=(0, 0, 0)):
    screen.fill((255, 255, 255))
    txt = font.render(text, True, color)
    screen.blit(txt, (screen.get_width() // 2 - txt.get_width() // 2, screen.get_height() // 2))
    pygame.display.flip()

def play_level(sequence):
    global stop_game, camera_gesture
    for gesture in sequence:
        draw_text(f"Show: {gesture}")
        camera_gesture = None
        t = threading.Thread(target=get_gesture_from_camera)
        t.start()

        # Wait for either gesture or stop
        while t.is_alive():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stop_game = True
                    return False
        if camera_gesture != gesture:
            draw_text("Wrong!")
            time.sleep(2)
            return False
        draw_text("Correct!")
        time.sleep(1)
    return True

def main():
    global stop_game
    sequence = []
    level = 1
    draw_text("Click to start!")
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False

    while not stop_game:
        draw_text(f"Level {level}")
        time.sleep(1)
        sequence.append(random.choice(gestures))
        if not play_level(sequence):
            break
        level += 1
    draw_text("Game Over!")
    time.sleep(3)
    pygame.quit()

if __name__ == "__main__":
    main()
