import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep

# --- 1. SETUP ---
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Width
cap.set(4, 720)   # Height

detector = HandDetector(detectionCon=0.8)

# Define the standard keys
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]

finalText = "" # This variable holds what you have typed

# --- 2. BUTTON CLASS ---
class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text

# Create standard letter buttons
buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 50, 100 * i + 50], key))

# Add Special Buttons (SPACE and DELETE) manually
# We make them wider (size=[200, 85])
buttonList.append(Button([250, 350], "SPACE", size=[200, 85])) 
buttonList.append(Button([500, 350], "DEL", size=[200, 85]))

# --- 3. DRAWING FUNCTION ---
def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        
        # Draw Button Shape
        # Using cvzone.cornerRect looks cooler, but standard rectangle is safer for beginners
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), cv2.FILLED)
        
        # Draw Letter
        # Adjust text position based on length (center the text)
        if len(button.text) > 1: # For "SPACE" and "DEL"
            cv2.putText(img, button.text, (x + 20, y + 60),
                        cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
        else: # For single letters
            cv2.putText(img, button.text, (x + 20, y + 65),
                        cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
    return img

# --- 4. MAIN LOOP ---
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1) # Mirror view
    
    hands, img = detector.findHands(img) 
    img = drawAll(img, buttonList)

    # DRAW THE TEXT BOX (Where words appear)
    # White background, Black text
    cv2.rectangle(img, (50, 450), (1200, 550), (255, 255, 255), cv2.FILLED)
    cv2.putText(img, finalText, (60, 525),
                cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 0), 5)

    if hands:
        hand1 = hands[0]
        lmList = hand1["lmList"]
        
        if lmList:
            # 8 is Index Tip, 4 is Thumb Tip
            x8, y8 = lmList[8][0], lmList[8][1] 
            x4, y4 = lmList[4][0], lmList[4][1]
            
            for button in buttonList:
                x, y = button.pos
                w, h = button.size

                # CHECK HOVER
                if x < x8 < x + w and y < y8 < y + h:
                    
                    # Change color to darker purple
                    cv2.rectangle(img, (x, y), (x + w, y + h), (175, 0, 175), cv2.FILLED)
                    
                    # Redraw text on top
                    if len(button.text) > 1:
                        cv2.putText(img, button.text, (x + 20, y + 60), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
                    else:
                        cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                    
                    # CHECK CLICK (Distance)
                    length, info, img = detector.findDistance((x8, y8), (x4, y4), img)
                    
                    if length < 30:
                        # CLICKED! (Green Color)
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), cv2.FILLED)
                        
                        # --- HANDLING THE TYPING ---
                        if button.text == "SPACE":
                            finalText += " "
                        elif button.text == "DEL":
                            finalText = finalText[:-1] # Remove last character
                        else:
                            finalText += button.text # Add letter
                        
                        sleep(0.2) # Delay to prevent double clicking

    cv2.imshow("Virtual Keyboard", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break