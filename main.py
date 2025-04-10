from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Eğitim verisi: [Glikoz, BMI, Yaş]
X = np.array([
    [130, 28.1, 45],
    [85, 22.4, 30],
    [155, 35.0, 50],
    [90, 21.0, 25]
])

# Etiketler: 1 = Diyabet Var, 0 = Yok
y = np.array([1, 0, 1, 0])

# Yeni hasta verisi
yeni_hasta = np.array([[140, 30.2, 48]])

# K-NN modeli (k=3 komşu)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Tahmin
tahmin = model.predict(yeni_hasta)

print("Tahmin Sonucu (1=Diyabet, 0=Sağlıklı):", tahmin[0])
