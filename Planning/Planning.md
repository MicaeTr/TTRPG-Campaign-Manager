# TTRPG Campaign Manager Planning Document 

### Why this project?
    I wish to create this project as I would like to have an all in one campaign management tool that I, and others, can use for free. 

### Goal of this project: 
    The goal of this project is to create an all in one Campaign Management Tool for GMs (Game Masters). This includes features for campaign notes, location specific notes, maps, combat, player status, and the campaigns themselves. I want the user to be able to download this tool, be able to plan for sessions, run battle with their players, and update any information that they have regarding players and regarding the campaign itself. I want to be able to support different TTRPG systems and allow GMs to program their own systems into this manager. I want to be able to support non-official content and UI customization.

### Planning for this project: 
    This project requires intensive planning due to the magnitude of its goals. This document is that plan. This document will be 
    updated when the plan changes and develops. 

### Design
    The design of this project is perhaps the most important part of the project as this will determine it's success. The goal of 
    the design needs to allow certain aspects, such as map usage and campaign notes, to be used with any TTRPG system, but also allow for TTRPG system specific rules for things such as combat.

    In order to achieve the goals of this project, it must be loosely coupled, and it must be as modular as possible, with different systems stored seperately. This system also needs to allow for non-official content to be added onto the official rules set. 

    This design needs to account for the creation, storage, and retention of campaign files. This design needs to account for UI customization.

    This system will be designed to be modular, with the UI automatically adding elements specific to a system. 

    This system will keep information seperate by using a Model-View-Controller design. 
    
    The Model will be determined during the set up of a campaign and will consist of a Main TTRPG system to which non-official material can be added and Common materials. Common materials refer to things such as maps, notes, and location specific notes that can be used by any system. 

    The View will simply show the user the UI while the Controller allows the user to manipulate data in the model. 

### Development Timeline
    This project will be developed in phases and will generally be developed from the top down (hence this document which plans out the project). The goal of the current development timeline is to create a minimum viable product using Dungeons & Dragons 5E.
    
    -The first phase will be implementing the combat mechanics and official materials regarding monsters.

    -The 2nd phase will be implementing Campaign Note Management Features. This will include a small document editor so that documents can be created, edited, and saved within the system 

    - The 3rd phase will be implementing Map features. This will include the upload of a map and the saving of a waypoint where the players are currently located. 

    - The 4th phase will be adding UI features to this system.

Once the miimum viable product is complete, more advanced features will be implemented.