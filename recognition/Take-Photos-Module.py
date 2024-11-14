import os
import cv2
import numpy as np
import pandas as pd
from datetime import datetime

def load_id_names(filename):
    if os.path.isfile(filename):
        return pd.read_csv(filename)[['id', 'name']]
    else:
        df = pd.DataFrame(columns=['id', 'name'])
        df.to_csv(filename, index=False)
        return df

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def capture_photos(camera, classifier, user_id, save_dir):
    count = 0
    while cv2.waitKey(1) & 0xFF != ord('q'):
        ret, frame = camera.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = classifier.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            face = gray_frame[y:y + h, x:x + w]
            if cv2.waitKey(1) & 0xFF == ord('s') and np.mean(face) > 50:
                resized_face = cv2.resize(face, (220, 220))
                filename = f'face.{user_id}.{datetime.now().microsecond}.jpeg'
                cv2.imwrite(os.path.join(save_dir, filename), resized_face)
                count += 1
                print(f'{count} -> Photos taken!')
        cv2.imshow('Face', frame)

def main():
    filename = 'id-names.csv'
    faces_directory = 'faces'
    classifier_file = 'Classifiers/haarface.xml'

    id_names = load_id_names(filename)
    ensure_directory_exists(faces_directory)

    print('Добро пожаловать!')
    print('\nПожалуйста, введите свой ID.')
    print('Если вы здесь впервые, выберите случайный ID от 1 до 10000.')

    user_id = int(input('ID: '))
    user_name = ''
    user_directory = os.path.join(faces_directory, str(user_id))  # Инициализация переменной

    if user_id in id_names['id'].values:
        user_name = id_names.loc[id_names['id'] == user_id, 'name'].values[0]
        print(f'С возвращением, {user_name}!!')
    else:
        user_name = input('Пожалуйста, введите ваше имя: ')
        ensure_directory_exists(user_directory)
        new_entry = pd.DataFrame([{'id': user_id, 'name': user_name}])
        id_names = pd.concat([id_names, new_entry], ignore_index=True)
        id_names.to_csv(filename, index=False)
    ensure_directory_exists(user_directory)

    print("\nДавайте начнем съемку!")
    print("Теперь вы можете начать делать фотографии. Как только вы увидите прямоугольник вокруг вашего лица, нажмите клавишу 's', чтобы сделать снимок.", end=" ")
    print("Рекомендуется сделать как минимум 20-25 фотографий под разными углами и в разных позах, с очками и без.")
    input("\nНажмите ENTER, чтобы начать, и 'q', чтобы выйти, когда закончите!")

    camera = cv2.VideoCapture(0)
    face_classifier = cv2.CascadeClassifier(classifier_file)

    capture_photos(camera, face_classifier, user_id, user_directory)

    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
