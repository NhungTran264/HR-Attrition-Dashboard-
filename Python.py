import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')  # tên file dataset Kaggle
df.shape
df.head()
df['Attrition'].value_counts(normalize=True)

# Bỏ các cột không có giá trị dự đoán (ID, cột hằng số)
df = df.drop(columns=['EmployeeCount', 'EmployeeNumber', 'Over18', 'StandardHours'])

# Encode target
df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})

# One-hot encode các cột categorical còn lại
categorical_cols = df.select_dtypes(include='object').columns.tolist()
df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

X = df_encoded.drop(columns=['Attrition'])
y = df_encoded['Attrition']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# Logistic Regression cần scale dữ liệu
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

log_model = LogisticRegression(max_iter=1000, class_weight='balanced')
log_model.fit(X_train_scaled, y_train)

# Random Forest không cần scale, tự xử lý tốt hơn với dữ liệu hỗn hợp
rf_model = RandomForestClassifier(n_estimators=200, class_weight='balanced', random_state=42)
rf_model.fit(X_train, y_train)

from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

y_pred_rf = rf_model.predict(X_test)
print(classification_report(y_test, y_pred_rf))
print("ROC-AUC:", roc_auc_score(y_test, rf_model.predict_proba(X_test)[:,1]))

importances = pd.DataFrame({
    'Feature': X.columns,
    'Importance': rf_model.feature_importances_
}).sort_values(by='Importance', ascending=False)

top10 = importances.head(10)
print(top10)

plt.figure(figsize=(8,6))
sns.barplot(data=top10, x='Importance', y='Feature')
plt.title('Top 10 Yếu Tố Ảnh Hưởng Đến Attrition')
plt.tight_layout()
plt.savefig('feature_importance.png', dpi=150)
plt.show()
