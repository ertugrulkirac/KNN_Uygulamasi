import matplotlib.pyplot as plt
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

# K-NN modeli
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Tahmin
tahmin = model.predict(yeni_hasta)
print("Tahmin Sonucu (1=Diyabet, 0=Sağlıklı):", tahmin[0])

# Görselleştirme (sadece Glikoz vs. BMI)
for i in range(len(X)):
    if y[i] == 1:
        plt.scatter(X[i][0], X[i][1], color='red', label='Diyabetli' if i == 0 else "")
    else:
        plt.scatter(X[i][0], X[i][1], color='green', label='Sağlıklı' if i == 1 else "")

# Yeni hastayı göster
plt.scatter(yeni_hasta[0][0], yeni_hasta[0][1], color='blue', marker='x', s=200, label='Yeni Hasta')

plt.xlabel('Glikoz Seviyesi')
plt.ylabel('BMI')
plt.title('K-NN ile Diyabet Tahmini')
plt.legend()
plt.grid(True)
plt.show()
