---
title: Color Grading
description: "Color grading is a way to map the color of a pixel to another color. This can be used to change the brightness, contrast, hue, saturation, … of a whole image."
category: generated
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Color_Grading"
sourceRevision: 6401
sourceUpdated: "2023-03-31T08:54:06Z"
lastSynced: "2026-10-05T14:11:59Z"
sourceStatus: verified
generated: true
tags:
  - generated
sidebar:
  hidden: true
---
:::caution[SOURCE STATUS: WIP]
This source page is marked as undergoing editing on the Frictional Wiki.
:::

> **Figure (original Wiki file, not inlined):** [Color Grading example](https://wiki.frictionalgames.com/page/File:Grading.jpg)

Color grading is a way to map the color of a pixel to another color. This can be used to change the brightness, contrast, hue, saturation, … of a whole image.  

It is possible to smoothly fade between two different grading templates.  

It uses a small 3D texture with a color as input and another color as output.

## Creation Guide
### Requirements
- Photoshop (CS5 or later recommended)
- [NVIDIA Texture Tools for Adobe Photoshop v8.55](https://developer.nvidia.com/gameworksdownload#?dn=texture-tools-for-adobe-photoshop-8-55) - Download the correct version for your system (probably 64-bit)
  - The modern Nvidia Texture Tool should also work using equivalent settings.

### Setup
1. Take a screenshot of the game with color grading disabled
1. Open the screenshot in Photoshop
1. Drag and drop the default grading texture on the canvas (found at **/core/textures/grading_default.dds**)
1. Place the color strip anywhere in the image
1. Flatten the image to merge all the layers
1. Select "**Image > Mode > 8 Bits/Channel**" in the top menu 
*Note: FG documentation originally listed 16 Bits/Channel, however this seemed to result in incorrect color grading results.*

### Adjustments
- Use any of the options in "**Image > Adjustments**"
- These can be used to change the brightness, saturation, contrast and so on
- Any changes you see on the image in Photoshop will carry over to the game

> **Figure (original Wiki file, not inlined):** [adjustments.jpg](https://wiki.frictionalgames.com/page/File:adjustments.jpg)

### Layers
It is also possible to use the any of the layer blend modes.   

There are two kinds of layers allowed:

- Solid color
- Dupilcate of the first layer

It is possible to duplicate the first layer and make adjustments to it and then blend it.   

The use of Layer Masks is allowed as long as they are generated from the image and not hand painted.

> **Figure (original Wiki file, not inlined):** [layers.jpg](https://wiki.frictionalgames.com/page/File:layers.jpg)

### Saving
> **Figure (original Wiki file, not inlined):** [Example crop](https://wiki.frictionalgames.com/page/File:crop.jpg)

1. Crop the color strip from the canvas, make sure the resulting image is 256×16 px
1. Select "**Save a Copy...**" and set the format as "**D3D/DDS (*.DDS)**'" and save it in the folder "**/textures/colorgrading/**"
1. In the DDS format settings select "**8.8.8.8 ARGB 32 bit | unsigned**", "**Volume Texture**", "**No MIP maps**"

> **Figure (original Wiki file, not inlined):** [DDS Format Fixed.png](https://wiki.frictionalgames.com/page/File:DDS_Format_Fixed.png)

## Level Usage
You can apply your color grading texture either in the [Level Settings](/level-editor/level-settings/#colorgrading) or via the level script.
TODO: Link to/explain color grading scripts.|width=25%

## Source & attribution

- Original Frictional Wiki page: [HPL3/Color Grading](https://wiki.frictionalgames.com/page/HPL3/Color_Grading)
- Revision: `6401`
- Source update: `2023-03-31T08:54:06Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).
