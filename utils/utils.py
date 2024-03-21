import joblib
from sklearn.metrics import classification_report


def save_model(model, filename):
    """
    保存训练好的模型到指定文件。

    参数:
        model: 训练好的模型实例。
        filename: 保存模型的文件路径。
    """
    joblib.dump(model, filename)
    print(f"Model saved to {filename}")


def load_model(filename):
    """
    从指定文件加载模型。

    参数:
        filename: 模型文件的路径。

    返回:
        加载的模型实例。
    """
    model = joblib.load(filename)
    print(f"Model loaded from {filename}")
    return model


def evaluate_model(model, x_test, y_test):
    """
    评估模型的性能，打印分类报告。

    参数:
        model: 要评估的模型实例。
        X_test: 测试数据集的特征。
        y_test: 测试数据集的真实标签。
    """
    predictions = model.predict(x_test)
    report = classification_report(y_test, predictions)
    print("Model evaluation report:")
    print(report)
