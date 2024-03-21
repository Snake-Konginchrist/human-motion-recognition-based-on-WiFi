# Wi-Fi智能动作识别系统

## 项目简介

Wi-Fi智能动作识别系统是一个创新项目，旨在通过Wi-Fi信号分析，无需任何附加传感器即可识别人体健身动作。此系统利用机器学习技术，可广泛应用于家庭自动化、安全监控、健康监测等多种场合。

## 如何使用

1. **数据收集**：运行`data/collect_data.py`以收集Wi-Fi信号数据。
2. **数据预处理**：执行`data/preprocess_data.py`对收集的数据进行预处理。
3. **模型训练**：通过`model/train_model.py`训练机器学习模型。
4. **动作识别**：使用`model/predict_action.py`来识别新的动作。

## 开发环境

- Python 3.8+
- Scikit-learn
- NumPy

## 贡献

欢迎通过Issue或Pull Request参与项目贡献。请确保你的代码清晰并且有适当的注释。

## 许可

该项目采用MIT许可证。详见[LICENSE](LICENSE)文件。