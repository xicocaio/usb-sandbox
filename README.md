# usb-sandbox
Simple project for experimenting with usb communication

## Stack

The stack bellow was used mostly due to its ease of installation, configuration, and also efficiency and portability.
* Language: Python (3.7.7)
* Core usb library: PyUSB (1.0)

## Pre-installation

This system was developed in Ubuntu 16.04 but will work properly on any other Operational System(OS X, Windows, etc.).

However, this guide will only include instructions for plugins and packages that are not already installed on this OS. For this reason, we assume that technologies like a python interpreter and pipenv are ready for use, and should not be on the scope of this document.

* Now install pipenv dependency manager:

```bash

$ pip install --user pipenv

```

## Project configuration

Now we'll start setting up the project.

* Clone the repo from GitHub and change to project root directory.
After that, install project dependencies and go to python virtual env, by running:

```bash
$ pipenv install
$ pipenv shell
```


## Running the project

Now we will run the project and get query answers.

* The project will do the following actions:
    1. Print information about specific usb device
    

To get information about Sennheiser earphones run:

```bash
$ python earphone
```

## Useful helpful commands for usage together with this project

Verbose output about usb connections.

```
$ dmesg -w
```

Information about connected usb devices.

```
$ watch -n 1 lsusb
```

## Knwon issues with specific owned earphone gear

   **Sennheiser HD 4.40 BT**
   - Earphone connects via usb, but just after doing a soft reset (down volume and power buttons, followed by three purple blinks)
   - Tested removing battery, and earphone still connects and is listed as one of usb devices
   - Not clear how this type of harware should react with usb control inputs from this code
   - Still unclear if issue with my owned earphone is hardware or software, but there are some indications that it is hardware, and probably concerning the battery as follows:
        - Removed battery but did not test its voltage to verify if it is fine
        - When pluging back battery one time, observed a single random red blink indication
        - Buttons do not work when plugged with the cable jack, but it is not clear if they should
