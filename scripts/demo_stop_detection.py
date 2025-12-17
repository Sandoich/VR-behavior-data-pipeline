import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

import numpy as np
import pandas as pd

from vr_behavior.kinematics import compute_angular_kinematics
from vr_behavior.stop_detection import find_stationary_intervals, merge_intervals

# dummy data
n = 200
df = pd.DataFrame({
    "VarjoTime": np.linspace(0, 5e9, n),
    "AOI": ["A"] * n,
    "rx": np.random.rand(n),
    "ry": np.random.rand(n),
    "rz": np.random.rand(n),
    "rw": np.random.rand(n),
})

df = compute_angular_kinematics(df)

intervals = find_stationary_intervals(df, speed_col="velocity_rota", threshold=2e-11)
merged = merge_intervals(intervals, max_gap_s=0.09)

print("Raw intervals:", len(intervals))
print("Merged intervals:", len(merged))
print(merged.head())
