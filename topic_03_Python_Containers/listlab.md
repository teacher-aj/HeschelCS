List Lab

Learning about Python lists
Inspired by: http://www.upriss.org.uk/python/session5.html

Goal

Learn the basic ins and outs of Python lists.

Reminder — getting input

To ask the user for input, use:

response = input("a prompt for the user > ")


The result will always be a string.

What to do

Open list_lab.py and write code to complete the four series of actions described below. Commit frequently. When finished, push to GitHub and submit your assignment.

Series 1

Create a list containing: ["Apples", "Pears", "Oranges", "Peaches"].

Display the list.

Ask the user for another fruit and add it to the end of the list.

Display the list.

Ask the user for a number and display the fruit corresponding to that number (use 1-based numbering for the user; adjust for Python’s 0-based indexing).

Add another fruit to the beginning of the list using the + operator and display the list.

Add another fruit to the beginning of the list using insert() and display the list.

Display all the fruits that begin with the letter P (use a for loop).

Series 2

Using the list created in Series 1:

Display the list.

Remove the last fruit from the list.

Display the list.

Ask the user for a fruit to delete; find it and delete it from the list.

Bonus: Multiply the list by 2 (so each item appears twice). Keep asking the user for a fruit to delete until they enter one that exists in the list. When found, delete all occurrences of that fruit.

Series 3

Using the list from Series 1 again:

For each fruit in the list, ask the user: Do you like apples? (use lowercase fruit name)

If the user answers no, delete that fruit from the list.

If the user answers anything other than yes or no, keep prompting until they answer one of those two.

When done, display the final list.

Series 4

Using the list from Series 1 again:

Create a copy of the list where each fruit string is reversed (for example Apples becomes selppA).

Delete the last item from the original list.

Display both lists: the modified original and the reversed-copy.
