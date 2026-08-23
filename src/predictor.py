import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

MODEL_PATH = "models/winter_road_model.keras"

CLASS_NAMES = [
    "dry",
    "ice",
    "slush",
    "snow",
    "wet"
]


def predict_road(image_path):

    model = tf.keras.models.load_model(
        MODEL_PATH
    )

    img = image.load_img(
        image_path,
        target_size=(224, 224)
    )

    img_array = image.img_to_array(
        img
    )

    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    predictions = model.predict(
        img_array,
        verbose=0
    )

    score = tf.nn.softmax(
        predictions[0]
    )

    road_class = CLASS_NAMES[
        np.argmax(score)
    ]

    confidence = float(
        100 * np.max(score)
    )

    return road_class, confidence


if __name__ == "__main__":

    image_path = input(
        "画像パスを入力してください: "
    )

    road_class, confidence = predict_road(
        image_path
    )

    print(
        f"\n判定結果: {road_class}"
    )

    print(
        f"信頼度: {confidence:.1f}%"
    )