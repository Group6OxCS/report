I worked exclusively on the game. The features I have implemented include:
 
* __The car__ (March 17)
    
    I used the Unity standard assets car, which came with model and control code.
    * Hooked up the car's prebuilt control code to our interface system
    * Found textures for the car and implemented them.


* __The camera__

    I gave a lot of attention to the camera as it contributes a lot to making the core game fun to play as a human, and interesting to watch with an AI.
    * Made a stable camera that smoothly points in the direction of the velocity vector, instead of being fixed to the car's hull (March 17)
        * This adds a reversing camera for free.
    * Added dynamic camera angles:
        * the camera changes its position and FoV depending on the speed of the car. This helps make the car feel fast. (March 25, April 27)
        * the camera 'trucks' (filmmaking technical term!) sideways when the car drifts, for more dramatic angles and more satisfying drifting
    * Added camera shake when going fast (April 29)
 
* __Tracks:__
    * Forest Run (March 24)
        * The first fully-featured track with complex terrain, trees and grass.
    * Grand Loop (May 1)
        * A simple track optimised for the presentation.
    * Overhauled the terrain of level1 (April 9)
    
* __Ghost car__ (April 25)
    * Records the run of the car while in play mode by taking snapshots every n physics frames
    * Replays previous runs by smoothly interpolating between the snapshots every physics frame
    
* __Track waypoints__ (March 25) (with Matthew)
    * Implemented the system that manages the track waypoints and detects the car passing through them,.
    * I built the original system, which Matthew overhauled to its current state.
    
* __Nitro__ (April 7)
    * Keeps track of fuel that slowly regenerates
    * When used, applies a flat force propelling car forwards
    * I also made the sound that plays when it is used, but not the system that plays the sound

* __Stuck detection__ (April 9)
    * Detects if the car is immobile for a certain period and replaces it at the last visited waypoint.
 
* __Other small things__:
    * Added first skybox
    * Worked on control schemes and input
    * Repurposed the fuel meter to show NO_2 level instead
    * Customised UI textures to label the various meters (N0_2 and m/s)
    * And, of course, bug fixes
    
