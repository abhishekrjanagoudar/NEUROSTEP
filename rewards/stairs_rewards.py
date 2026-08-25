def progress_reward(step_progress: float) -> float:
    return max(0.0, step_progress)


def stumble_penalty(stumble_events: int, weight: float = 0.2) -> float:
    return -weight * float(stumble_events)
