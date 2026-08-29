---
title: Chapter 8 - Classes
description: "Using the knowledge you've gained thus far, you can make some pretty respectable programs. In fact, things before this point made up the bulk of what programming was like back when C was the new kid on the block. It's a"
category: scripting
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Scripting/AngelScript_Fundamentals/Chapter_8_-_Classes"
sourceRevision: 6191
sourceUpdated: "2020-11-18T19:08:20Z"
lastSynced: "2026-08-28T18:40:04Z"
sourceStatus: incomplete
generated: true
tags:
  - scripting
---
Using the knowledge you've gained thus far, you can make some pretty respectable programs. In fact, things before this point made up the bulk of what programming was like back when C was the new kid on the block. It's a style known as *procedural programming*. It's a simple concept - a program has a start and it goes down a list of instructions until it reaches an end.

Nowadays, though, programming has evolved into a myriad of different styles. The one that has grown to be the most popular among the highest-used programming languages is known as *object-oriented programming* (OOP).

## What is Object-Oriented Programming
Imagine you had a program in which you needed to maintain a bunch of related variables. In this scenario, let's pretend that our program needed to simulate a bike down to various details:

*A bike has two wheels, a seat, and gears.
*The wheels can be a particular size.
*The seat can be at various heights.
*There can be different numbers of gears.
*The bike itself could be moving at various speeds, or fully stopped.

There's our description of a bike. (Ignore the fact that it leaves a few things out - we don't want to overcomplicate our example.)

Let's make a program now that would store these variables:

```
	int gearCount;
	int wheelSize;
	float seatHeight;
	float bikeVelocity;
```

That doesn't look so bad. But what if our program had to simulate more than one bike? How would you store the information on each one? I suppose you could just have groups of variables for each bike:

```
	int gearCount1;
	int wheelSize1;
	float seatHeight1;
	float bikeVelocity1;
	
	int gearCount2;
	int wheelSize2;
	float seatHeight2;
	float bikeVelocity2;
	
	int gearCount3;
	int wheelSize3;
	float seatHeight3;
	float bikeVelocity3;
```

That's not very helpful, is it? Sure, we can store information on three bikes, but what about four? Or a hundred? If we have to type out a new set of variables for each bike, this program is going to get really cumbersome really fast.

This situation does look familiar though. Perhaps we can use arrays to simplify things a bit?

```
	array<int> gearCounts;
	array<int> wheelSizes;
	array<float> seatHeights;
	array<float> bikeVelocities;
```

This is a bit better. Now we can store information on as many bikes as we want. As a bonus, since we are using arrays, we can also use a loop to access them all instead of referring to each one individually by hand.

This still isn't quite right, though. For one, there isn't any relationship between the arrays apart from their assumed one. In other words, there's nothing in the language that joins together these four arrays in order to set them apart as being intended for a common purpose. 

There's also another problem. Each "bike" is represented by the values in the same index across all four arrays. (i.e. Bike "1" would be represented by the data in `gearCounts[1]`, `wheelSizes[1]`, `seatHeights[i]`, and `bikeVelocities[1]`.) But what if someone came along and shoved some information in some arrays without doing it in the others? Now all the data is out of order, and since there's no way to tell which data originally belonged to which bike, there's no way to reverse it, so your entire data structure just became corrupted beyond repair.

What we need is a way to group these four variables together into a single thing so that no matter what, the same four values will always be linked. This is where object-oriented programming comes in.

## Classes
In OOP, an "object" is a group of variables (called fields) that join together to form a cohesive whole. Together, they can represent various tangeable concepts that would be incredibly difficult to manage otherwise.

For our bike example, instead of depending on the interoperability of distinct values, we can create an object representation of the bike itself by defining a *class*:

```
	class Bike
	{
		int gearCount;
		int wheelSize;
		float seatHeight;
		float bikeVelocity;
	}
```

From a technical standpoint, there is only one new keyword in there for you - the `class` keyword. After that keyword comes the identifier for the class, followed by a code block that forms the body of the class.

We can now use this class whenever we want to create a bike *instance*:

```
	Bike myBike;
```

In OOP, an object is the blanket term for a particular thing or concept with defined properties. A class is a bunch of code that represents the blueprint of an object, much like an architect would create a blueprint of a house. An instance represents a single manifestation of that class. 

You can think of it like this. The conceptual idea of Toyota Corola is like the object, the blueprints at the Toyota factory are like the class, and an individual car you see driving around is like the instance.

:::note[Note]
Just to confuse you, programmers in different disciplines sometimes use the terms "object" and "instance" interchangeably. There's not really a way to reconcile this, so I'm just giving you a heads up.
:::

Now that we have an instance, we are going to need to be able to access the fields within that instance. Remember the note back in Lesson 2 about dot-notation? As it turns out, this is exactly how we do it:

```
	// Getting the value of a field
	int size = myBike.wheelSize;
	
	// Setting the value of a field
	myBike.gearCount = 5;
```

As it turns out, it's not just fields we can have in objects. We can also define functions too:

```
	class Bike
	{
		int gearCount;
		int wheelSize;
		float seatHeight;
		float bikeVelocity;
		
		// circumference = PI * diameter
		float GetWheelCircumference()
		{
			// cMath_PI is a globally available value equal to PI 
			// (or a close enough approximation to it, rather)
			return wheelSize * cMath_PI;
		}
	}
```

We access them in the same way we would access fields as well:

```
	Bike bike;
	bike.wheelSize = 600; // in millimeters
	float wheelCircum = bike.GetWheelCircumference();
```

:::note[Note]
The technical description for this accessing process is actually using a new kind of operator known as the member access operator (`.`). When this operator is used on an instance of an object, it tells the program to "look inside this object and get the member with this name".

The term "member" is used to describe any part of the inside of a class. Fields, functions, and other things are all considered a "member".
:::

Now that we have our `Bike` class all set up, lets see how we can use it in our program:

```
	array<Bike> bikes;
	
	for (int i = 0; i < 100; i++)
	{
		Bike bike;
		bike.gearCount = 5;
		bike.wheelSize = 600;
		bike.seatHeight = 3.0;
		bike.bikeVelocity = 50;
		
		bikes.push_back(bike);
	}
```

That's pretty neat, isn't it? Since `Bike` is just another type (an object type, but still a type), you can easily create an array of them. Plus, all the information for each bike is packed within each `Bike` instance, so there's no chance of information getting messed up with other bikes. It's all just safely packed in neat little packages that the program itself keeps organized so you don't have to worry about it.

:::note[Note]
"Regular" types like `int` or `bool` are called *primitive types* because they are intrinsic to the programming language itself. The difference between primitive types and object types is that primitive types merely store a single value, whereas object types can store multiple values or even other object types in their fields. In Lesson 2, the numeric types and the `bool` type are all primitive types, and everything else are object types.

(The `tString` type is a bit of a special case in that it's sort of both kinds of types at the same time. Just don't think about that too much.)
:::

## Constructors
When an instance of a class gets created, all of the fields in that instance are set to their default values (depending on their types). However, for some object types, you don't want that to happen. Say, for example, our bike had a gear switching field that represented shifting between gears from 1 to 5 (assume there are 5 gears):

```
	class Bike
	{
		// ... 
		int currentGear;
	}
```

When you create an instance of `Bike`, `currentGear` will have an initial value of 0. That doesn't make any sense, though, because there are only gears one through five. Any other value for `currentGear` would be an incorrect value.

When defining a class, you can define a special kind of function called a *constructor*. The job of a constructor is to provide a way to create an instance of an object that you can customize so that various fields have an initial value that you specify. Constructors can also be defined with parameters, allowing code to pass in values that they want the constructor to use.

```
	class Bike
	{
		// ...
		int currentGear;
		
		Bike()
		{
			currentGear = 1;
		}
		
		Bike(int startingGear)
		{
			currentGear = startingGear;
		}
	}
	
	// ...
	// Elsewhere in your code
	
	// Calling the default constructor without parameters
	Bike bikeWithDefaultGear;
	
	// Calling the second constructor with parameters
	Bike bikeWithSpecificGear(3);
```

As you can see, constructors are defined similarly to functions. There are two key differences - first, the name of the constructor function must be the same as the name of the class, and second, a constructor does not define a return type.

As far as how they are used, the constructor with parameters defined is called just like a function - by putting parentheses around the parameter(s). The parameterless constructor is called implicitly whenever the instance is declared, so there's no need to have an empty set of parentheses in this case.

## Member Qualifying
You know that when you want to access a variable, field, or parameter, you use its name, of course. But what would happen in the following situation?

```
	class Foo
	{
		int a; // this a is 5
		
		void DoSomething(int a) // this a is 3
		{
			int b = a;
		}
	}
```

Which `a` is the code within the function referring to - the field or the parameter? As it turns out, the variable with the highest scope takes precedence, which in this case would be the parameter. (The field is in the class scope whereas the parameter is only in the function scope.) That means that when the function is done, `b` will have a value of 3.

That's good to know, but what if you needed to access the field instead of the parameter? Do you always have to name the parameter and the field different names to avoid these conflicts?

Well, there's not a strict convention around it, though in my opinion you should avoid doing that anyway just to prevent potential confusion. However, if you do find yourself in a situation where you need to refer to the field when a same-name parameter exists, there is a special keyword for just such an occassion:

```
	class Foo
	{
		int a; // this a is 5
		
		void DoSomething(int a) // this a is 3
		{
			int b = this.a;
		}
	}
```

The `this` keyword performs something called *member qualification*. What that means is that it ensures that the `a` being referenced is the field instead of the parameter by "qualifying" it. 

{{note|What `this` strictly does is it provides a reference to the current object. For example, if you had the following:

```
	class Foo
	{
		int a;
		
		void DoSomething()
		{
			this.a = 5;
		}
	}
	
	// ...
	// Elsewhere in your code
	
	Foo foo;
	foo.a = 5;
```

The `foo` variable outside of the class and the `this` keyword inside of the class are both referring to the same underlying code in memory.}}

There are some conventions that state you should always use the `this` keyword when referring to a field within the class. This follows the train of thought that you should always be as explicit as possible when programming so as to reduce ambiguity and confusion to zero (or as close as you can get). Personally, I find this convention to be a bit tired and  old-fashioned, as it promotes verbose coding practices that cause programming to take longer than it needs to. On the otherhand, there's something to be said about being explicit in cases where your intent isn't obvious. So my personal suggestion is to use `this` when referring to a member of a parent class just because in the child classes, it's not immediately apparent where that member is defined. ("Parent" classes and "child" classes are covered under the appendix section [Inheritance](https://wiki.frictionalgames.com/page/hpl3/community/scripting/angelscript_tutorial#inheritance).) 
:::caution[SOURCE STATUS: Incomplete]
update this redirect
:::

HPL3/Scripting/AngelScript Fundamentals/Chapter 7 - Calling Other Scripts|Chapter 7 - Calling Other Scripts|HPL3/Scripting/AngelScript Fundamentals|AngelScript Fundamentals|HPL3/Scripting/AngelScript Fundamentals/Chapter 9 - Miscellaneous AngelScript Features|Chapter 9 - Miscellaneous AngelScript Features

## Source & attribution

- Original Frictional Wiki page: [HPL3/Scripting/AngelScript Fundamentals/Chapter 8 - Classes](https://wiki.frictionalgames.com/page/HPL3/Scripting/AngelScript_Fundamentals/Chapter_8_-_Classes)
- Revision: `6191`
- Source update: `2020-11-18T19:08:20Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).
