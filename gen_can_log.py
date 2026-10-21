import numpy as np
import pandas as pd

rng = np.random.default_rng(42)

CAN_IDS = ["0x0C9", "0x18F", "0x1A0", "0x2B4", "0x3C1", "0x4E8", "0x5F2"]
WEIGHTS = [0.30, 0.25, 0.15, 0.12, 0.08, 0.06, 0.04]

N = 5000

can_ids = rng.choice(CAN_IDS, size=N, p=WEIGHTS)
dlcs = rng.integers(1, 9, size=N)  # 1~8 字节

timestamps = []
t = 0.0
for _ in range(N):
    t += rng.uniform(0.001, 0.02)
    timestamps.append(round(t, 3))

data_list = []
for dlc in dlcs:
    bs = rng.integers(0, 256, size=dlc)
    data_list.append(" ".join(f"{b:02X}" for b in bs))

df = pd.DataFrame({
    "timestamp": timestamps,
    "can_id": can_ids,
    "data": data_list,
    "dlc": dlcs,
})

df.to_csv("can_log.csv", index=False, encoding="utf-8")
print("已生成 can_log.csv")
print(df.shape)
print(df.head())