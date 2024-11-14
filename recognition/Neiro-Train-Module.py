import os
import pandas as pd
import numpy as np
import cv2

def load_id_names(filepath):
    data = pd.read_csv(filepath)
    return data[['id', 'name']]

def train_lbph(face_recognizer, faces_directory, save_path):
    faces, labels = [], []
    for user_id in os.listdir(faces_directory):
        user_path = os.path.join(faces_directory, user_id)
        if not os.path.isdir(user_path):
            continue
        for image_name in os.listdir(user_path):
            image_path = os.path.join(user_path, image_name)
            try:
                face_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                if face_image is not None:
                    faces.append(face_image)
                    labels.append(int(user_id))
            except Exception as e:
                print(f"Error processing image {image_path}: {e}")
                continue
    faces, labels = np.array(faces), np.array(labels)
    print('Training Started')
    face_recognizer.train(faces, labels)
    face_recognizer.save(save_path)
    print('Training Complete!')

def main():
    csv_file = 'id-names.csv'
    faces_directory = 'faces'
    trained_model_path = 'Classifiers/TrainedLBPH.yml'

    id_names = load_id_names(csv_file)

    # Создание объекта LBPHFaceRecognizer
    lbph = cv2.face.LBPHFaceRecognizer_create(threshold=500)

    # Тренировка модели
    train_lbph(lbph, faces_directory, trained_model_path)

if __name__ == '__main__':
    main()