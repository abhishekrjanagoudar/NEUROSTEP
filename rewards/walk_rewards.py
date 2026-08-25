def velocity_tracking_reward(forward_velocity_error: float) -> float:
    return max(0.0, 1.0 - forward_velocity_error)


def energy_penalty(joint_torque_l2: float, weight: float = 0.001) -> float:
    return -weight * joint_torque_l2
