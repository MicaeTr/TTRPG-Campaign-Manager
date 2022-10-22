# TTRPG Campaign Manager Planning Document 

### Why this project?

    This project will create an all in one campaign management tool that is completely free for all users.

### Goal of this project: 
    The goal is to create an all in one Campaign Management Tool for GMs (Game Masters). This includes features for campaign notes, location specific notes, maps, combat, player status, and the campaigns themselves. Users will be able to download the tool, plan for sessions, run battles with their players, and update information they have regarding players and the campaign itself. Supporting different TTRPG systems and allowing GMs to program their own systems will be part of the management tool as well as support of non-official content and UI customization.

### Planning for this project: 
    The project requires intensive planning due to the magnitude of its goals. The document herein formalizes the action plan and will be updated with changes and new developments.

### Design
    The design of the project will determine its success. The design needs to allow certain aspects, 
    such as map usage and campaign notes, to be used with any TTRPG system. It should also allow for TTRPG system specific 
    rules for items such as combat. The design needs to account for the creation, storage, and retention of campaign files as well as UI customization.

    In order to achieve the goals of the project, it must be loosely coupled and be as modular as possible, with different systems stored separately. This system also needs to allow for non-official content to be added onto the official rules set. The system will be modular with the UI automatically adding specific elements specific to a system. 

    The system will keep information separate by using a Model-View-Controller design. 
    
    The Model will be determined during the set up of a campaign and will consist of a Main TTRPG system to which non-official and common materials will be added. Common materials refer to features such as maps, notes, and location specific notes that can be used by any system. 

    The View will simply show the user the UI while the Controller allows the user to manipulate data in the model. 

### Development Timeline

    The project will be developed in phases and from the top down. The development timeline is to create a minimum viable product using Dungeons and Dragons 5E in the following four phases:
    
    -Phase 1: Implementation of the combat mechanics and official materials regarding monsters.

    -Phase 2: Implementation of Campaign Note Management Features including a document editor so documents can be created, edited, and saved within the system.

    - Phase 3: Implementation of Map features including uploading of a map and the saving of a waypoint where players are located.

    - Phase 4: Addition of UI features to the system.

Once the minimum viable product is complete, more advanced features will be considered and added.