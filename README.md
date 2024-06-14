# Lab 5 – Threads and Requests.

## Premise

There is a speed improvement when you use threads to download multiple
files as opposed to downloading the files sequentially.

## Description

This exercise consists of three parts: the first is to write a function
to download a single file, the second is to write code to download a set
of images sequentially and finally the third is to write code to
download the same set of images using threads. You will time both
downloads to decide if there is any advantage of using threads.

Please work in a new folder and make sure that you have enough space to
download about 115M of images so, you can delete the entire folder
afterwards.

You must use the following image URLs:

## Python Frameworks/Modules

-   **Requests:** This is an external framework that you would have
    needed to run the labs.

-   **Time:** This is an internal module that is a part of python
    standard distribution and does not require any separate
    installation.

-   **Threading:** This is also an internal module that is a part of
    python standard distribution and does not require any separate
    installation.

You may use the following pseudocode as a guide:

## Part A

1.  Create a function to take a single URL that does the following.

    a\) Use the request library to download the content (specified by the argument) as bytes. *[see **download_file.py**]*

    b\) Generate a name for the file based on the URL.[use the split method to extract the last part of the URL and add a suitable extension\]*

    c\) Write the contents of the URI to the above file name. *\[Again see **download_file.py**\]*

    d\) Print a suitable message.

## Part B

1.  Start timer. *\[import the time module* *use time.perf_counter() to get the current time.\]*

1.  Call the function in Part A with arguments from the above list
    sequentially (download one after the previous download is
    completed).

1.  End timer. *\[again use time.perf_counter() to get the current time.\]*

1.  Print elapse times. *\[subtract (1) from (2).\]*

## Part C

1.  Start timer.

1.  In a threaded fashion, call the function in Part A with an argument
    from the above list. *\[see **threading.py**\]*

1.  ![](media/image1.png)End timer.

1.  Print elapse times.

See the hints for Part B.

## Extra

1.  You will be graded on the quality of your code and also any
    improvements on the above pseudocode.

## *Submission*

1.  Your code file will be named «your_first_name».py.

2.  Must be uploaded to course dropbox before the deadline.

3.  See schedule for due date.