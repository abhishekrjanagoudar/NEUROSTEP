def upright_bonus(torso_up_projection: float) -> float:
    return max(0.0, torso_up_projection)


def action_penalty(action_l2: float, weight: float = 0.01) -> float:
    return -weight * action_l2
