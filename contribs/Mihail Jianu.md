 I have implemented the following game features:
  - A prototype for the game. It was made in Unity3D as well, and its purpose was for testing only.
  
    - This instance of the game included only one level, with one finishline, and it was able to detect the time it would take the player to reach it.
    
    - The car's model had a cubic form and it could be controlled by the user like a normal car (accelerate, brake, steer left, right).
  - A minimap that is used to show the user the real time current position of the car.
  
    - It implements an overall vision of the track (chasing the car), for the user to follow, in order to identify in advance all the turns that come next.
    
    - It can also be used by an A.I., as the obstacle detection was merged with the minimap, thus the A.I. can see the obstacles directly on the minimap.
    
    - To implement it, I had to add a completely new perspective to the game (bird's eye), and make it follow the car, wherever it is
   
  - A manual/automatic gearbox interface (that was not included in the final release, however).
  
    - It  allows the user to  change between the two types of gearbox, as  well as to shift up or down the between gears in  any fashion  they like.
    
    - In order to write it, I had to add three more input commands (change gear, shift up and shift down, that were mapped to keys 'K', 'B', 'V', respectively)
