# 模型训练脚本
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def train_model():
    # 生成模拟数据
    x, y = make_classification(n_samples=1000, n_features=20, n_classes=3, n_informative=4, random_state=42)

    # 分割数据集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

    # 训练随机森林模型
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(x_train, y_train)

    # 验证模型性能
    predictions = model.predict(x_test)
    print(f"Model accuracy: {accuracy_score(y_test, predictions)}")
