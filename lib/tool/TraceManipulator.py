class TraceManipulator(object):
  
  @staticmethod
  def getEnlargedTrace(trace, enlarge):
    new_coordinates = []
    current_step = 0
    
    while current_step <= len(trace)-1:
      new_coordinates.append(trace[current_step])
      for expand_coo in TraceManipulator.enlargeCoordonate(trace[current_step], enlarge):
        new_coordinates.append(expand_coo)
      current_step += enlarge
    
    return list(set(new_coordinates))
  
  @staticmethod
  def enlargeCoordonate(coordinate, step):
    coordinates = []
    
    for width in range(step):
      width += 1
      ref_coo = (coordinate[0]-width, coordinate[1]-width)
      coordinates.append(ref_coo)
      
      for width2 in range(step):
        width2 += 1
        
        coordinates.append((ref_coo[0], ref_coo[1]+width2))
        coordinates.append((ref_coo[0]+width2, ref_coo[1]))
      
    return coordinates
