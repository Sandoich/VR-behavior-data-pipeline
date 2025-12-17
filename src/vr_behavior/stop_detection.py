import pandas as pd

def find_stationary_intervals(df, time_col="VarjoTime", speed_col="velocity_rota", threshold=2e-11):
    """
    Find stationary intervals where speed is below a threshold.

    Returns a DataFrame with columns: start_time, end_time, duration_s
    """
    df = df.dropna(subset=[time_col, speed_col]).sort_values(time_col).copy()
    is_stationary = df[speed_col] < threshold

    # group consecutive True/False blocks
    groups = (is_stationary != is_stationary.shift()).cumsum()
    stationary_df = df[is_stationary].copy()
    if stationary_df.empty:
        return pd.DataFrame(columns=["start_time", "end_time", "duration_s"])

    start_times = stationary_df.groupby(groups.loc[stationary_df.index])[time_col].min()
    end_times = stationary_df.groupby(groups.loc[stationary_df.index])[time_col].max()

    intervals = pd.DataFrame({"start_time": start_times, "end_time": end_times}).reset_index(drop=True)
    intervals = intervals[intervals["start_time"] != intervals["end_time"]]
    intervals["duration_s"] = (intervals["end_time"] - intervals["start_time"]) / 1e9
    return intervals


def merge_intervals(intervals, max_gap_s=0.09):
    """
    Merge adjacent intervals if the gap between them is below max_gap_s.
    """
    if intervals.empty:
        return intervals

    intervals = intervals.sort_values("start_time").reset_index(drop=True).copy()
    merged = [intervals.iloc[0].to_dict()]

    for i in range(1, len(intervals)):
        prev = merged[-1]
        cur = intervals.iloc[i].to_dict()
        gap_s = (cur["start_time"] - prev["end_time"]) / 1e9

        if gap_s < max_gap_s:
            # merge
            prev["end_time"] = max(prev["end_time"], cur["end_time"])
            prev["duration_s"] = (prev["end_time"] - prev["start_time"]) / 1e9
        else:
            merged.append(cur)

    return pd.DataFrame(merged)
