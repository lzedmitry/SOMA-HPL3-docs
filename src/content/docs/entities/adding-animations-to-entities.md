---
title: Adding Animations to Entities
description: "With this tool you will be able to add, delete and edit animations for the current entity."
category: entities
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Entities/Adding_Animations_to_Entities"
sourceRevision: 7138
sourceUpdated: "2026-07-30T21:57:07Z"
lastSynced: "2026-09-28T13:28:41Z"
sourceStatus: verified
generated: true
tags:
  - entities
---
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

- Original Frictional Wiki page: [HPL3/Entities/Adding Animations to Entities](https://wiki.frictionalgames.com/page/HPL3/Entities/Adding_Animations_to_Entities)
- Revision: `7138`
- Source update: `2026-07-30T21:57:07Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).
