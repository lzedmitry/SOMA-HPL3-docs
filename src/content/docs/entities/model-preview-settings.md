---
title: Model Preview Settings
description: "= Entity Preview/Animation Editor window ="
category: entities
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Entities/Model_Preview_Settings"
sourceRevision: 7137
sourceUpdated: "2026-07-30T21:56:11Z"
lastSynced: "2026-09-28T13:28:41Z"
sourceStatus: verified
generated: true
tags:
  - entities
---
= Entity Preview/Animation Editor window =

When you have your entity all set up with bodies, joints and such, it is time to test how it would look in the game. That's what the Entity Preview window is for. In this window you will be able to see how the entity would look ingame, meaning it will be physically simulated. In it you will also get to edit the entity's animations, if any. To start the preview, just press the "Toggle preview" button (the one with cogwheels) in lower toolbar.

The window behaves just like a regular viewport. You can move and orbit the camera around the model the same way. Added to this, you can use the mouse pointer to actually "pick" and drag physical objects in the scene.

**Animation controls** 

** **Animation''': With this control you can select the animation to play, if there is any available. When selected, it will be looped on and on.
** **Autoplay''': when this is checked, pressing the play button will not be needed when selecting an animation on the Animation selector.
** **Play button'''
** **Loop button'''
** **Step backward/forward button'''
** **Time display'''
** **Timeline'''
**Visualization controls**:

** **Ph ''' Toggles drawing of physical objects information. Bodies will be shown as wireframe objects, with a cross indicating their center of mass and joints will appear as green spheres.
** **Sk'''If a skeleton is present, it will be drawn draw it as red lines for bones and spheres for joints when this button is pressed.
** **BV ''' Toggles showing of Bounding Volume for the meshes on screen.
** **Fl ''' Will set the floor object to visible when pressed.
** **Am/Ma/Bk ''' Toggles Ambient, Main and Back lights on the scene respectively.
The buttons below the previous ones work as follows:

** **Edit Animations'''  When pressed, the Animation Editor pane will be shown, more on this later.
** **Exit Preview'''  When pressed, the preview window will be dismissed.
Buoyancy controls

** **Buoyancy''': Toggles buoyancy active, along with a plane representing a liquid surface.
** **B. Density''': Buoyancy density.
** **S. Height''': Height of the liquid surface.
** **B. A. viscosity''': Buoyancy angular viscosity.
** **B. L. viscosity''': Buoyancy linear viscosity.
Animation Editor pane

With this tool you will be able to add, delete and edit animations for the current entity. 

Animation related controls

** **Add new animation'''  this button will add an animation with empty parameters.
** **Hide visemes'''this button will toggle the showing of special animations known as "visemes" which are used for facial animation. 
** **Animation list'''  Every animation set up for the current entity will show up here (unless it is a viseme and Hide visemes is toggled)
** **Delete animation ''' this button will delete the animation that is currently selected on the Animation list
** **Name'''
** **File'''
** **Layer'''
** **Speed'''
** **TImeline''': The timeline for the animation editor will have different functionality, depending on which elements (events or transitions) are being edited at the moment.
''' Animation elements tab frame: 
'''* Event tab
**** **New**: this button will add a new event to the currently selected animation, at the current time position in the timeline. A marker will be added to the timeline, drag this marker along the timeline to modify the event's time parameter.
**** **Event list**: Shows the events that are set up for the current animation.
**** Delete: Deletes the currently selected event.
**** Name: name of the current event. 
**** Time: position in seconds in the animation when the event will be triggered.
**** Type: The type for the current event. There is an extra value that is used depending on what the type is, as follows.
***** PlaySound
>  The event will play the sound picked with the File control.
***** 
Step:
***** 
ScriptCallback:
***** 
Message: 

''' Transition Tab
'''* New: this button will add a new transition to the currently selected animation
'''* 
Transition list: Shows every transition defined for the current animation

.
'''* Delete: Deletes the currently selected transition.
'''* Name: name of the current transition. 
'''* PrevAnimation: lets you choose the previous animation for the transition (meaning the transition will be triggered when choosing to play the current animation while the previous is playing in the game) from a combo box. If "Any" is chosen, the transition will be played in any case.   
        * Min and Max time: time interval in the previous animation where triggering the transition is okay. These only work when a previous animation other than "Any" is chosen. The interval will be shown with draggable markers on the timeline as well.
'''* Transition: animation that will be played as a "bridge" between the previous and the currently selected (base) animation.
**** Play transition preview: toggle to enable preview of the transition.
**** Start time: for tweaking the min and max time on the previous animation, one can choose at which time position the transition is to start. Also has an associated draggable marker on the timeline.

Notes on the timeline workings: event markers will only be shown when the event tab is selected. The timeline will play transition previews and will show transition markers when a transition on the Transition tab is picked, otherwise the current animation will be played.

## Source & attribution

- Original Frictional Wiki page: [HPL3/Entities/Model Preview Settings](https://wiki.frictionalgames.com/page/HPL3/Entities/Model_Preview_Settings)
- Revision: `7137`
- Source update: `2026-07-30T21:56:11Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).
