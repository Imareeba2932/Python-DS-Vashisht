import cv2

def add_text(frame):
    text = "Obama Speech"
    fs = 1  # scale of font
    font = cv2.FONT_HERSHEY_SIMPLEX
    color = (255, 255, 255) # white color
    thickness = 2
    origin = (50, 50)
    frame = cv2.putText(frame, text, origin, font, fs, color, thickness)
    frame = cv2.putText(frame, "president's translator", (50, 75), font, .5, color, 1)

    return frame

def read_video(path):
    video = cv2.VideoCapture(path)
    while True:
        state, frame = video.read()
        if not state:
            break
        frame = add_text(frame)
        cv2.imshow('frame', frame)          # display the frame
        if cv2.waitKey(10) == ord('q'):      # if you pressed 'q', 
            break                           # then quit
    video.release()                         # free the object
    cv2.destroyAllWindows()                 # close the window

# execute outside function
if __name__ == "__main__":
    read_video(r"C:\Users\ZAID\Videos\obama.mp4")   
