import pandas as pd
import numpy as np
import math
import time

# Verileri yükleme ve ön işleme
data = pd.read_csv("tsp_85900_1.txt", header=None, names=["x", "y"])
with open('tsp_85900_1.txt') as f:
    lines = f.readlines()
data = []
for line in lines:
    coords = line.strip().split()
    data.append({'x': float(coords[0]), 'y': float(coords[1])})
    df = pd.DataFrame(data)

df['x'] = df['x'].astype(float)
df['y'] = df['y'].astype(float)



df["visited"] = False

# Uzaklık hesaplama fonksiyonu
def distance(city1, city2):
    x1, y1 = df.at[city1, 'x'], df.at[city1, 'y']
    x2, y2 = df.at[city2, 'x'], df.at[city2, 'y']
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

# TSP çözümü
def solve_tsp():
    start_time = time.time()

    # Şehirleri ziyaret sırasına göre saklayacak bir liste oluşturma
    path = [0]
    current_city = 0
    df.at[current_city, 'visited'] = True

    # Tüm şehirleri ziyaret edene kadar devam eden bir döngü
    while len(path) < len(data):
        # Tüm şehirlerle olan uzaklıkları hesaplama
        distances = [distance(current_city, i) for i in range(len(data))]
        distances[current_city] = np.inf

        # En kısa uzaklığa sahip şehri bulma
        next_city = np.argmin(distances)
        path.append(next_city)
        df.at[next_city, 'visited'] = True
        current_city = next_city

    # Son şehre olan mesafeyi ekleyin ve tamamlanan yolu yazdırma
    path.append(0)
    total_distance = sum([distance(path[i], path[i+1]) for i in range(len(path)-1)])
    print("En kısa yol: ", path)
    print("Toplam mesafe: ", total_distance)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Geçen süre: ", elapsed_time, "saniye")

# Gezgin satıcı problemi çözümünü çağırma
solve_tsp()

