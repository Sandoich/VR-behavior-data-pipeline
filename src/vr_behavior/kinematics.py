def compute_midpoint_time_delta(data_frame, time_col="VarjoTime", group_col="AOI"):
    """
    Compute midpoint-based time differences for acceleration calculation.

    This method estimates time deltas using midpoints between consecutive frames,
    which is more stable for acceleration computation.
    """
    data_frame = data_frame.sort_values(by=[group_col, time_col])

    data_frame["delta_time_mid"] = (
        data_frame.groupby(group_col)[time_col].shift(1) + data_frame[time_col]) / 2

    data_frame["delta_time_mid"] = data_frame["delta_time_mid"].diff()
    return data_frame



def compute_angular_kinematics(data_frame):
    """
    Compute angular velocity and angular acceleration from VR rotation data.

    Parameters
    ----------
    data_frame : pandas.DataFrame
        Input dataframe containing quaternion rotation data and timestamps.
        Required columns:
        - rx, ry, rz, rw : quaternion rotation
        - VarjoTime : timestamp in nanoseconds
        - AOI : grouping identifier

    Returns
    -------
    pandas.DataFrame
        DataFrame with additional columns:
        - rotation_difference
        - velocity_rota
        - acceleration_rota
    """

    
    # 换算欧拉角
    # Calculate Euler angles
    data_frame = calculate_euler_angles(data_frame)
    
    # delta_VarjoTime = 后一帧-前一帧的时间差
    # delta_VarjoTime = time difference between the next frame and the previous frame
    data_frame = calculate_AOI_time_difference(data_frame)
    
    # rotation_difference 后一帧与前一帧之间弧度的变量
    # rotation_difference: variable representing the angle difference between the next frame and the previous frame
    data_frame = calculate_rotation_sum(data_frame)
    
    
    # 每一帧的速度 = 后一帧-前一帧的rotation位移/每一帧的时间差
    # Velocity of each frame = rotation displacement between consecutive frames/time difference of each frame
    data_frame['velocity_rota'] = data_frame['rotation_difference'] / data_frame['delta_VarjoTime']
   
    
    # 计算后一帧与前一帧的速度差
    # Calculate the velocity difference between the next frame and the previous frame
    data_frame['delta_velocity_rota'] = data_frame.groupby('AOI')['velocity_rota'].diff()
    

    data_frame = compute_midpoint_time_delta(data_frame)

    # 计算每一帧的加速度 = 后一帧的速度-前一帧的速度/每一帧的时间差
    # Calculate the acceleration of each frame = velocity of the next frame - velocity of the previous frame/time difference of each frame
    data_frame['acceleration_rota'] = data_frame['delta_velocity_rota'] / data_frame['delta_time_mid']
    
    return data_frame
