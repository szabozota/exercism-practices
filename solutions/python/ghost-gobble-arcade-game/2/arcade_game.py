def eat_ghost(power_pellet_active, touching_ghost):
    if power_pellet_active and touching_ghost:
        return True
    else:
        return False


def score(touching_power_pellet, touching_dot):
    if touching_power_pellet or touching_dot:
        return True
    else:
        return False


def lose(power_pellet_active, touching_ghost):
    if not power_pellet_active and touching_ghost:
        return True
    else:
        return False


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    if has_eaten_all_dots and power_pellet_active and touching_ghost:
        return True
    if has_eaten_all_dots and not power_pellet_active and not touching_ghost:
        return True
    if not has_eaten_all_dots and not power_pellet_active and touching_ghost:
        return False
    if not has_eaten_all_dots and power_pellet_active and touching_ghost:
        return False
    if has_eaten_all_dots and touching_ghost:
        return False
