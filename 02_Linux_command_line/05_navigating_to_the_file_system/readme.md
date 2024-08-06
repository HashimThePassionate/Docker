# Navigating the Linux File System

This section covers the basics of navigating the Linux file system using common commands like `pwd`, `ls`, and `cd`. Additionally, it explains the difference between absolute and relative paths, which are fundamental concepts for file system navigation in Linux.

## 1. Displaying the Current Directory: `pwd`

The `pwd` command stands for "print working directory." It displays the full path of the current directory you are in.

```bash
root@9cb804f3e19a:/# pwd
/
```

In this example, the output `/` indicates that the current directory is the root directory.

## 2. Listing Directory Contents: `ls`

The `ls` command is used to list the files and directories in the current directory. There are several options you can use with `ls` to modify its output.

### Basic `ls` Usage

```bash
root@9cb804f3e19a:/# ls
bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```

This command lists all the files and directories in the root directory (`/`). The output is a simple list of names.

### Listing One File per Line: `ls -1`

```bash
root@9cb804f3e19a:/# ls -1
bin  
boot 
dev  
etc  
home 
lib  
lib64
media
mnt  
opt  
proc 
root 
run
sbin
srv
sys
tmp
usr
var
```

The `-1` option forces `ls` to display each file or directory on a new line.

### Detailed Listing: `ls -l`

```bash
root@9cb804f3e19a:/# ls -l
total 48
lrwxrwxrwx   1 root root    7 Apr 22 13:08 bin -> usr/bin
drwxr-xr-x   2 root root 4096 Apr 22 13:08 boot
drwxr-xr-x   5 root root  360 Aug  6 06:42 dev
drwxr-xr-x   1 root root 4096 Aug  6 06:42 etc
drwxr-xr-x   3 root root 4096 Jun  5 02:06 home
lrwxrwxrwx   1 root root    7 Apr 22 13:08 lib -> usr/lib
lrwxrwxrwx   1 root root    9 Apr 22 13:08 lib64 -> usr/lib64
drwxr-xr-x   2 root root 4096 Jun  5 02:02 media
drwxr-xr-x   2 root root 4096 Jun  5 02:02 mnt
drwxr-xr-x   2 root root 4096 Jun  5 02:02 opt
dr-xr-xr-x 194 root root    0 Aug  6 06:42 proc
drwx------   2 root root 4096 Jun  5 02:05 root
drwxr-xr-x   4 root root 4096 Jun  5 02:06 run
lrwxrwxrwx   1 root root    8 Apr 22 13:08 sbin -> usr/sbin
drwxr-xr-x   2 root root 4096 Jun  5 02:02 srv
dr-xr-xr-x  11 root root    0 Aug  6 06:39 sys
drwxrwxrwt   2 root root 4096 Jun  5 02:05 tmp
drwxr-xr-x  12 root root 4096 Jun  5 02:02 usr
drwxr-xr-x  11 root root 4096 Jun  5 02:05 var
```

The `-l` option provides a detailed listing of files and directories, showing information like permissions, number of links, owner, group, size, and timestamp.

## 3. Moving Between Directories: `cd`

The `cd` command is used to change the current directory.

### Changing to a Specific Directory

```bash
root@9cb804f3e19a:/# cd etc/apt/
root@9cb804f3e19a:/etc/apt# ls
apt.conf.d  auth.conf.d  keyrings  preferences.d  sources.list  sources.list.d  trusted.gpg.d
```

Here, `cd etc/apt/` changes the current directory to `/etc/apt`, and the `ls` command lists the contents of this directory.

### Moving Up One Directory Level

```bash
root@9cb804f3e19a:/etc/apt# cd ../..
root@9cb804f3e19a:/# ls /bin
```

##  Understanding Absolute and Relative Paths

When navigating the file system, it's essential to understand the difference between absolute and relative paths.

### Absolute Path

An absolute path specifies the complete path to a file or directory from the root directory (`/`). It always starts with a forward slash (`/`).

For example:
```bash
root@9cb804f3e19a:/# cd /etc/apt/
```

In this command, `/etc/apt/` is an absolute path that points directly to the `apt` directory inside `/etc`, starting from the root directory (`/`).

### Relative Path

A relative path specifies a path relative to the current directory. It does not start with a forward slash (`/`).

For example:
```bash
root@9cb804f3e19a:/# cd etc/apt/
```

In this command, `etc/apt/` is a relative path. It tells the system to navigate to the `apt` directory located inside the `etc` directory from the current location. If your current directory was `/home/user`, using `cd etc/apt/` would not work unless the `etc/apt/` directory exists within `/home/user`.

### Examples in Context

- **Absolute Path Example:**
  ```bash
  root@9cb804f3e19a:/# cd /root
  ```
  Here, `/root` is an absolute path that directly specifies the root user's home directory.

- **Relative Path Example:**
  ```bash
  root@9cb804f3e19a:/# cd etc/apt/
  ```
  This command uses a relative path to navigate to `etc/apt/` from the current directory, which is the root directory (`/`).

The command `cd ../..` moves up two levels in the directory structure. The `ls /bin` command then lists the contents of the `/bin` directory.

### 4. Navigating to the Home Directory

```bash
root@9cb804f3e19a:/# cd /root
root@9cb804f3e19a:~# cd ..
root@9cb804f3e19a:/# cd ~
root@9cb804f3e19a:~# ls
```

- `cd /root` changes the directory to the root user's home directory.
- `cd ..` moves up one directory level.
- `cd ~` is a shortcut to return to the home directory.

The final `ls` command lists the contents of the home directory, though in this case, it is empty.

