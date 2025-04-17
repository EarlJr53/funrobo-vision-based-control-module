# Module 3: Vision-based Control

This repository accompanies the class activities in module 3 with a focus on helping you learn the following:
1. Basics of digital image representation
2. Basic digital image manipulation and processing
3. Object detection in images
4. Camera calibration
5. Visual servoing techniques

These activities will be performed using Jupyter Notebooks.

## Setting up your PC

- You can complete this assignment on any computer OS: Mac, Windows, Linux, etc. All you need is Python 3 interpreter (code was tested using Python 3.10).

#### Step 0 (Optional): Install VScode
- Install Visual Studio Code (I strongly recommend using this, if you don’t already do. It’s the best IDE in my humble opinion)
- Follow the instructions [here to install.](https://code.visualstudio.com/download)



#### Step 1: Install Python 3 (if not already installed)
- First, check if you have Python3, to do that, open your terminal and type:
```bash
$ python3 --version     # <--- type this
Python 3.10.12          # <--- you should see something like this
```
- If you don’t have Python installed, follow this [tutorial here](https://realpython.com/installing-python/) to install it.


#### Step 2: Create a virtual environment
- This is technically optional, but I strongly recommend that you create a new python virtual environment for this course.
- Follow this [tutorial here](https://docs.python.org/3/tutorial/venv.html).


#### Step 3: Get this repository from Github
- I recommend you fork this repository to the account of one of your teammates and then you all can clone from the forked version.
- Follow [this tutorial](https://ftc-docs.firstinspires.org/en/latest/programming_resources/tutorial_specific/android_studio/fork_and_clone_github_repository/Fork-and-Clone-From-GitHub.html) to understand how to fork and clone repositories


#### Step 4: Install all required Python packages
```bash
# first: make sure you have activated the virtual environment (if you used one). See step 2 tutorial

# cd to the project folder
$ cd vision-based-control-module

# install all required packages from requirements.txt
$ pip install -r requirements.txt
```


### How to Run

- If setup worked well, you should be able to open the **lesson1.ipynb** in VS Code and start working!

- When returning to work on lesson2, please make sure you run step 4 again as new packages have been added. If the setup worked well, you should be able to open the **lesson2.ipynb** in VS Code and start working!


N.B. Please make sure you select the python interpreter associated with the virtual environment you just created when running the Jupyter notebook.