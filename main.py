M=67
H=180
S=float(input())
T=60
E=0.035 * M + ((S / T)**2 / H) * 0.029 * M
print(f"Калорий сожжено: {E}; Дистанция: {S / T * (H / 4 + 0.37)};")