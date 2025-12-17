import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

import numpy as np
import pandas as pd

from vr_behavior.kinematics import compute_angular_kinematics


# ---- create dummy data ----
n = 200
df = pd.DataFrame({
    "VarjoTime": np.linspace(0, 5e9, n),
    "AOI": ["A"] * n,
    "rx": np.random.rand(n),
    "ry": np.random.rand(n),
    "rz": np.random.rand(n),
    "rw": np.random.rand(n),
})

# ---- run feature extraction ----
out = compute_angular_kinematics(df)

print(out[["velocity_rota", "acceleration_rota"]].head())



