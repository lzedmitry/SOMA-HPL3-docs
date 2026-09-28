---
title: PathNode
description: "Helper Function: helperai.hps"
category: areas
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Areas/PathNode_Area"
sourceRevision: 6754
sourceUpdated: "2024-02-01T14:58:31Z"
lastSynced: "2026-09-28T13:28:41Z"
sourceStatus: verified
generated: true
tags:
  - areas
---
## Overview
Helper Function: [helper_ai.hps](https://wiki.frictionalgames.com/page/Ai_Helper)

The PathNode Area is an area that acts as a point entity that generates a navigable path for agents to use for pathfinding. Each area much be assigned to each enemy entity using the function `Pathfinder_Track_Add()` and the agent must be started on the path using the function `Pathfinder_Track_Start()`. These Functions require the helper_ai.hps script to be included in the map file. Not all agents can be used with the pathnode system as some are designed to be used in specific situations.

## Properties
The PathNode Area takes no properties

## Script Example
A simple for loop can be used to add `n` path nodes to an agents pathfinding.

```
for(int i = 1; i <= n; i++)
{
	Pathfinder_Track_Add("_agent_", "PathNodeArea_" + n, 0.0f, 0.5f, "", false);
}
```

where `"_agent_"` is the name of the agent to assign to the node.

To start the agent on the path node network you can call the `Pathfinder_Track_Start()` function.

```
Pathfinder_Track_Start("_agent_", true, 1.0f, "");
```

## Source & attribution

- Original Frictional Wiki page: [HPL3/Areas/PathNode Area](https://wiki.frictionalgames.com/page/HPL3/Areas/PathNode_Area)
- Revision: `6754`
- Source update: `2024-02-01T14:58:31Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).
