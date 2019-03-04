# Problem definition:

  There is an arbitrary line segment, which start point (wall1) and end point (wall2) are defined by a pair of tuples:  
(x1, y1) and (x2, y2).  
There is also an arbitrary vector which start and end point are defined in the same way.  
  
  
The need is to evaluate whether the vector (which could be extended) hits the line segment.  
If it does, it's also needed to evaluate how close their intersection point lies to the segment's center point.  
If the vector crosses the segment in its center point, the result is 100%.  
If the vector crosses one of the segments edge points, the result is 0%.
