def positions_near(position_ref, position_to_compare, distance, allow_same_position):

  position_x = position_ref[0]
  position_y = position_ref[1]
  position_to_compare_x = position_to_compare[0]
  position_to_compare_y = position_to_compare[1]

  if position_to_compare_x == position_x and position_to_compare_y == position_y:
    if allow_same_position:
      return True
    else:
      return False

  if (position_to_compare_x == position_x or \
  position_to_compare_x == position_x-distance or \
  position_to_compare_x == position_x+distance) and \
  (position_to_compare_y == position_y or \
  position_to_compare_y == position_y-distance or \
  position_to_compare_y == position_y+distance):
    return True
  return False