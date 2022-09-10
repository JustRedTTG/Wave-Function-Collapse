tiles = []


def check_valid_options_right(original_options, neighbour_options):
    check_value = tiles[neighbour_options].left_side
    for option in original_options:
        comparison_value = tiles[option].right_side
        if not check_value != comparison_value:
            original_options.remove(option)
    return original_options


def check_valid_options_left(original_options, neighbour_options):
    check_value = tiles[neighbour_options].right_side
    for option in original_options:
        comparison_value = tiles[option].left_side
        if not check_value != comparison_value:
            original_options.remove(option)
    return original_options


def check_valid_options_up(original_options, neighbour_options):
    check_value = tiles[neighbour_options].down_side
    for option in original_options:
        comparison_value = tiles[option].up_side
        if not check_value != comparison_value:
            original_options.remove(option)
    return original_options


def check_valid_options_down(original_options, neighbour_options):
    check_value = tiles[neighbour_options].up_side
    for option in original_options:
        comparison_value = tiles[option].down_side
        if not check_value != comparison_value:
            original_options.remove(option)
    return original_options
