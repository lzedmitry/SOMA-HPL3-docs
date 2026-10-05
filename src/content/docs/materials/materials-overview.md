---
title: Materials Overview
description: "A material is a .mat text file that defines a two-dimensional surface. It contains all of the information needed for HPL3 to simulate the surface visually, aurally, and physically."
category: materials
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Materials/Materials_Overview"
sourceRevision: 5338
sourceUpdated: "2020-09-09T07:49:48Z"
lastSynced: "2026-10-05T14:11:59Z"
sourceStatus: verified
generated: true
tags:
  - materials
---
> **Figure (original Wiki file, not inlined):** [222x222px](https://wiki.frictionalgames.com/page/File:Hpl3-material-example.png)

A **material** is a `.mat` text file that defines a two-dimensional surface. It contains all of the information needed for HPL3 to simulate the surface visually, aurally, and physically.  

The main attributes of a material are:

*Material Type
*[Corresponding Physics Material](https://wiki.frictionalgames.com/page/HPL3/Materials/Physics_Material)
*[Texture Units](https://wiki.frictionalgames.com/page/HPL3/Materials/Texture_Units)
*[Material Variables](/materials/material-specific-variables/)

HPL3 Material are created and edited using the Material Editor.

:::tip[Tip]
`.mat` files can be opened directly with the material editor application, if you set it as the default app in your computer's settings.
:::

## .mat file Example
The basic structure of a .mat file is as follows: 

```
<Material>
    <Main BlendMode="Add" DepthTest="true" ForceFullScaleTextures="true" PhysicsMaterial="Bed" Type="soliddiffuse" UVSubDivs="1 1" UseAlpha="false" />
    <TextureUnits>
        <Diffuse AnimFrameTime="1" AnimMode="None" AnimStartTime="0" Compress="false" File="textures/detail/algae_detail.dds" MipMaps="true" Type="2D" Wrap="Repeat" />
    </TextureUnits>
    <SpecificVariables>
        <Var Name="HeightMapScale" Value="0.05" />
        <Var Name="HeightMapBias" Value="0" />
        <Var Name="IlluminationBrightness" Value="1" />
        <Var Name="FrenselBias" Value="0.2" />
        <Var Name="FrenselPow" Value="8" />
        <Var Name="AlphaDissolveFilter" Value="false" />
        <Var Name="DissolveLayer" Value="0" />
        <Var Name="DetailUvMul" Value="4 4" />
        <Var Name="DetailWeight_Diffuse" Value="1" />
        <Var Name="DetailWeight_Specular" Value="1" />
        <Var Name="DetailWeight_Normal" Value="1" />
        <Var Name="DetailFadeStart" Value="5" />
        <Var Name="DetailFadeEnd" Value="10" />
        <Var Name="SwayActive" Value="false" />
        <Var Name="SwayForceFieldAffected" Value="true" />
        <Var Name="SwayFreq" Value="1" />
        <Var Name="SwayAmplitude" Value="0.1" />
        <Var Name="SwaySpeed" Value="1" />
        <Var Name="SwayOctaveMuls" Value="0.125 0.25 1" />
        <Var Name="SwayForceFieldMul" Value="0.3" />
        <Var Name="SwayForceFieldMax" Value="0.6" />
        <Var Name="SwayYFreqMul" Value="0" />
        <Var Name="SwaySingleDir" Value="false" />
        <Var Name="SwaySingleDirVector" Value="0 0 1" />
        <Var Name="SwaySingleSampleVector" Value="1 0 0" />
        <Var Name="LiquidTrickleColor" Value="0 0 0 1" />
        <Var Name="LiquidTrickleSpecular" Value="0 0 0 0" />
        <Var Name="LiquidTrickleLoopFade" Value="false" />
        <Var Name="LiquidTrickleFadeSpeed" Value="0.5 0.5" />
        <Var Name="LiquidTrickleEdgeSize" Value="0.5" />
        <Var Name="LiquidTrickleDryness" Value="0.5" />
        <Var Name="LiquidTrickleBlendMode" Value="Alpha" />
    </SpecificVariables>
</Material>
```

*`Main` describe general material parameters. More on that in [Material Editor General](https://wiki.frictionalgames.com/page/HPL3/Materials/Materials_Editor_General) and in the different material types section in the main Materials category.
*`TextureUnits` describe different shaders maps the material may use. More on that in [Texture Units](https://wiki.frictionalgames.com/page/HPL3/Materials/Texture_Units).
*`SpecificVariables` describe further material configuration and unique variables. They vary from different material types. More on that in [Material Specific Variables](/materials/material-specific-variables/) and in the different material types section in the main Materials category.
*

## Finding Materials
`.mat` files can be found in several locations:

*Inside a sub-folder under the `/textures` folder of the game.
*Inside a sub-folder under the `/static_objects` folder of the game.
*Inside a sub folder under the `/entities` folder of the game.

## Source & attribution

- Original Frictional Wiki page: [HPL3/Materials/Materials Overview](https://wiki.frictionalgames.com/page/HPL3/Materials/Materials_Overview)
- Revision: `5338`
- Source update: `2020-09-09T07:49:48Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).
