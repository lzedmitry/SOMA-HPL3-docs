---
title: Chapter 2 - Structure of a Script
description: "A bit wordy, perhaps, but it all boils down to the following categories, each of which you will learn about in a particular lesson:"
category: scripting
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Scripting/AngelScript_Fundamentals/Chapter_2_-_Structure_of_a_Script"
sourceRevision: 4618
sourceUpdated: "2020-08-16T10:19:16Z"
lastSynced: "2026-08-28T18:40:04Z"
sourceStatus: verified
generated: true
tags:
  - scripting
---
|   |   |
| --- | --- |

A bit wordy, perhaps, but it all boils down to the following categories, each of which you will learn about in a particular lesson:

*Includes (Chapter 5)
*Class Declaration (Chapter 8)
*Functions (Chapter 6)
*Types and Variables (Chapter 3)
*Callback Functions (Appendix 2)
*Comments

Most of these aspects are explained in later lessons. There is one that you can learn about now, however: comments.

## Commenting
Most of the things that go into a script is part of the program's execution - you want it to do something here, then do something there, then do something to those two somethings over there. Sometimes, however, you just want to write a reminder of what some code does so that you don't have to go through it all and figure it out later. That's where comments come in. Anything that has been marked as a comment is ignored by the program, so you can type in whatever you want without worrying that it will screw up the program.

There are two types of comments in AngelScript - inline comments and block comments:

```
    // This is an inline comment

    /* 
    This is a block comment
    */
```

*Inline comments are just for a single line. Anything after the comment marker `//` becomes a comment, but on the next line, it's back to business as usual.
*Block comments are for multiple lines. A block comment is marked as everything between the starting marker `/*` and the ending marker `*/`. This can span many lines, and can even mark your entire program as a comment if you aren't careful.

## Hello World
As per tradition, every introductory programming course needs a “Hello World” program, and this tutorial is no exception. In your map’s script, find the section of the code that contains the following:

```
    ////////////////////////////
    // Run when entering map
    void OnEnter()
    {

    }
```

Inside those curly brackets, add `cLux_AddDebugMessage(“Hello World!”);`. Don’t worry what it means just yet. When you’re done, the above code snippet should now look like this:

```
    ////////////////////////////
    // Run when entering map
    void OnEnter()
    {
        cLux_AddDebugMessage("Hello World!");
    }
```

Go ahead and save your script, if you haven’t done that already.

Now it’s time to start up the game in mod development mode. To do this, there’s a file in your game installation directory which launches the dev mode.

*For SOMA, the file is called `SomaDev.bat`
*For Amnesia: Rebirth, the file is called `RebirthDev.bat`

When you open this file, it starts the game in developer mode. For the first little bit, the game will be loading, but once you hear sounds start to play, hit the F1 button. This brings up the developer panel, and on it contains a lot of commands and tools for testing and proofing your map.

For now, scroll down until you find the “Load Map” button. Click that button, then navigate to where you saved your map. Open your map from there (it will be the “.hpm” file that you see). Once you do, you should get basically a black screen with a handful of text around the edges. In the lower left corner, you should see the text “Hello World!”.

:::note[Note]
If you don’t see the text, make sure the developer panel is hidden by pressing F1 again. This is because the game is effectively frozen while the panel is visible by default, so the script may not appear right away if the panel is visible. If you still do not see the text, press F5, which reloads the map and causes it to become visible again.
:::

If all went well, then congratulations. You just created your first SOMA mod. It may not be very shiny, but like I said in Lesson 0, we all have to start somewhere.

So let’s look at what we just did in pieces:

```
    cLux_AddDebugMessage(“Hello World!”);
```

1. We used the code `cLux_AddDebugMessage` followed by an opening and (eventually) closing parentheses. This is a function call, which you will learn more about in Lesson 6. For now, just know that this function’s job is to print text onto the screen.
1. Within the parentheses is some text within quotation marks, `“Hello World!”`. This is what is known as a “string literal”. You’ll learn about them and other types in next chapter. The important part to note here is that it is the text that actually appeared in the game itself.
1. Finally, after the closing parenthesis, there is a lonely little semicolon. That semicolon marks the end of a line of code. Do not forget this: every line of code that isn’t a class or function declaration (more on them later) needs a semicolon at the end of it. If you do not put a semicolon at the end of a line of code, HPL3 will complain about it and refuse to run your script.

No programmer is immune from that mistake, no matter how many decades they’ve been a guru in their field. As long as you remember your semicolons, then when the errors happen, you know what to check first.

HPL3/Scripting/AngelScript Fundamentals/Chapter 1 - Introduction|Chapter 1 - Introduction|HPL3/Scripting/AngelScript Fundamentals|AngelScript Fundamentals|HPL3/Scripting/AngelScript Fundamentals/Chapter 3 - Variables and Types|Chapter 3 - Variables and Types

## Source & attribution

- Original Frictional Wiki page: [HPL3/Scripting/AngelScript Fundamentals/Chapter 2 - Structure of a Script](https://wiki.frictionalgames.com/page/HPL3/Scripting/AngelScript_Fundamentals/Chapter_2_-_Structure_of_a_Script)
- Revision: `4618`
- Source update: `2020-08-16T10:19:16Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).
