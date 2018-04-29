Group 6 Practical Report
========================

Our project's goal is to create a website that allows the ranking and development of AIs whose task it is to drive a car around a track. It presents a leaderboard, encouraging competitive AI development. Individual AIs can be viewed and improved by anyone. The track provides a feature-rich environment, with many inputs the AIs can use to navigate, providing many optimization opportunities and compromises. Our project also provides data visualizations for those wishing to analyse the performance of the AIs.

Project Functionality and Features
----------------------------------

\begin{figure}[h]
    \centering
    \includegraphics[scale=0.5]{flow.pdf}
    \caption{User Interaction Flow}
    \label{fig:uif}
\end{figure}

Referring to figure \ref{fig:uif}, we shall examine the functionality of each page.

### Leaderboard

\begin{center}
\includegraphics[width=400px]{leaderboard.png}
\end{center}

The leaderboard displays each script, and all the metrics gathered from its run on the selected track. The metrics are selected to show both the speed and precision of an AI, but also its efficiency in using its resources. The leaderboard can be sorted based on any metric, and has pagination.

### View Script

\begin{center}
\includegraphics[width=400px]{view_script.png}
\end{center}

This page allows users to view the code used for any particular AI. It shows how the AI is related to other scripts by displaying its parent and children, and shows the AIs scores on each track. It also allows users to run the script or fork it, allowing the users to create new AIs based on existing ones. The run button comes with an additional option: to show a replay of another AI while the current AI is running. This allows for comparison between AIs driving styles, which cannot be done with simple metrics.

### Fork / New Script

\begin{center}
\includegraphics[width=400px]{fork_script.png}
\end{center}

Both the fork script button, found on each AIs view page, and the new script button, found on the navigation bar, lead to this page, the difference being that fork copies an existing AIs code. This page provides a code editor, which supports syntax highlighting and error detection, as well as a short documentation section. It allows changing language, the choices being Python 3, JavaScript and Lua. More languages can be added, should the need arise.

### Run Script

\begin{center}
\includegraphics[width=400px]{run_script.png}
\end{center}

This page handles the execution of scripts. It embeds the game, which allows the choice between several tracks. While running, the game displays the car's speed, sensor readings, current time, remaining nitro and a text field that is controlled by the script, allowing for live debugging. All errors in the script are caught and displayed to the user, with a traceback if available. Once the car finished the track, the page presents the user with a button to submit the new score if it is better than the currently stored score.

### Graphs

\begin{center}
\includegraphics[width=400px]{graphs.png}
\end{center}

This page allows users to analyse the data gathered from scripts. They are animated and interactive, and support zooming and dragging. The page supports the following graph modes:

 - Generation line:

   This mode displays a user-chosen metric on the y-axis, with the generation on the x-axis. This mode can be used to see how a particular family of scripts have improved over time in relation to certain metrics.

 - Scatter:

   This mode displays a scatter graph of two user chosen metrics, allowing the correlation of certain metrics to be analysed.

 - Tree:

   This mode displays the scripts in a tree form, with the nodes color-coded based on a user-chosen metric. It allows exploration of a family tree in an easier format than the other graphs.

### Human mode

\begin{center}
\includegraphics[width=400px]{human_mode.png}
\end{center}

The best human time is listed on the leaderboard, so show an upper limit on the best achievable score and allow comparison between human and AI drivers. On the humans view page is an option to play the game, which functions the same way as the run script page, except the car is controlled using the keyboard. This mode has not been included on the diagrams for clarity.

\newpage

Project Implementation
----------------------

\begin{figure}[h]
    \centering
    \includegraphics[scale=0.5]{structure.pdf}
    \caption{Internal Component Structure}
    \label{fig:ics}
\end{figure}

The overall structure of the project is shown in figure \ref{fig:ics}. Details on each component follows.

### Server

The server is build using Django and Python 3.6. It serves the pages and static files such as the game. It uses a local SQLite3 database for storage. The client side uses the following libraries:

 - Bootstrap - for styling
 - jQuery - for general DOM element manipulation
 - FontAwesome - for icons
 - Ace - for code editor with syntax highlighting
 - Highlight.js - for highlighting on script view pages
 - jQuery tablesorter plugin - for leaderboard sorting
 - D3.js - for interactive graphs
 - Brython - Python 3 implementation in JavaScript
 - Fengari - Lua implementation in JavaScript
 - inspect.lua, json.lua - utility Lua libraries

#### Runtime Control, Scripting Engines and the Unity bridge

The runtime communications is handled by some JavaScript code. The scripting runtime is executed in a web worker, and communicates page to the main page using JSON. The communication is asynchronous and happens on a separate thread from the game.

Each scripting engine has an adapter, which allows all scripting languages to be handled the same by the runtime controller. Each adapter defines an interface allowing the runtime controller to execute the following actions: `begin`, which loads the runtime; `load`, which loads the script; `verify`, which checks the script for certain errors before the game is loaded; and `new_data`, which provides updated sensor data for the script to use. The adapter send back the following messages: `ready`, `loaded`, `verified`, which show the completion of the `begin`, `load` and `verify` operations; and `cmds`, which provides an updated set of commands from the script for the game.

The Unity bridge is a set of functions which is globally accessible, allowing Unity to communicate with the page via a JavaScript plugin.

### Game

The game is constructed in much the same way as any other Unity game. It contains the following major components, which are implemented as prefabs:

 - The game manager - This object loads the correct interface based on the environment it is running in. There are two interfaces: `JSInterface`, which provides commands from a script; and `HumanInterface`, which provides commands based on the keyboard state. Together these interfaces abstract the controller of the car, allowing the rest of the code to behave the same regardless of the environment.
 - The track controller - This object notified the car when it has passed though a waypoint, as well as providing the number of laps the car must complete.
 - The car control - This object translates commands into the physical changes required, as well as gathering sensor data. It keeps track of metrics such as fuel usage, providing them to the game manager once it has finished its laps.
 - The UI - This object is provided the same data as scrips are, and displays this data in a human-friendly way.

Unimplemented and Rejected Features
-----------------------------------

 - Branching tracks

   This was rejected due to the extra complexity it would introduce in both the game, the script sensors and the scripts themselves.

 - Track collectables

   This feature would introduce object on the tracks, such as extra nitro which could be used to improve performance. It was not implemented due to time constraints
