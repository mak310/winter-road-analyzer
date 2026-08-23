import PySimpleGUI as sg

from road_analyzer import analyze_road

layout = [

    [
        sg.Text(
            "Winter Road Analyzer",
            font=("Meiryo", 18, "bold")
        )
    ],

    [
        sg.Text("路面種別")
    ],

    [
        sg.Combo(
            [
                "乾燥路面",
                "湿潤路面",
                "圧雪路面",
                "凍結路面"
            ],
            default_value="乾燥路面",
            key="-ROAD-",
            readonly=True,
            size=(20, 1)
        )
    ],

    [
        sg.Button("判定")
    ],

    [
        sg.HorizontalSeparator()
    ],

    [
        sg.Text("推定μ")
    ],

    [
        sg.Text(
            "-",
            key="-MU-",
            font=("Meiryo", 16)
        )
    ],

    [
        sg.Text("危険度")
    ],

    [
        sg.Text(
            "-",
            key="-RISK-",
            font=("Meiryo", 16)
        )
    ],

    [
        sg.Text("推奨タイヤ")
    ],

    [
        sg.Text(
            "-",
            key="-TIRE-",
            font=("Meiryo", 14)
        )
    ],

    [
        sg.Text("推奨速度")
    ],

    [
        sg.Text(
            "-",
            key="-SPEED-",
            font=("Meiryo", 14)
        )
    ],

    [
        sg.Text("制動距離係数")
    ],

    [
        sg.Text(
            "-",
            key="-BRAKE-",
            font=("Meiryo", 14)
        )
    ],

    [
        sg.Text("運転アドバイス")
    ],

    [
        sg.Multiline(
            "",
            size=(45, 4),
            key="-ADVICE-",
            disabled=True
        )
    ],

    [
        sg.Button("終了")
    ]

]

window = sg.Window(
    "Winter Road Analyzer",
    layout,
    size=(600, 650)
)

while True:

    event, values = window.read()

    if event in (
        sg.WINDOW_CLOSED,
        "終了"
    ):
        break

    if event == "判定":

        result = analyze_road(
            values["-ROAD-"]
        )

        window["-MU-"].update(
            f'{result["mu"]:.2f}'
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

window.close()