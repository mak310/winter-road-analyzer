from pathlib import Path

import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import models

# データセットフォルダ
DATASET_DIR = Path("dataset")

# 画像サイズ
IMG_HEIGHT = 224
IMG_WIDTH = 224
BATCH_SIZE = 8

# データ読み込み
train_ds = tf.keras.utils.image_dataset_from_directory(
    DATASET_DIR,
    validation_split=0.2,
    subset="training",
    seed=42,
    image_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE
)

val_ds = tf.keras.utils.image_dataset_from_directory(
    DATASET_DIR,
    validation_split=0.2,
    subset="validation",
    seed=42,
    image_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE
)

class_names = train_ds.class_names

print("クラス一覧")
print(class_names)

# パフォーマンス最適化
AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.prefetch(buffer_size=AUTOTUNE)

# モデル作成
model = models.Sequential([

    layers.Rescaling(
        1.0 / 255,
        input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)
    ),

    layers.Conv2D(
        16,
        3,
        activation="relu"
    ),

    layers.MaxPooling2D(),

    layers.Conv2D(
        32,
        3,
        activation="relu"
    ),

    layers.MaxPooling2D(),

    layers.Conv2D(
        64,
        3,
        activation="relu"
    ),

    layers.MaxPooling2D(),

    layers.Flatten(),

    layers.Dense(
        128,
        activation="relu"
    ),

    layers.Dense(
        len(class_names)
    )
])

model.compile(
    optimizer="adam",
    loss=tf.keras.losses.SparseCategoricalCrossentropy(
        from_logits=True
    ),
    metrics=["accuracy"]
)

# 学習
history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=10
)

# モデル保存
Path("models").mkdir(exist_ok=True)

model.save(
    "models/winter_road_model.keras"
)

print("\n学習完了")
print("保存先: models/winter_road_model.keras")