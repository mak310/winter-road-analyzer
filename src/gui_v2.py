import io

import PySimpleGUI as sg
from PIL import Image

from predictor import predict_road
from road_analyzer import analyze_road


ROAD_MAPPING = {
    "dry": "乾燥路面",
    "wet": "湿潤路面",
    "slush": "シャーベット路面",
    "snow": "圧雪路面",
    "ice": "凍結路面"
}


def load_image(path, size=(500, 300)):

    image = Image.open(path)

    image.thumbnail(size)

    bio = io.BytesIO()

    image.save(
        bio,
        format="PNG"
    )

    return bio.getvalue()


selected_image = None

layout = [

    [
        sg.Text(
            "Winter Road Analyzer",
            font=("Meiryo", 22, "bold")
        )
    ],

    [
        sg.Button("画像選択")
    ],

    [
        sg.Image(
            key="-IMAGE-"
        )
    ],

    [
        sg.Text("選択画像")
    ],

    [
        sg.Text(
            "未選択",
            key="-FILE-",
            size=(80, 2)
        )
    ],

    [
        sg.HorizontalSeparator()
    ],

    [
        sg.Button(
            "AI判定",
            size=(15, 1)
        )
    ],

    [
        sg.Text("AI判定結果")
    ],

    [
        sg.Text(
            "-",
            key="-AI-ROAD-",
            font=("Meiryo", 20, "bold")
        )
    ],

    [
        sg.Text("信頼度")
    ],

    [
        sg.Text(
            "-",
            key="-CONFIDENCE-",
            font=("Meiryo", 14)
        )
    ],

    [
        sg.Text("推定μ")
    ],

    [
        sg.Text(
            "-",
            key="-MU-",
            font=("Meiryo", 18)
        )
    ],

    [
        sg.Text("危険度")
    ],

    [
        sg.Text(
            "-",
            key="-RISK-",
            font=("Meiryo", 18)
        )
    ],

    [
        sg.Text("推奨タイヤ")
    ],

    [
        sg.Text(
            "-",
            key="-TIRE-",
            font=("Meiryo", 16)
        )
    ],

    [
        sg.Text("推奨速度")
    ],

    [
        sg.Text(
            "-",
            key="-SPEED-",
            font=("Meiryo", 16)
        )
    ],

    [
        sg.Text("制動距離係数")
    ],

    [
        sg.Text(
            "-",
            key="-BRAKE-",
            font=("Meiryo", 16)
        )
    ],

    [
        sg.Text("運転アドバイス")
    ],

    [
        sg.Multiline(
            "",
            size=(60, 5),
            key="-ADVICE-",
            disabled=True
        )
    ],

    [
        sg.Button("終了")
    ]
]

window = sg.Window(
    "Winter Road Analyzer v4.0",
    layout,
    size=(800, 950),
    finalize=True
)

while True:

    event, values = window.read()

    if event in (
        sg.WINDOW_CLOSED,
        "終了"
    ):
        break

    if event == "画像選択":

        filename = sg.popup_get_file(
            "路面画像を選択",
            file_types=(
                (
                    "Image Files",
                    "*.jpg;*.jpeg;*.png"
                ),
            )
        )

        if filename:

            try:

                selected_image = filename

                image_data = load_image(
                    filename
                )

                window["-IMAGE-"].update(
                    data=image_data
                )

                window["-FILE-"].update(
                    filename
                )

            except Exception as e:

                sg.popup_error(
                    f"画像読込エラー\n{e}"
                )

    if event == "AI判定":

        if not selected_image:

            sg.popup_error(
                "先に画像を選択してください。"
            )

            continue

        try:

            road_class, confidence = predict_road(
                selected_image
            )

            road_type = ROAD_MAPPING[
                road_class
            ]

            result = analyze_road(
                road_type
            )

            window["-AI-ROAD-"].update(
                road_type
            )

            window["-CONFIDENCE-"].update(
                f"{confidence:.1f}%"
            )

            window["-MU-"].update(
                f"{result['mu']:.2f}"
            )

            window["-RISK-"].update(
                result["risk"]
            )

            window["-TIRE-"].update(
                result["tire"]
            )

            window["-SPEED-"].update(
                result["speed"]
            )

            window["-BRAKE-"].update(
                result["brake_distance"]
            )

            window["-ADVICE-"].update(
                result["advice"]
            )

        except Exception as e:

            sg.popup_error(
                f"AI判定エラー\n{e}"
            )

window.close()