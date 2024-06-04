import cv2
import numpy as np
import telepot
import streamlit as st
from PIL import Image
from datetime import datetime
import pytz
from PIL import ImageEnhance
import os
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
from tensorflow.keras.models import load_model
from playsound import playsound

def getTime():
    IST = pytz.timezone('Asia/Kolkata')
    timeNow = datetime.now(IST)
    return timeNow

def imgenhance():
    image1 = Image.open('violence_frame.jpg')
    curr_bri = ImageEnhance.Sharpness(image1)
    new_bri = 1.3
    img_brightened = curr_bri.enhance(new_bri)
    im1 = img_brightened.save("bright.jpg")

    image2 = Image.open('bright.jpg')
    curr_col = ImageEnhance.Color(image2)
    new_col = 1.5
    img_col = curr_col.enhance(new_col)
    im2 = img_col.save("violence_frame.jpg")

def draw_faces(filename, result_list):
    # load the image
    data = pyplot.imread(filename)
    # plot each face as a subplot
    for i in range(len(result_list)):
        # get coordinates
        x1, y1, width, height = result_list[i]['box']
        x2, y2 = x1 + width, y1 + height
        # define subplot
        pyplot.subplot(1, len(result_list), i+1)
        pyplot.axis('off')
        # plot face
        pyplot.imshow(data[y1:y2, x1:x2])
    # show the plot
    pyplot.savefig("faces.png")
    pyplot.show()

# Load your LRCN model and define CLASSES_LIST, IMAGE_HEIGHT, and IMAGE_WIDTH
def load_lrcn_model():
    # Load your LRCN model here
    model = load_model('LRCN_model_Date_Time_2024_04_07_13_20_07_Loss_0_345083087682724.h5')
    CLASSES_LIST = ["Punch", "Walking", "Kick"]  # Define your classes list
    IMAGE_HEIGHT = 64
    IMAGE_WIDTH = 64

    return model, CLASSES_LIST, IMAGE_HEIGHT, IMAGE_WIDTH

def predict_single_action(frame, model, CLASSES_LIST, IMAGE_HEIGHT, IMAGE_WIDTH):
    filename = 'violence_frame.jpg'
    my_image = 'violence_frame.jpg'
    face_image = 'faces.png'
    SEQUENCE_LENGTH=20
    model = load_model('LRCN_model_Date_Time_2024_04_07_13_20_07_Loss_0_345083087682724.h5')
    temp_video_path = "temp/uploaded_media.mp4"
    with open(temp_video_path, "wb") as f:
        f.write(video_file.getbuffer())

    cap = cv2.VideoCapture(temp_video_path)

    # Initialize the VideoCapture object to read from the video file.
    video_reader = cap

    # Get the width and height of the video.
    original_video_width = int(video_reader.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_video_height = int(video_reader.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Declare a list to store video frames we will extract.
    frames_list = []

    # Initialize a variable to store the predicted action being performed in the video.
    predicted_class_name = ''

    # Get the number of frames in the video.
    video_frames_count = int(video_reader.get(cv2.CAP_PROP_FRAME_COUNT))

    # Calculate the interval after which frames will be added to the list.
    skip_frames_window = max(int(video_frames_count/SEQUENCE_LENGTH), 1)

    # Iterating the number of times equal to the fixed length of sequence.
    for frame_counter in range(SEQUENCE_LENGTH):

        # Set the current frame position of the video.
        video_reader.set(cv2.CAP_PROP_POS_FRAMES, frame_counter * skip_frames_window)

        # Read a frame.
        success, frame = video_reader.read()

        # Check if frame is not read properly then break the loop.
        if not success:
            break

        # Resize the Frame to fixed Dimensions.
        resized_frame = cv2.resize(frame, (IMAGE_HEIGHT, IMAGE_WIDTH))

        # Normalize the resized frame by dividing it with 255 so that each pixel value then lies between 0 and 1.
        normalized_frame = resized_frame / 255

        # Appending the pre-processed frame into the frames list
        frames_list.append(normalized_frame)

    # Passing the  pre-processed frames to the model and get the predicted probabilities.
    predicted_labels_probabilities = model.predict(np.expand_dims(frames_list, axis=0))[0]

    # Get the index of class with highest probability.
    predicted_label = np.argmax(predicted_labels_probabilities)

    # Get the class name using the retrieved index.
    predicted_class_name = CLASSES_LIST[predicted_label]

    if predicted_class_name == "Walking" and predicted_labels_probabilities[predicted_label] <= 0.8:
        predicted_class_name = "Violence detected"
        # Save the frame where violence is detected
        cv2.imwrite('violence_frame.jpg', frame)
        # Send the frame as an alert
        timeMoment = getTime()
        imgenhance()
                # load image from file
        pixels = pyplot.imread(my_image)
        detector = MTCNN()
                # detect faces in the image
        faces = detector.detect_faces(pixels)
                # display faces on the original image
        draw_faces(my_image, faces)
        bot = telepot.Bot('6906694967:AAF0D8H49-5DRIe__DLAnxn_aT7VSCoENqE') ## GET YOUR OWN TELEGRAM GROUP ID AND BOT ID
        bot.sendMessage(-1002127106440, f"VIOLENCE ALERT!! \nLOCATION: Jail Block 2 \nTIME: {timeMoment}")
        bot.sendPhoto(-1002127106440, photo=open('violence_frame.jpg', 'rb'))
        bot.sendMessage(-1002127106440, "FACES OBTAINED")
        bot.sendPhoto(-1002127106440, photo=open('faces.png', 'rb'))

    elif predicted_class_name == "Walking" and predicted_labels_probabilities[predicted_label] > 0.8:
        predicted_class_name = "Non-violence Detected"
    else:
        predicted_class_name = "Violence detected"
        cv2.imwrite('violence_frame.jpg', frame)
        timeMoment = getTime()
        imgenhance()
                # load image from file
        pixels = pyplot.imread(my_image)
        detector = MTCNN()
                # detect faces in the image
        faces = detector.detect_faces(pixels)
                # display faces on the original image
        draw_faces(my_image, faces)
        # Send the frame as an alert
        bot = telepot.Bot('6906694967:AAF0D8H49-5DRIe__DLAnxn_aT7VSCoENqE') ## GET YOUR OWN TELEGRAM GROUP ID AND BOT ID
        bot.sendMessage(-1002127106440, f"VIOLENCE ALERT!! \nLOCATION: Jail Block 2 \nTIME: {timeMoment}")
        bot.sendPhoto(-1002127106440, photo=open('violence_frame.jpg', 'rb'))
        bot.sendMessage(-1002127106440, "FACES OBTAINED")
        bot.sendPhoto(-1002127106440, photo=open('faces.png', 'rb'))


    # Display the predicted action along with the prediction confidence.
    print(f'Action Predicted: {predicted_class_name}\nConfidence: {predicted_labels_probabilities[predicted_label]}')

    # Release the VideoCapture object.
    video_reader.release()
    return(predicted_class_name)




# Streamlit code
st.title('🚨 Violence Detection')
video_file = st.file_uploader("Upload the Video (should be of format '.mp4')", type=["mp4"])

detect_button = st.button("DETECT VIOLENCE")

if detect_button and video_file is not None:
    lrcn_model, CLASSES_LIST, IMAGE_HEIGHT, IMAGE_WIDTH = load_lrcn_model()
    
    # Save the uploaded video file to a temporary location
    temp_video_path = "temp/uploaded_media.mp4"
    with open(temp_video_path, "wb") as f:
        f.write(video_file.getbuffer())

    cap = cv2.VideoCapture(temp_video_path)
    time_moment = getTime()  # You need to replace this with the actual time moment

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        predicted_class_name = predict_single_action(frame, lrcn_model, CLASSES_LIST, IMAGE_HEIGHT, IMAGE_WIDTH)
        if predicted_class_name == "Violence detected":
            st.error("Violence detected! Alert sent.")
            
            

            break
        else:
            st.success("NO Violence")
            break

    cap.release()
    # Remove the temporary video file after processing
    os.remove(temp_video_path)
