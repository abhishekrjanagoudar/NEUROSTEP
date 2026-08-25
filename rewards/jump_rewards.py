def jump_height_reward(jump_height: float) -> float:
    return max(0.0, jump_height)


def landing_stability_reward(stability_score: float) -> float:
    return max(0.0, stability_score)
