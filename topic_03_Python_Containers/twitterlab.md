# Mini Twitter Project

This project will be completed this week to practice what we have learned about python contrainers (lists and dictionaries). 

## Overview

In this project you everyone will build a small, bare bones text-based version of Twitter.
You will create users, write posts, view a feed, and like posts.
Everything will be stored using Python dictionaries and lists.

Your goal is to practice creating, accessing, updating, and looping
through dictionaries.

## What You Will Build

Your mini Twitter will include:

1.  A dictionary of users\
2.  A list of posts\
3.  Functions to create accounts, write posts, view the feed, and like
    posts\
4.  A menu system for user actions

## Starter Code

    users = {}            # username -> user info
    posts = []            # list of post dictionaries
    post_id = 1           # numbering posts for easy reference

A post will look like this:

    {
        "id": 1,
        "user": "alex",
        "text": "Hello everyone!",
        "likes": 0
    }

A user will look like this:

    {
        "bio": "your bio here",
        "followers": 0
    }

## Required Features

### 1. Create a User

Write a function that asks for a username and a bio. Store the
information in the `users` dictionary.

### 2. Write a Post

Write a function that asks for a username and the text of the post.
Create a new post dictionary and add it to the `posts` list.

### 3. View the Feed

Loop through the `posts` list and print each post in a readable format.

### 4. Like a Post

Ask for a post ID and increase the like count on that post.

### 5. Main Menu

Create a loop that shows this menu:

    1. Create a user
    2. Write a post
    3. View the feed
    4. Like a post
    5. Exit

The menu should repeat until the user chooses Exit.

## Extension Challenges

Choose at least one for extra credit:

1.  Search the feed for a keyword\
2.  Count how many times each hashtag appears\
3.  Let users edit their bio\
4.  Let users delete their own posts\
5.  Show the most popular post in the feed

## Grading Checklist

-   Uses dictionaries correctly\
-   Uses lists correctly\
-   Functions work without errors\
-   Code is readable and well organized\
-   At least one extension is completed\
-   Code is tested before submission

## Tips

-   Use functions to keep code organized\
-   Test each feature as you write it\
-   Print dictionaries while debugging\
-   Keep printed output clean and simple
