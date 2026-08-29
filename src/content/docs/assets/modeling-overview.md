---
title: Modeling Overview
description: "This tutorial was written for anybody working on the project and details the outlines used when creating the game. Much of this is suggestions, like specular should have half width and height, and so on. Still it should"
category: assets
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Modeling/Modeling_Overview"
sourceRevision: 7126
sourceUpdated: "2026-07-30T21:11:21Z"
lastSynced: "2026-08-28T18:40:04Z"
sourceStatus: verified
generated: true
tags:
  - assets
---
### Introduction
This tutorial was written for anybody working on the project and details the outlines used when creating the game. Much of this is suggestions, like specular should have half width and height, and so on. Still it should be pretty valuable for anybody wanting to do their own models and all of the guidelines are meant to make life easier and increase in-game performance.

### Creation of Graphics
The following be sort of a set by set guideline of the process to create objects for the game. Hopefully this will give a clear view of the steps that needs to be taken when creating graphics.

**Modeling** 

This is preferably done in Maya and the latest Collada plug-in shall be used. This has been included in the “plugin” folder.

Make sure that the unit type is set to meters!

The object shall be positioned in the file so that the bottom of the object is at the center of the screen.

When texturing the objects, make sure that the diffuse texture is what is set as texture for all sub meshes.

**Material** 

Each material will require one or more the following textures:

**Diffuse**  
Size: Normal.  
File format: dds, dxt5.  
Suffix: None.  
This is simply the color and is needed for pretty much all materials.

**Normal map**   
Size: Normal.  
File format: dds, 3dc.   
Suffix: “nrm”.  
The normal map for the material and uses the standard format rgb = xyz and is in tangent space. Note that this needs to be converted to a format of XY only though (3dc)!

**Specular map**  

Size: Half of diffuse  
File format: dds, dxt5.  
Suffix: “spec”.  
The specular map handles the specular intensity and power for each pixel. The intensity uses the R,G and B channel and the power in the Alpha channel.
Intensity sets the amount of specularity (for each color channel) applied to a pixel, the higher value of the channel, the higher intensity.
Power sets the sharpness of the specular highlight, a low value give a dull and diffuse look, while a high value give a wet/shiny look.

**Alpha**   
Size: Normal  
File format: tga, single channel (greyscale).  
Suffix: “alpha”.  
Sets the alpha for each texture and for any lit surface this is a simply 0 or 1 decision per pixel since a lit pixel can never be half transparent, only fully visible or invisible.

**Height map**   
Size: Half of diffuse  
File format: tga, single channel (greyscale).  
Suffix: “height”.  
Height map is more like a depth map actually. White = largest depth, Black = no depth and this is important to remember when creating it.

**Illumination map**   
Size: Half of diffuse  
File format: dds, dxt1.  
Suffix: “illum”.  
This map will be added additively on top of the model when rendering and will not be affected by lighting. It is useful for creating glowing surfaces such as lightbulb, ember, etc.

With size means the size of texture width and height. So if diffuse is 512×512 in size, then a map with half of the size of diffuse will be 256×256. Normal simply means that it has the same size of the diffuse texture. Also note that the size of map might be specified otherwise in the description of an object, and if so the specified size shall be used.

All of the textures in a material (and the material itself!) must be named according the model which uses it. An example of naming is as follows:

The model has the name of “ball01” and its material has a diffuse, normal map and specular map. The textures will then be named like this:

”ball01.dds”, the diffuse.  
“ball01_nrm.dds”, the normal map.
“ball01_spec.dds”, the specular map.  

If the model has uses several materials then add some extra name after the name of the file when settings up the textures. Here is an example:

The model has the name “frontdoor01” and have two submeshes: “frame” and “door”. Each of these submeshes have its own texture and therefore also material. The base name for each submesh material will be: “frontdoor01_frame” and “frontdoor01_door” respectively. This means that the textures will have the names:

For frame:  
“frontdoor01_frame.dds”, the diffuse.  
“frontdoor01_frame_nrm.dds”, the normal map.  
“frontdoor01_frame_spec.dds”, the specular map  

For door:  
“frontdoor01_door.dds”, the diffuse.  
“frontdoor01_door_nrm.dds”, the normal map.  
“frontdoor01_door_spec.dds”, the specular map.  

### Testing and setting up model
First create a folder in the “models” directory in “data/viewer” named exactly like the name of the work batch (ie “Furniture Batch9”). For each model in the work batch, create a folder named exactly like the model (“ball01.dae” model file should be in a “ball01” folder) and put all the files for the model in there (even the Photoshop files). It is best if this is done when starting to create the model so a lot of file copy can be skipped! For example, the model “shelf” in the work batch “Furniture Batch9” should have the current local path for all files:

“models/Furniture Batch9/shelf/”

With all the files in place start modelview.exe and then press “Load Model” and choose the exported dae file. If all goes as it should the model viewer will now create a mat file in directory where the model and all of the textures are put. If this does not work for some reason, then it is probably because 1) there is a bad extension a texture files or 2) the texture set to the model in Maya is not the diffuse file.

Now the model can be viewed in engine! Hold down the left mouse button and move the mouse to rotate the view. To zoom either use the mouse scroll wheel or hold the middle mouse button while moving

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Modeling/Modeling Overview](https://wiki.frictionalgames.com/page/HPL3/SOMA/Modeling/Modeling_Overview)
- Revision: `7126`
- Source update: `2026-07-30T21:11:21Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).
