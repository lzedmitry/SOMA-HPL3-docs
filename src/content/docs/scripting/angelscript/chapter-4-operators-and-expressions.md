---
title: Chapter 4 - Operators and Expressions
description: "So we can create variables now, and we can store values in those variables. That's great and all, but there's only so much we can do with just assigning values. What we want to do is manipulate those values in whatever w"
category: scripting
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Scripting/AngelScript_Fundamentals/Chapter_4_-_Operators_and_Expressions"
sourceRevision: 4573
sourceUpdated: "2020-08-15T20:13:28Z"
lastSynced: "2026-09-28T13:28:41Z"
sourceStatus: verified
generated: true
tags:
  - scripting
---
So we can create variables now, and we can store values in those variables. That's great and all, but there's only so much we can do with just assigning values. What we want to do is manipulate those values in whatever ways we want.

That is where operators come in. Operators perform an operation (appropriately enough) on one or more values. You've already been introduced to one of the operators: the assignment operator (`=`). Its job is to take a value on the right and assign it to a variable on the left. When you take several values and manipulate them or assign them to variables, the resulting line of code is called an *expression*.

There are a bunch of other operators as well, and they generally fall into one of three categories: math operators, boolean operators, and bitwise operators.

## Math Operators
The the math operators are what you might expect - general arithmetic. Each one results in a numeric value.

| Operator | Name | Example |
| --- | --- | --- |
| + | Addition | 
```
int x = 2 + 5; // 7
```
 |
| - | Subtraction | 
```
int x = 7 - 1; // 6
```
 |
| * | Multiplication | 
```
int x = 4 * 3; // 12
```
 |
| / | Division | 
```
int x = 6 / 3; // 2
```
 |
| % | Modulo | 
```
int x = 9 % 4; // 1
```
 |

Those first four aren't really surprising. It's just basic math. That last one may be a new one, but it's not that complex. Basically, "modulo" is another name for "remainder". So in the example above, when you do the modulo operation on `9` and `4`, you perform the integer division on the two numbers and return the remainder (9 / 4 = 8 remainder 1, so 9 % 4 = 1).

:::note[Note]
When I say that modulo is another name for remainder, that's not *entirely* true. There are actually subtle differences between a remainder and a modulo, which are described [on this website](http://www.sitecrafting.com/blog/modulus-remainder/). That being said, when performed on positive numbers, modulo and remainder behave identically, which will in practice account for 99% of all times you will be using modulo in your code.
:::

Some of you may have tilted your head quizzically in the last paragraph when I mentioned doing the "integer division" on some numbers. The reason that I specified what kind of division to perform is that, unlike the other operators, division behaves slightly differently when performed on integer types as opposed to floating-point types. When you perform division on floating-type, it results in what you might expect:

```
    float f = 5.0 / 2.0; // 2.5
```

However, doing the same division on integer types, you get a different result:

```
    int i = 5 / 2; // 2
```

This is because unlike the other operators, division between two whole numbers can result in a decimal number. However, integer types cannot hold decimal values. Because of this, if you store the result of a division that would be a decimal into an integer variable, the decimal part of the number is discarded. In other words, every decimal value is rounded down to the nearest whole number.

In addition to the math operators shown above that takes two numbers and assigns the result to a variable, there are also a set of math operators that are known as "compound operators":

*(In the following table, the initial value of `x` is `5`.)*

| Operator | Name | Example |
| --- | --- | --- |
| += | Compound Addition | 
```
x += 2; // 7
```
 |
| -= | Compound Subtraction | 
```
x -= 3; // 2
```
 |
| *= | Compound Multiplication | 
```
x *= 3; // 15
```
 |
| /= | Compound Division | 
```
x /= 2; // 2
```
 |
| %= | Compound Modulo | 
```
x %= 2; // 1
```
 |

As you can see, the compound operators are all the regular math operators joined together with the assignment operator (`=`). What they do is they take the value of the variable on the left, perform the specified math operation with the value on the right, and then assign the result back to the variable on the left.

These operators are a convenience operation that exists between a regular math operator and an assignment operator. The reason for this is because the following two lines of code perform the exact same operation:

```
    x = x + 5;
    x += 5;
```

There are two more math operators to know about - the increment operators:

*(In the following table, the initial value of `x` is `5`.)*

| Operator | Name | Example |
| --- | --- | --- |
| ++ | Increment | 
```
x++; // 6
```
 |
| %%--%% | Decrement | 
```
x--; // 4
```
 |

Like the compound operators, the increment operators are shorthand for a specific operation. In this case, they are shorthand for adding or subtracting a value by 1. In other words, doing `x++` will take the value of `x`, add 1, and then store the result back into `x`.

However, there's a special way that the increment operators can be used. They can either be used before the variable (known as "pre-increment") or after the variable (known as "post-increment"). By themselves, a pre-increment and post-increment do the exact same thing. The difference happens when you use the increment operator alongside an assignment:

```
    int a = 5;
    int b = ++a;
```

What do you think the value of `a` is? How about `b`? As it turns out, the value of both `a` and `b` is 6. The reason for this is because the pre-increment operator `++a` increments the value of `a` before assigning it to `b`. However, if I had the following instead:

```
    int a = 5;
    int b = a++;
```

What do you think the values of `a` and `b` are now? The value of `a` is still 6, but the value of `b` is 5. That's because with a post-increment operator, the operator waits until the overall expression is complete before incrementing the variable.

Another way of looking at how this works is to see the regular math operator equivalents of the above two examples:

```
    // Pre-increment equivalent
    int a = 5;
    a = a + 1;
    int b = a;
    
    // Post-increment equivalent
    int a = 5;
    int b = a;
    a = a + 1;
```

    

:::note[Note]
You might be wondering if the compound and increment operators behave identically to their arithmetic operator equivalents, then why even have them? There are two reasons for this. First, it's more convenient to use the shorthand operators when they are available (and never underestimate the value of convenience in programming). Second, when the code gets compiled, there are special instructions that can perform the compound and increment operations more efficiently than their regular math operation counterparts.
:::

### String Concatenation
When you are dealing with strings, you can add two string values together using the addition operator (`+`). This process is called "concatenation". When you do this, the string value on the right is added onto the end of the string value on the left, and the result is a single string value:

```
    tString a = "abc";
    tString b = "def";
    tString c = a + b; // "abc" + "def" = "abcdef"
```

*(This works with the addition compound operator as well.)*

:::note[Note]
When dealing with strings and other values, you can concatenate any built-in type with a string as well. When you do this, the type is automatically converted into a string. For example, see the following:

```
    int x = 123;
    tString s = "abc" + x;
    
    // s becomes "abc" + 123, or "abc123"
```

:::

## Boolean Operators
Where the math operators return a numeric value, the boolean operators returns a bool type value. These operators are split into categories as well: the comparison operators and the logic operators:

| Operator | Name | Example |
| --- | --- | --- |
| == | Is Equal To | 
```
bool b = 3 == 3; // true
```
 |
| != | Not Equal To | 
```
bool b = 3 != 3; // false
```
 |
| > | Greater Than | 
```
bool b = 2 > 1; // true
```
 |
| < | Less Than | 
```
bool b = 2 < 1; // false
```
 |
| >= | Greater Than or Equal To | 
```
bool b = 3 >= 3; // true
```
 |
| %%<=%% | Less Than or Equal To | 
```
bool b = 3 <= 3; // true
```
 |

As you can see, they are fairly self-explanatory. The comparison operators all compare a value on the left with a value on the right, then returns `true` if the comparison is satisfied or `false` if not. For example, `1 == 1` would be true, whereas `1 == 2` would be false.

:::note[Note]
1=Note the difference between the assignment operator `=` and the comparison operator `==`. One of these operations assigns a value to a variable, whereas the other one compares the values and returns a result. In order to differentiate them, when "sounding out" the code in regular English (or your relative language), always describe `a = b` as "a equals b" and always describe `a == b` as "a is equal to b".
:::

Where the comparison operators compare numerical values, the logic operators compare boolean values:

| Operator | Name | Example |   |   |
| --- | --- | --- | --- | --- |
| && | Logical AND | 
```
bool b = true && true; // true
```
 |   |   |
|  |  | Logical OR | 
```
bool b = true | false; // true
```
 |
| ^^ | Logical XOR | 
```
bool b = false ^^ false; // false
```
 |   |   |
| ! | Logical NOT | 
```
bool b = !true; // false
```
 |   |   |

Each logical operator has a specific set of rules that determines whether the result of the logical operation between two values is true or false. The way to visualize these rules is using a construct called a *truth table*, which is a chart that plots all the possible values of the inputs and shows the result of the operation between those values.

First, the Logical AND operator (`&&`). The rule for this operator is "the result is true of both of the inputs are true".

```
x     | y     | x && y
---------------------
false | false | false
true  | false | false
false | true  | false
true  | true  | true
```

Second, the Logical OR operator (`||`). The rule for this operator is "the result is true of either of the inputs are true".

```
x     | y     | x || y
---------------------
false | false | false
true  | false | true
false | true  | true
true  | true  | true
```

Third, the Logical XOR operator (`^^`), which is short for "exclusive OR". The rule for this operator is "the result is true of either of the inputs are true, but not both".

```
x     | y     | x ^^ y
---------------------
false | false | false
true  | false | true
false | true  | true
true  | true  | false
```

The last operator Logical NOT (`!`) is special in that it only works on a single value. All it does is flip that value to the opposite.

```
x     | !x
---------------------
false | true
true  | false
```

## Bitwise Operators
The bitwise operators are similar to the logical operators. The difference is that they work on numerical values and they affect the bit values of the number in binary form.

*(For the sake of simplicity, we are going to use an imaginary 4-bit type `uint4` for values in examples for these operators.)*

| Operator | Name | Example |   |
| --- | --- | --- | --- |
| & | Bitwise-AND | 
```
uint4 i = 2 & 1; // 0
```
 |   |
| \| | Bitwise-OR | 
```
uint4 i = 2 | 1 // 3
```
 |
| ^ | Bitwise-XOR | 
```
uint4 i = 2 ^ 3; // 1
```
 |   |
| << | Left Shift | 
```
uint4 i = 2 << 1; // 4
```
 |   |
| >> | Right Shift | 
```
uint4 i = 4 >> 1; // 2
```
 |   |
| ~ | Bitwise-NOT | 
```
uint4 i = ~4; // 11
```
 |   |

These are probably some of the least intuitive examples in this entire lesson. That's because instead of operating on the numbers, bitwise operators operate on the binary data underlying the numbers. For example, in our temporary 4-bit representation, the number 3 is represented in binary as "0011". 

:::note[Note]
For an explanation of how binary works, see the note in Lesson 2 in the section under "Built-In Types".
:::

The bitwise-AND, bitwise-OR, and bitwise-XOR operators (`&`, `|`, and `^`, respectively) follow the same rules as their logical equivalents. (See above for a reminder of what those rules are.) The only difference is that it performs that comparison on the corresponding bits in two numerical values. For an easier visual representation, see the following example:

```
    uint4 a = 10;    // Binary: 1010
    uint4 b = 6;     // Binary: 0110
    uint4 c = a & b; // Binary: 0010
```

If you look at the binary representations in that example, pretend that the 0's are false and the 1's are true. You then take the rules for logical AND (`&&`) and apply them to each binary digit, comparing straight down. The first digit has a 1 in `a` and a 0 in `b`, so the result is 0. The second digit has a 0 in `a` and a 1 in `b`, so the result is again 0. The third digit has 1 in both `a` and `b` so the result there is 1. And the last digit has a 0 in both `a` and `b`, so the result is 0. If you then take those result digits "0010", it becomes the binary representation for the number 2, which is the value that gets stored in `c`.

This same process happens for the bitwise-or and bitwise not operators as well. In those cases, you merely use the rules from the logical OR (`%%||%%`) and the logical XOR (`%%^^%%`) operators, respectively. 

:::note[Note]
Try and guess what the results for the following two examples are:

```
    // Bitwise-OR
    uint4 a = 10;    // Binary: 1010
    uint4 b = 6;     // Binary: 0110
    uint4 c = a | b; // Binary: ????
    
    // Bitwise-XOR
    uint4 a = 10;    // Binary: 1010
    uint4 b = 6;     // Binary: 0110
    uint4 c = a ^ b; // Binary: ????
```

*(Go ahead, try and work it out. Did you try? Don't continue until you do.)*

If you got a binary result of "1110" (which represents 14) for the bitwise-OR operator and a binary result of "1100" (which represents 12) for the bitwise-XOR, then nice work!
:::

The next two operators in the table are the left-shift operator and the right-shift operator (`%%<<%%` and `%%>>%%`, respectively). Where the previous bitwise operators performed comparisons on the bits of two values, the shift operators instead take all the bits of a binary number and moves them to the left or right by a specified number of digits. See the following example:

```
    uint4 a = 6;      // Binary: 0110
    uint4 b = a << 1; // Binary: 1100
```

As you can see, when `a` gets left-shifted by 1, all the 1's in the binary moved one digit to the left. The same thing happens when the right-shift operator is used:

```
    uint4 a = 13;     // Binary: 1101
    uint4 b = a >> 2; // Binary: 0011
```

All the binary digits of `a` got shifted two positions to the right. Notice, however, that this caused a 1 to get shifted right off the edge of the binary. When this happens, that 1 ceases to exist - even if you were to then left-shift `b`, you would only bet 0's back.

:::note[Note]
An interesting property of the shifting operators is that left-shifting is the same as multiplying by 2 and right-shifting is the same as dividing by 2 (integer division, that is). This is due to the nature of binary being a base-2 system. A similar nature happens with our regular numbers, which exists in a base-10 system - if you were to take a number like 500 and "shift" all the digits to the right, it becomes 50, which happens to be 500 divided by 10.
:::

The last bitwise operator is the bitwise-NOT (`~`). It acts similarly to the logical NOT (`!`), and is also known as the bitwise-compliment. What it does is it takes all the bits in a number and flips them - all the 1's become 0, and all the 0's become 1:

```
    uint4 a = 5;  // Binary: 0101
    uint4 b = ~a; // Binary: 1010
```

Bitwise-operators are a bit more technical than the other operators, but as you can see, they do have fairly simple rules. Once you understand those rules, they aren't so bad after all!

:::note[Note]
The bitwise-operators have their own set of compound operators as well. They follow the same concept as the math compound operators - the value in the variable on the left gets put through the operator with the value on the right, and the result is stored back into the variable on the left:

```
    uint4 a = 2;
    a |= 4;
    // a is 6
```

:::

## Order of Operations
All the operators have what is known as a precedence. This means that when multiple operators are used at once, there is a strict order they follow which determines which ones get evaluated first. For example, if I had the following code:

```
    int i = 2 + 4 * 3;
```

Intuition might make you assume that `i` would have the result of 18, since 2 plus 4 is 6, which when multiplied by 3 gives 18. However, order of operations state that multiplication happens before addition. That would mean that you first have to multiply 4 and 3 to get 12, and 2 plus 12 is 14, which is the value that `i` will actually end up with.

Here is the full list of operators in order of their precedence (higher in the list means the operator happens first):

| ++ -- | Increment Operators |   |
| --- | --- | --- |
| ! | Logical NOT |   |
| ~ | Bitwise-NOT |   |
| * / % | Multiply, Divide, Modulo |   |
| << >> | Bitwise Left-Shift, Right-Shift |   |
| & | Bitwise-AND |   |
| ^ | Bitwise-XOR |   |
| \| | Bitwise-OR |   |
| <= < >= > | Comparison Operators |   |
| == != ^^ | Equality Comparison Operators and Logical XOR |   |
| && | Logical AND |   |
|  |  | Logical OR |
| = += -= *= /= %= &= \|= ^= <<= >>= | Assignment and Compound Operators |   |

Whenever two operators with the same precedence occur in an expression, they are handled from left to right.

One thing you can do to sort of subvert the order of operations, however, is to group part of your expression inside parentheses. Whenever part an expression is within parentheses, that part gets processed first. So if you were to have the above example but with the addition operation within parentheses, you would end up with a value of 18:

```
    int i = (2 + 4) * 3;
```

HPL3/Scripting/AngelScript Fundamentals/Chapter 3 - Variables and Types|Chapter 3 - Variables and Types|HPL3/Scripting/AngelScript Fundamentals|AngelScript Fundamentals|HPL3/Scripting/AngelScript Fundamentals/Chapter 5 - Statements and Flow Control|Chapter 5 - Statements and Flow Control

## Source & attribution

- Original Frictional Wiki page: [HPL3/Scripting/AngelScript Fundamentals/Chapter 4 - Operators and Expressions](https://wiki.frictionalgames.com/page/HPL3/Scripting/AngelScript_Fundamentals/Chapter_4_-_Operators_and_Expressions)
- Revision: `4573`
- Source update: `2020-08-15T20:13:28Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).
