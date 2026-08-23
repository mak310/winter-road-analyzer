ROAD_DATA = {
    "乾燥路面": {
        "mu": 0.80,
        "risk": "★☆☆☆☆",
        "tire": "サマータイヤ",
        "speed": "法定速度内"
    },

    "湿潤路面": {
        "mu": 0.50,
        "risk": "★★☆☆☆",
        "tire": "オールシーズンタイヤ",
        "speed": "60 km/h以下"
    },

    "圧雪路面": {
        "mu": 0.30,
        "risk": "★★★☆☆",
        "tire": "スタッドレスタイヤ",
        "speed": "40 km/h以下"
    },

    "凍結路面": {
        "mu": 0.10,
        "risk": "★★★★★",
        "tire": "高性能スタッドレスタイヤ",
        "speed": "30 km/h以下"
    }
}


def analyze_road(road_type):

    return ROAD_DATA[road_type]


if __name__ == "__main__":

    result = analyze_road("凍結路面")

    print("路面状態:", "凍結路面")
    print("推定μ:", result["mu"])
    print("危険度:", result["risk"])
    print("推奨タイヤ:", result["tire"])
    print("推奨速度:", result["speed"])