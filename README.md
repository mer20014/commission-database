# Overview

This program was made to track commission information and store it
into a cloud database. It can modify important information as needed,
and tracks the name of the customer, the type of commission, how
much it costs, how much they've paid, what they want for the
commission, and if it has been completed.

[Software Demo Video](https://youtu.be/yZHJlgb4kis)

# Cloud Database

For the program, I used Firebase for storing my data. It starts with
the Commission collection, which moves into the documents that host
a cusomters name, and then each field has the other imformation
that is unique to each customer

# Development Environment

* Visual Studio Code 1.72
* Python 3.8.5
* Cloud Firestore through Firebase

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Cloud Database Workshop](https://byui-cse.github.io/cse310-course/workshops/Cloud_DB/CSE310_Workshop_Cloud_DB.pdf)
* [Official Firebase Tutorial](https://firebase.google.com/docs/firestore)

# Future Work

* Impliment option 2 and 3 in search function
* Fix bug that causes JSON file to not be found when in folders
* Simplify UI