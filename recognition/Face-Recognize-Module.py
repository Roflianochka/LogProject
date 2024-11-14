import pandas as pd
import cv2
from api.tasks import log_face_activity


def load_id_names(filepath):
    data = pd.read_csv(filepath)
    return data[['id', 'name']]


def recognize_faces(camera, face_classifier, face_recognizer, id_names):
    recognized_names = set()  # Для отслеживания уже распознанных имен
    last_seen_names = set()  # Для отслеживания имен, которые были потеряны из вида

    while cv2.waitKey(1) & 0xFF != ord('q'):
        ret, frame = camera.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=4)

        current_names = set()  # Имена, распознанные в текущем кадре

        for (x, y, w, h) in faces:
            face_region = gray_frame[y:y + h, x:x + w]
            face_region = cv2.resize(face_region, (220, 220))
            label, confidence = face_recognizer.predict(face_region)

            try:
                name = id_names.loc[id_names['id'] == label, 'name'].values[0]
                current_names.add(name)  # Добавляем имя в текущий список
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(frame, name, (x, y + h + 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255))

                # Если имя распознано и его ещё не выводили
                if name not in recognized_names:
                    print(f'Распознан: {name}')
                    recognized_names.add(name)  # Добавляем имя в распознанные
                    user_id = label
                    log_face_activity.delay(user_id)
            except IndexError:
                pass

        # Проверяем, потеряны ли имена
        lost_names = last_seen_names - current_names
        for lost_name in lost_names:
            recognized_names.discard(lost_name)  # Убираем имя из распознанных

        last_seen_names = current_names  # Обновляем имена, которые были видны в последнем кадре

        cv2.imshow('Recognize', frame)


def main():
    csv_file = 'id-names.csv'
    classifier_file = 'Classifiers/haarface.xml'
    trained_model_path = 'Classifiers/TrainedLBPH.yml'

    id_names = load_id_names(csv_file)

    face_classifier = cv2.CascadeClassifier(classifier_file)
    lbph = cv2.face.LBPHFaceRecognizer_create(threshold=500)
    lbph.read(trained_model_path)

    camera = cv2.VideoCapture(0)
    recognize_faces(camera, face_classifier, lbph, id_names)

    camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
