# Managing Packages in Ubuntu

##  What is APT?
APT, short for Advanced Package Tool, is a command-line utility for managing software packages on Debian-based Linux distributions such as Ubuntu. It simplifies the process of installing, upgrading, and removing software by handling dependencies intelligently.

### Key Features:**
-   **Dependency Resolution:** APT automatically resolves dependencies when installing or removing packages, ensuring that all required libraries and components are installed correctly.
-   **Package Management:** It provides a simple interface for installing, upgrading, and removing packages, making it easy to manage software on your system.
-   **Repository Support:** APT works with software repositories, allowing you to easily add, remove, or update repositories to access a wide range of software packages.
-   **Command-Line Interface:** APT can be used via the command-line interface (CLI), making it suitable for both novice and experienced users who prefer text-based interactions.

##  To interact with apt type on terminal
```bash
    apt
```
<img src="" alt="apt" width="100%">

## Now lets simple install nano text editor with apt
```bash
    apt install nano
```
<img src="" alt="nano" width="100%">

You will get this error but why??

## First we check all the packages in database directory
```bash
apt list 
```
<img src="" alt="error" width="100%">

when we run this command apt install nano apt will look to their database if it is not available than it can simply run exception,Look we cannot find nano package in list, so what should we do?
Simple tell apt to update packages database list directories and then install again

## Updating packages
```bash
    apt update
```
<img src="" alt="update" width="100%">

## Reinstall nano through apt
```bash
    apt install nano
```
<img src="" alt="Installing Nano" width="100%">

## Now to remove nano 
```bash
    apt remove nano
```


