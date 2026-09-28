---
title: Level Editor Color Dialog
description: "= Color Picker window = This window serves as a means for selecting colors. It allows to work in both HSB and RGB color spaces."
category: level-editor
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Level_Design/Level_Editor_Color_Dialog"
sourceRevision: 7105
sourceUpdated: "2026-07-30T10:01:58Z"
lastSynced: "2026-09-28T13:28:41Z"
sourceStatus: verified
generated: true
tags:
  - level-editor
---
= Color Picker window =
This window serves as a means for selecting colors. It allows to work in both HSB and RGB color spaces.

> **Figure (original Wiki file, not inlined):** [color_picker.png](https://wiki.frictionalgames.com/page/File:color_picker.png)

 
## General inputs
- **Current/previous color preview**: These frames show the current color and the initial one.
- **Picked color history**: When a color is picked, it will make it to this list. Here will be listed up to the last ten picked colors. Clicking on any of them will make the clicked color as current.
- **Graphical inputs**: these offer a means of visually picking the desired color. There are markers for each to show where the currently defined color lies.
  1. **Color bar**: this input will show the range of values for the color dimension that is chosen out of the HSB and RGB sets via the checkboxes next to each numeric input.
  1. **Color box**: this input show the 2D range of the 2 remaining dimensions in the chosen set using the selected value in the color bar. So for example if G is checked, the color bar will show the full range for Green, and the color box will show the full ranges for Red and Blue. 
  1. **Alpha bar**: this input allows for selecting an alpha value. Note that alpha will not be used unless the checkbox next to the alpha numeric input is checked.
- **Numeric inputs**: offer a fine control over the resulting color. Keep in mind that modifying HSB values will affect the RGB values displayed and vice-versa.
** **H''': Value for Hue
** **S''': Value for Saturation
** **B''': Value for Brightness
** **R''': Controls the amount of red in the blend.
** **G''': Controls the amount of green in the blend.
** **B''': Controls the amount of blue in the blend.
** **A''': Controls the alpha value of the final color.
** **Hex''': will show the hexadecimal code for the current color. Note that hand editing this code will modify the current color.
** **Vec''': shows the current color in a scripting friendly format.

## Source & attribution

- Original Frictional Wiki page: [HPL3/Level Design/Level Editor Color Dialog](https://wiki.frictionalgames.com/page/HPL3/Level_Design/Level_Editor_Color_Dialog)
- Revision: `7105`
- Source update: `2026-07-30T10:01:58Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).
