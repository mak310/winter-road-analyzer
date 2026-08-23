ROAD_DATA = {
    "乾燥路面": {
        "mu": 0.80,
        "risk": "★☆☆☆☆",
        "tire": "サマータイヤ",
        "speed": "法定速度内",
        "brake_distance": "1.0倍",
        "advice": (
            "通常走行可能です。\n"
            "法定速度を守って安全運転してください。"
        )
    },

    "湿潤路面": {
        "mu": 0.50,
        "risk": "★★☆☆☆",
        "tire": "オールシーズンタイヤ",
        "speed": "60 km/h以下",
        "brake_distance": "1.5倍",
        "advice": (
            "急ブレーキを避けてください。\n"
            "車間距離を十分に確保してください。"
        )
    },

    "シャーベット路面": {
        "mu": 0.25,
        "risk": "★★★★☆",
        "tire": "スタッドレスタイヤ",
        "speed": "35 km/h以下",
        "brake_distance": "3.5倍",
        "advice": (
            "シャーベットプレーニングに注意してください。\n"
            "急な車線変更を避けてください。"
        )
    },

    "圧雪路面": {
        "mu": 0.30,
        "risk": "★★★☆☆",
        "tire": "スタッドレスタイヤ",
        "speed": "40 km/h以下",
        "brake_distance": "2.5倍",
        "advice": (
            "急加速を避けてください。\n"
            "カーブ手前で十分減速してください。"
        )
    },

    "凍結路面": {
        "mu": 0.10,
        "risk": "★★★★★",
        "tire": "高性能スタッドレスタイヤ",
        "speed": "30 km/h以下",
        "brake_distance": "5.0倍",
        "advice": (
            "急ハンドル・急ブレーキは禁止です。\n"
            "十分な車間距離を確保してください。"
        )
    }
}


def analyze_road(road_type):
    return ROAD_DATA[road_type]


if __name__ == "__main__":

    road_type = "シャーベット路面"

    result = analyze_road(road_type)

    print("路面状態 :", road_type)
    print("推定μ :", result["mu"])
    print("危険度 :", result["risk"])
    print("推奨タイヤ :", result["tire"])
    print("推奨速度 :", result["speed"])
    print("制動距離係数 :", result["brake_distance"])
    print("運転アドバイス :")
    print(result["advice"])