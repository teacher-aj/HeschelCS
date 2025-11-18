# Mini Twitter Project 

This week you’re going to build a tiny, text-only version of Twitter.  
You’ll make accounts, write posts, see the feed, and like posts.  
Everything will be saved in Python using **dictionaries** and **lists**.

This project is meant to help you practice the basics: creating a dictionary, adding things into it, looping through a list, and updating values.

## What You Are Starting With

You will begin with three variables:

```
users = {}        # usernames will go here
posts = []        # every post you create gets added here
post_id = 1       # each post gets its own number
```

A **post** should look like:

```
{
    "id": 1,
    "user": "alex",
    "text": "Hello everyone!",
    "likes": 0
}
```

A **user** should look like:

```
{
    "bio": "your bio here",
    "followers": 0
}
```

## What You Need to Build

### Create a User
Write a function that asks the person for two things:  
– a username  
– a short bio  

Then make a dictionary with that information and store it inside `users` like this:

```
users["alex"] = {"bio": "hi", "followers": 0}
```

### Write a Post
Write a function that asks:  
– who is posting  
– what they want to say  

Then make a post dictionary, give it the next available `id`, and add it to the `posts` list.

### View the Feed
Write a function that loops through the `posts` list and prints each post so it looks neat.  
(Username, the text, and how many likes it has.)

### Like a Post
Ask the user for the post ID.  
Find that post in the list and increase its `"likes"` by 1.

### The Menu
Write a loop that keeps showing these choices until the person chooses Exit:

```
1. Create a user
2. Write a post
3. View the feed
4. Like a post
5. Exit
```

When the user types a number, call the matching function.

## Extra Challenge Ideas (Optional)

You only need one of these, but you can do more:

– search the feed for a word  
– count hashtags  
– let users edit their bio  
– let users delete their own posts  
– show the post with the most likes  

## What I’m Looking For

Your code should:  
– actually use dictionaries and lists  
– run without crashing  
– be organized into functions  
– be easy to read  
– include at least one extension  
– be tested before you turn it in  

## Hint to Get Started

Build it one step at a time.  
Start with just the “create a user” function, print `users` to check it works, and move on from there.
