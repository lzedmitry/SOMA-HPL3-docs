---
title: Chapter 5 - Statements and Flow Control
description: "In the last lesson, you learned that expressions are lines of code where one or more values are manipulated or assigned to variables through the use of operators. There are other lines of code that do not use operators ("
category: scripting
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Scripting/AngelScript_Fundamentals/Chapter_5_-_Statements_and_Flow_Control"
sourceRevision: 4574
sourceUpdated: "2020-08-15T20:14:03Z"
lastSynced: "2026-08-28T18:40:04Z"
sourceStatus: verified
generated: true
tags:
  - scripting
---
In the last lesson, you learned that expressions are lines of code where one or more values are manipulated or assigned to variables through the use of operators. There are other lines of code that do not use operators (or at least uses them in a different way). These lines of code are called *statements*.

The main use of statements in code is to control how a program moves from one line of code to the next. By default, when you run a program, it starts at the first line of code, moves down one line at a time, then stops once it passes the last line. This is well and good, but it's a bit limited, isn't it? What if you wanted to do part or all of your program multiple times? What if you wanted to skip part of it under certain conditions? These concepts are made possible in programming due to special statements that perform *flow control*.

## Conditions
It is said that when the concept of conditionals enters programming, that is what truly separates a calculator from a computer. Being able to execute some code and skip other code based on a condition is incredibly powerful, and many programs wouldn't have been made possible without it.

### If
The first step into conditional programming is the `if` keyword. When using `if`, you specify a condition in the form of a boolean value. If the value is true, the code under the `if` gets executed. If the value is false, then it doesn't.

```
    int i = 0;
    
    if (true)
    {
        i = 1; // the boolean value is true, so this code executes
    }
    
    if (false)
    {
        i = 2; // the boolean value is false, so this code gets skipped
    }
    
    // at the end of this script, i is 1
```

The structure of an `if` statement is a bit different from what you've been used to up to this point, so lets break it down.

First, you have the `if` keyword. Nothing groundbreaking quite yet. Next, you have a set of parentheses. These parentheses contain the condition that the `if` uses to decide whether or not to execute its code. (The parentheses are not optional, so don't forget to type them out.)

Within the parentheses, you have the boolean condition. In this case, it just happens to be a literal boolean value (`true` in the first case, and `false` in the second).

Then you have a set of curly braces that take up several lines of code. When this happens, the area inside the curly braces is called a *code block*. Code blocks are used to say "this code belongs to a statement". In this case, this is the code block that belongs to the `if` statement - it is what may or may not execute depending on the condition.

In this example, we used literal boolean values as the condition. This is pretty boring, though - the first `if` statement has `true` so it will always run and there's no point in having an `if` at all. The second `if` statement has `false`, so it will *never* run and there's no point in having any of the code inside that block. To make `if` statements a tad more useful, you can use variables as the condition as well:

```
    bool b = true;
    
    if (b)
    {
        // Some code that runs if the value in <code>b</code> is true
    }
```

or even boolean expressions that utilize the comparison operators:

```
    int a = 5;
    int b = 2;
    
    if (a > b)
    {
        // Some code that runs if the value in <code>a</code> is greater than the value in <code>b</code>
    }
```

You can also chain together multiple conditions using the logic operators:

```
    int a = 2;
    int b = 5;
    int c = 9;
    
    if (a < b && b < c)
    {
        // Some code that runs if the value in <code>a</code> is less than the value in <code>b</code> AND the value in <code>b</code> is less than the value in <code>c</code>
    }
```

As you can see, you can get some pretty imaginative conditions going.

### Else
In addition to `if`, there exists an `else` keyword. This keyword is a companion to `if`, and it will run a block of code if the condition within the `if` statement is false:

```
    int i = 5;
    
    if (i == 2)
    {
        i = 3; // Doesn't run since <code>i</code> is not equal to 2
    }
    else
    {
        i = 4; // This runs since the condition was false
    }
    
    // At the end of this script, <code>i</code> is 4
```

As you can see, the code within the `else` statement's code block only executes if the condition within the `if` statement is false. The `if` statement and the `else` statement used together is informally referred to as an *if-else* statement.

### If-ElseIf-Else
One trick you can do with `else` statements is that you can use them to chain together multiple if-else segments. This can be called an *if-elseif-else* statement:

```
    int i = 5;
    
    if (i < 2)
    {
        i = 1; // Doesn't run since <code>i</code> is not less than 2
    }
    else if (i > 8)
    {
        i = 9; // Also doesn't run since <code>i</code> is not greater than 8
    }
    else 
    {
        i = 6 // All other conditions are false, so this will run
    }
    
    // At the end of this script, <code>i</code> is 6
```

:::note[Note]
Mentally, the `if` statement works just like a logical conditional sentence in plain English (or your own language). In the previous `if` example, for instance, it can be read out like so:

```
If the value in <code>i</code> is equal to 2, set <code>i</code> to equal 3.
```

You can include the `else` statement in this sentence as well:

```
If the value in <code>i</code> is equal to 2, set <code>i</code> to equal 3, else set <code>i</code> equal to 2.
```

Forming your conditions in logical prose like this is a useful way to visualize how you want your conditions to be structured.
:::

### Switch
As you can see, you can get some neat little if-elseif-else statement chains going along. But what if you had something like this?

```
    int i; // Is equal to some number
    
    if (i == 0)
    {
        // Do something if <code>i</code> is 0
    }
    else if (i == 1)
    {
        // Do something if <code>i</code> is 1
    }
    else if (i == 2)
    {
        // Do something if <code>i</code> is 2
    }
    else if (i == 3)
    {
        // Do something if <code>i</code> is 3
    }
    else if (i == 4)
    {
        // Do something if <code>i</code> is 4
    }
    // And so on...
```

That's a bit tedious, isn't it? Are you going to need to put in a new else-if statement for every single value that `i` could possibly be equal to?

As it turns out, there is a better way - the `switch` statement:

```
    int i; // Is equal to some number
    
    switch (i)
    {
        case 0:
            // Do something if <code>i</code> is equal to 0
            break;
        case 1:
            // Do something if <code>i</code> is equal to 1
            break;
        case 2:
            // Do something if <code>i</code> is equal to 2
            break;
        case 3:
            // Do something if <code>i</code> is equal to 3
            break;
        case 4:
            // Do something if <code>i</code> is equal to 4
            break;
    }
```

There's several bits of new information in there, so let's break it down:

First, you have the initial `switch` statement. Like the `if` statement, you start with the `switch` keyword followed by a value inside parentheses, which is in turn followed by a code block. Unlike the `if` statement, the `switch` statement does not use a boolean condition. Instead, it takes an integer value directly, then executes one of several code possibilities based on what that value is.

Within the `switch` statement's code block, there are several `case` keywords. `case` is used to start one of the "sub-block" sections that the `switch` statement could run. Each `case` keyword is followed by a value, denoting what value that case section represents. For example, if the value of `i` was 3, then the code within the `case 3` section would be run.

At the end of each `case` section is a `break` keyword. This is another keyword related to flow control, and I will go into it in greater detail later on in this lesson. For now, just know that it marks the end of a `case` code section.

There are a couple of other ways which you can use a `switch` statement. First, you can specify a `case` section that will run if the given value is one of several possibilities:

```
    int i; // Is equal to some number
    
    switch (i)
    {
        case 0:
        case 1:
        case 2:
            // Do something if <code>i</code> is equal to 0, 1, or 2
            break;
        case 3:
        case 4:
            // Do something if <code>i</code> is equal to 3 or 4
            break;
    }
```

As you can see, there isn't any code placed inside cases 0, 1, or 3. This causes the case to "fall through" to the next case, making it so the code inside `case 2` will run if `i` is equal to 0 or 1 as well.

You can also specify code to run if the given value doesn't match *any* of the cases:

```
    int i; // Is equal to some number
    
    switch (i)
    {
        case 0:
            // Do something if <code>i</code> is equal to 0
            break;
        case 1:
            // Do something if <code>i</code> is equal to 1
            break;
        case 2:
            // Do something if <code>i</code> is equal to 2
            break;
        default:
            // Do something if <code>i</code> is something else entirely
            break;
    }
```

In this example, if `i` doesn't match any of the cases (say if `i` were equal to 3), then the code within the `default` section will be run instead.

{{note|The `break` within the case sections is optional. If you do not put a `break` at the end of a case, then it will fall through just as though the that case section was empty. This is handy if you have code that you want to execute on one of several values, but other code that you only want to execute on a specific value:

```
    int i;
    int a = 1;
    int b = 2;
    int c = 3;
    
    switch (i)
    {
        case 1:
            a = 4; // Runs only if <code>i</code> is equal to 0
        case 2:
            b = 5; // Runs if <code>i</code> is equal to 0 or 1
        case 3:
            c = 6; // Runs if <code>i</code> is equal to 0, 1, or 2
            break;
    }
```
}}

## Loops
Conditionals are just one of the ways to have flow control in your program. Where conditions can make it so you can decide whether or not to execute some code, this section lets you specify whether to run some code *over and over again for a specified amount of time*. Appropriately enough, these statements are called *loops*.

### While
The fundamental loop statement is called the *while loop*. It's fairly simple in concept - just run a block of code for as long as a boolean condition is true:

```
    int x = 0;
    
    while (x < 5)
    {
        x++;
    }
```

A `while` loop follows a specific pattern. When the program first reaches the `while` statement, it first checks the condition. If it is true, then the code within the code block is run. Once the code block finishes, the program goes *back* to the while statement and checks the condition again. If it's still true, then the code block runs a second time. This process repeats over and over again until the condition becomes false.

In the above example, `x` is 0. 0 is less than 5, so the program enters the code block, which adds 1 to `x`. After that, it goes back to the `while` condition, which checks `x` again. `x` is now 1, which is still less than 5, so the code block runs and `x` gets 1 added to it again. This keeps going for when `x` is 2, 3, and 4. Once `x` becomes 5, then the condition is checked once more. `x` is now no longer less than 5 (as it is now equal to 5). The condition is false, so the program skips down below the code block and continues to run.

{{note|One thing to be wary of when dealing with loops is the "endless loop". This happens when a condition for a loop is such that the condition will never be false. The quintessential example of this is the following:

```
    while (true)
    {
        // Code in here will run forever
    }
    
    // Code out here will never run
```

Endless loops can never be broken, so the only way to get out of them is to force-close your program. In the programmer world, this is generally considered to be bad design.}}

### Do-While
A do-while loop is very similar to a while loop with one key difference. Take a look at the following example and see if you can tell what it is:

```
    int x = 0
    
    do
    {
        x++;
    } while (x < 5);
```

The `do` takes the place of the `while` from a while loop, and the `while` keyword and condition is moved to after the code block. This reflects the single difference between a while loop and a do-while loop - a do-while loop will always run its code block at least once. More specifically, where the while loop checks its condition *before* it runs its code block, the do-while loop checks its condition *after* running its code block each time.

To demonstrate this, look at the following:

```
    // While loop
    int x = 0;
    while (false)
    {
        x = 1;
    }
    
    // Do-While Loop
    do
    {
        x = 1;
    } while (false);
```

The condition inside the while statement for both loops is set to `false`, so it is guaranteed to fail the condition check. For the while loop, this means that the code inside the code block never runs, and `x` will remain at 0. However, since a do-while loop is guaranteed to run its code block at least once, `x` will be 1 once the loop is terminated.

### For
The while and do-while loop are great for when you want to repeat an action multiple times, but what if you want to operate over a range of values? Remember back in Lesson 2 and we were talking about arrays? Initializing an array was easy - all you had to do was declare an array variable. But what if you wanted to fill it full of values? Before, you would do it like this:

```
    array<int> arr;
    arr[0] = 0;
    arr[1] = 1;
    arr[2] = 2;
    arr[3] = 3;
    arr[4] = 4;
```

That's a bit wordy, isn't it? Although, all those lines of code do look repetitive, so this is a case where we can use loops to make it easier:

```
    array<int> arr;
    int i = 0;
    
    while (i < 5)
    {
        arr[i] = i;
        i++;
    }
```

That's a bit fancier. Instead of explicitly writing out each number, we use a loop that makes `i` go through each of the numbers with a loop and assign that number to each index of the array. It's still a bit wordy, though.

As it turns out, though, there's a loop statement designed specifically for this kind of situation: the *for loop*:

```
    array<int> arr;
    
    for (int i = 0; i < 5; i++)
    {
        arr[i] = i;
    }
```

Now that's concise. Let's go over how it all comes together.

First, as usual, the `for` keyword comes first, followed by some code surrounded by parentheses, and finally a code block. This code is split into three sections - a *setup*, a *condition*, and an *increase*. The setup code is run once, before the loop starts for the first time. Then the condition code is checked similar to the while loop - if the condition is true, then the code block is run. After the code block finishes, the code in the increase is run, followed by the condition getting checked again. This process is repeated (code block, increase, condition) until the condition becomes false.

In the above example, it starts by declaring the `i` variable and initializing it to 0. Then the condition is checked, which is true since 0 is less than 5. The code block runs, after which the increase section adds 1 to `i`. `i` is now 1, which is still less than 5, so the code block runs again. `i` becomes 2, 3, and 4, but once it becomes 5, the condition becomes false and the loop terminates.

{{note|All of the loop statements have been accompanied by a code block surrounded by curly braces, but this isn't actually strictly necessary. Instead, you can have a single line of code following the loop statement, and this line of code becomes the "code block" of the loop. For example, if you have the following loop:

```
    while (some condition)
    {
        // some code
    }
```

The brackets can be removed entirely, leaving the following:

```
    while (some condition)
        // some code
```

You can do this with the do-while loop and the for loop as well. Keep in mind, though, that this only works if the code body consists of a single line. If you have two lines:

```
    while (some condition)
        // some code
        // some other code
```

The second line of code is not recognized as being part of the loop, so it won't run until the loop terminates.}}

### Loop Control
When you set up a loop, it will run until its condition becomes false (even if it has to run forever). However, sometimes, you want to have a bit more control over how the loop runs. For these cases, there are two special keywords - `continue` and `break`.

When you use `continue` in a loop, it tells the loop to skip the rest of the code block and jump straight to checking the condition (or, in the case of a for loop, running the *increase* code):

```
    int x = 0;
    
    while (x < 5)
    {
        x++;
        cLux_AddDebugMessage("A");
        
        continue;
        
        cLux_AddDebugMessage("B");
    }
```

If you had this code running in HPL3, it would print "A" 5 times but "B" only once. That's because the `continue` causes the "B" line of code to not run as the program skips the rest of the code block and goes right back to the condition.

The second loop control keyword is `break`. What it does is it causes the loop to stop entirely. It skips the rest of the code block and terminates the loop:

```
    int x = 0;
    
    while (x < 5)
    {
        x++;
        cLux_AddDebugMessage("A");
        
        break;
        
        cLux_AddDebugMessage("B");
    }
```

Run in HPL3, this code would only print a single "A", even though its logic would say that it should loop 5 times. That's because when the program reaches the `break`, the loop stops right where it is and exits, going to the next code after the loop.

:::note[Note]
If you remember, `break` is the same keyword that is used to mark the end of a `case` section in a `switch` statement. It's role there is the same as in a loop - it causes the program to exit the switch block instead of falling through to the next case section.
:::

HPL3/Scripting/AngelScript Fundamentals/Chapter 4 - Operators and Expressions|Chapter 4 - Operators and Expressions|HPL3/Scripting/AngelScript Fundamentals|AngelScript Fundamentals|HPL3/Scripting/AngelScript Fundamentals/Chapter 6 - Functions|Chapter 6 - Functions

## Source & attribution

- Original Frictional Wiki page: [HPL3/Scripting/AngelScript Fundamentals/Chapter 5 - Statements and Flow Control](https://wiki.frictionalgames.com/page/HPL3/Scripting/AngelScript_Fundamentals/Chapter_5_-_Statements_and_Flow_Control)
- Revision: `4574`
- Source update: `2020-08-15T20:14:03Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).
