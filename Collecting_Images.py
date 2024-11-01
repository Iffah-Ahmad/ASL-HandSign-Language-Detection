import os
import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 30
dataset_size = 100

def collect_images_for_new_class():
    new_class_name = input("Enter the name for the new class: ")
    new_class_index = len([name for name in os.listdir(DATA_DIR) if os.path.isdir(os.path.join(DATA_DIR, name))])

    if new_class_index >= number_of_classes:
        print(f"Error: Maximum number of classes ({number_of_classes}) reached.")
        return

    class_dir = os.path.join(DATA_DIR, new_class_name)
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print(f'Collecting data for class {new_class_name} (index: {new_class_index})')

    cap = cv2.VideoCapture(0)  # Use camera index 0 for the default camera, adjust as needed
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        cv2.putText(frame, 'Ready? Press "Q" to start!', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(class_dir, '{}.jpg'.format(counter)), frame)

        counter += 1

    cap.release()
    cv2.destroyAllWindows()

if _name_ == "_main_":
    collect_images_for_new_class()