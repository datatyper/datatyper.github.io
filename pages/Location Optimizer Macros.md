title: Location Optimizer Macros
subtitle: The Fourth Kind of Macros That You Have Never Used
status: published
progress: 10%
date: 2020-04-07
category: alteryx
tags: [alteryx, optimization, spatial]
summary: Location Optimizer Macros can be used to add or remove suggested locations to a network, based on a criteria set by the user.


# Location Optimizer Macros (LOM)

There are four types of macros. Though most people can't even remember the name of the elusive fourth kind. We have,

1. Standard Macros - they package up several tools into a single tool
2. Batch Macros - they run in a loop for every batch of records in the data
3. Iterative Macros - they run in a loop repeatedly until a condition is met
4. Location Optimizer Macros - they also run **multiple iterations** to determine the best **suggested locations** to add or remove from a **network** based on a **score**.

The **network** here just refers to your spatial data.  The **multiple iterations** means that like the Batch and Iterative macros, the LOMs with run multiple times to find a solution. The **suggested locations** are additional spatial data points from which you are selecting from. And the **score** is a measure - to be minimized or maximized - that is used to determine the best location(s).

So, for example, if you owned a bike retailer with several stores, and you wanted to open a few new stores, you could use an LOM to determine the best locations. In this scenario, 


**What is the network?** These are your existing store locations. (This is a fancy term for your current spatial data)  
**Suggested locations?** The locations of potential new store locations. (You need to provide some viable options)  
**Score?** In this case, we will go with the total distance between each of your customers and their nearest store.

Two other things we need to specify is,  
1. How many stores we wish to open and, 
1. That we wish to minimize the score (we want to be close to our customers).

From their Alteryx LOMs take care of running different combinations of the LOMs to find the best solution (the locations with the lowest score).

![Warning]
(The LOM is very similar to the Optimization Tool. In the Optimization Tool you want to maximize or minimize a score - the result of the objective function. The same thing is true for LOMs, except you are adding points rather than deducing the value of decision variables. I appreciate I might have lost a lot of people with that last bit. I promise this will become more clear with a few examples)


## How does it work?
The Location Optimizer uses two phases.    
* Phase 1 uses a generic algorithm, it starts with a random guess and keeps the best mutations as the input for Phase 2. 
* Phase 2 then re-balances the set by iterating over small valid changes to each location until the score of the location set has been optimized.  
  
The Speed/Optimization control determines how long we stay in Phase 1 before completing the optimization in Phase 2.


## Sample Workflows
There is little guidance out there on how to use Location Optimizer Macros (or as I will refer to them going forward, LOMs). What we do have is two example workflows,
* Optimize location by minimizing distance
* Optimize location with a gravity model

![[lom-sample-workflows.png]]

The two examples provided by Alteryx provide good use cases for the 

## Example 0 - A Trivial Example
Let us look at a trivial example to get acquainted with LOMs...

(As this is a trivial example there are ways to do this without LOMs, the same way you can calculate the factorial of a number without an iterative macro, using the Generate Rows Tool and Multi-Row Formula Tool. But it still serves as a good example from which to learn how LOMs work)

Four friends live in all four corners of the United States. 
![[lom-four-friends-1.png]]

And they want to meet.

Furthermore, they decide that it's only fair that they split the petrol costs equally between them. That is, they want to find a place that minimizes the total distance travelled.

### Using the Centroid

You might think that the centroid (easily calculated using the Summarize Tool) might be a good start,

![[lom-four-friends-2.png]]

But there are a couple of problems with this.

(Ask audience to suggest why)

The first issue is that the centroid falls in Wichita. And they don't want to go to Wichita. LOMs will solve this, because the algorithm will only choose from a list of *suggested locations*. And they'll only suggest locations of places they want to go.

Secondly, and more importantly, the centroid does not necessarily minimize distance. For example, take the case below,

![[lom-four-friends-centroid-vs-min-distance.png]]
In this example the centroid occurs at position 1. The total distance from the centroid is then 1 + 1 + 2 = 4 units.
However, if the meeting point was position 0, then the total distance would be 0 + 0 + 3 = 3 units.
So the centroid needn't provide the best answer. Now we turn to LOMs to solve our probllem

### Using Location Optimizer Macros
Just like Batch and Iterative Macros we build out the solution for one iteration and then let Alteryx work its magic. The process is as follows,
1. Set the existing locations of the network. In this case, the friend locations. This could be from an Input Data/Text Input/Map Input Tool or a Macro Input if you want your workflow to provide the existing locations dynamically.
2. Provide a single location as template for the macro input. As with all macros, this is dummy data, so the exact location does not matter here. Name this input "Potential Locations"
3. Calculate the *Score*. We want to minimize distance from the friends locations. So lets calculate the total distance and pass this to a Macro Output. Name this output "Score"


![[lom-four-friends-macro.png]]

4. Add another Macro Output. The first Macro Output only outputs the score (i.e. the minimum distance). But we'll also want to see the name of the chosen location, so we add a second Macro Output that provides this information.


# Notes

## Meeting with Paige
What it does.
I want size more locations and picks the best ones based on a score. Have to specify how many

Use Case 1
Identifying last mile delivery locations. Doing delivery in a city - where do you put them
Ghost kitchens - where would you locate them so that they don't impact your existing restaurants

## Conversation with Tim Raines
### 1. Is it useful, or just a legacy feature of Alteryx?
LOMs are definitely still useful, albeit with more limited use cases than the other three macro types. The implementation in Alteryx is extremely flexible when dealing with spatial data. You can do almost anything within it. It can even be fooled into being a non-spatial genetic algorithm (though I wouldn't recommend it).

It's all about figuring out which 'site' is the best site out of a list of potential sites. The technique itself has a really long history in site location, especially as an academic problem to overcome. I don't know that it's made it very far in general usage yet, though there are some standardized implementations with ESRI which make it a bit easier to do than Alteryx for the lay-user. It tends to be used by very experienced users that are answering a specific niche set of questions. That is, I want to know what the most optimal locations are out of a set of potential locations to satisfy a condition.

### 2. Have you used it in a useful capacity?
The blog post is actually a really abstracted version of a use case that I had, where we were asked "how many distribution centers would we need to serve as much population as possible within 60 minutes" - without knowing where any candidate sites are.

### 3. Do you know any good use cases/examples
There are some really topical examples that are great use cases. Such as, companies wishing to choose the best locations for a new head office that minimize travel distance for their staff. Distribution companies that wish to make sure their centers are minimizing travel distance between them and their delivery points. where is the best location to site a hospital that will minimize the travel distance for the surrounding population most at need?
However, whilst you can do analytically optimize solutions in such use cases, the reality of many of these decisions in business is that you may not be able to secure the optimum site at a cheap enough price, or secure planning permission, and so on. Reality often gets int eh way of the optimum solution. That said, it can help to figure out if you should locate a site in town A vs town B quite well, even if the intricacies cloud the decision of the later point.

### 4. Do you know any good resources from which to learn?
As for the method, there are quite a lot of academic resources for this - google brings up loads. I think I linked in the ESRI training mats in the blog which are also useful.  In Alteryx, the resources are scarce. The Sample workflows are geared toward inclusion within a gravity model problem which makes them a bit confusing to really understand. I don't have Alteryx at work now (AHHHHH), so can't really do a sample workflow easily I'm afraid (though if I can get hold of a trial license for a bit I may be able to).  

A lot of the problems you might want to solve would involve a drivetime/public transport OD matrix, but I think you can fairly easily do a sample using straight line distance, which typically runs much quicker.  As I mentioned, the implementation is via a genetic algo, the basic idea being that it does a quick pass over as many of the candidate locations as possible choosing a subset to evaluate in more detail in the second pass. I think its deterministic if you set the seed, but I've not fully evaluated it - this part is very black box even if your optimization data and params are not!.

