# Redirection in Linux

Redirection is a powerful feature in Linux that allows you to control where the output of a command goes and where input is read from. This section will cover various forms of redirection, including output redirection to files, combining multiple files, and redirecting the output of commands to a file.

## 1. Viewing File Contents

Let's start by viewing the contents of a file.

### Example:

```bash
root@6406254312db:~# ls 
file.txt
root@6406254312db:~# cat file.txt 
Hello
World
```

- `ls`: Lists the files in the current directory. In this case, it shows `file.txt`.
- `cat file.txt`: Displays the contents of `file.txt`, which contains the text "Hello" and "World" on separate lines.

## 2. Basic Output Redirection

Output redirection allows you to redirect the output of a command to a file instead of displaying it on the screen.

### Redirecting Output to a New File

```bash
root@6406254312db:~# cat file.txt > filex.txt
root@6406254312db:~# ls
file.txt  filex.txt  
root@6406254312db:~# cat filex.txt 
Hello
World
```

- `cat file.txt > filex.txt`: Redirects the output of `cat file.txt` to a new file `filex.txt`. This command creates `filex.txt` and writes the contents of `file.txt` into it.
- `ls`: Shows that `filex.txt` has been created.
- `cat filex.txt`: Confirms that `filex.txt` contains the same content as `file.txt`.

### Combining Multiple Files

You can also combine the contents of multiple files into a single file.

```bash
root@6406254312db:~# cat file.txt filex.txt > combined.txt
root@6406254312db:~# ls
combined.txt  file.txt  filex.txt
root@6406254312db:~# cat combined.txt 
Hello 
World 

Hello
World
```

- `cat file.txt filex.txt > combined.txt`: Combines the contents of `file.txt` and `filex.txt` and writes them to a new file called `combined.txt`.
- `ls`: Shows that `combined.txt` has been created.
- `cat combined.txt`: Displays the contents of `combined.txt`, showing that it contains the combined content of `file.txt` and `filex.txt`.

## 3. Using `echo` with Redirection

The `echo` command prints text to the screen, but you can also redirect this output to a file.

### Example:

```bash
root@6406254312db:~# echo Hello
Hello
root@6406254312db:~# echo Hello > hello.txt
root@6406254312db:~# ls
combined.txt  file.txt  filex.txt  hello.txt
root@6406254312db:~# cat hello.txt 
Hello
```

- `echo Hello`: Prints "Hello" to the screen.
- `echo Hello > hello.txt`: Redirects the output to a file named `hello.txt`.
- `ls`: Shows that `hello.txt` has been created.
- `cat hello.txt`: Displays the content of `hello.txt`, which is "Hello".

## 4. Redirecting Command Output to a File

You can also redirect the output of various commands, such as `ls`, to a file.

### Example:

```bash
root@6406254312db:~# ls -l /etc/ > files.txt
root@6406254312db:~# ls
combined.txt  file.txt  files.txt  filex.txt  hello.txt
root@6406254312db:~# cat files.txt
```

- `ls -l /etc/ > files.txt`: Redirects the detailed listing of the `/etc/` directory to a file named `files.txt`.
- `ls`: Confirms that `files.txt` has been created.
- `cat files.txt`: Displays the content of `files.txt`, showing the detailed listing of files and directories within `/etc/`.

### Output Explanation

The output in `files.txt` might look like this:

```bash
total 300
drwxr-xr-x 1 root root    4096 Aug  6 09:01 alternatives
drwxr-xr-x 8 root root    4096 Jun  5 02:02 apt
-rw-r--r-- 1 root root    2319 Mar 31 08:41 bash.bashrc
...
```

This detailed listing includes information about the files and directories in `/etc/`, such as permissions, owner, size, and modification date.

## 5. Summary

In this section, you learned how to:

- Update your system using `apt update`.
- View the contents of files using `cat`.
- Redirect the output of commands to files using `>`.
- Combine the contents of multiple files into a single file.
- Use the `echo` command with redirection to create and populate files.
- Redirect the output of directory listings and other commands to files.

These redirection techniques are essential for efficiently managing files and output in Linux, allowing you to capture and manipulate command output as needed.

