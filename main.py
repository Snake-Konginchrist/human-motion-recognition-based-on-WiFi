# main.py
# 主程序，整合数据收集、预处理、模型训练和动作识别的流程

from data.collect_data import collect_wifi_signals
from data.preprocess_data import preprocess_data
from model.train_model import train_model
from model.predict_action import predict_action
from utils.utils import evaluate_model


def main():
    # 收集数据
    print("收集Wi-Fi信号数据...")
    collect_wifi_signals()

    # 数据预处理
    print("预处理数据...")
    preprocess_data()

    # 训练模型
    print("训练模型中...")
    train_model()

    # 动作识别
    print("识别健身动作中...")
    predict_action()

    # 评估模型
    print("评估模型性能...")
    evaluate_model()

    print("流程完成。")


if __name__ == "__main__":
    main()
