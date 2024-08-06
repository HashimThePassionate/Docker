# Manipulating Files and Directories in Linux

This section will guide you through the basic operations of creating, moving, renaming, and deleting files and directories in Linux. We will cover commands like `mkdir`, `mv`, `touch`, and `rm`, with detailed explanations and examples.

## 1. Creating a Directory: `mkdir`

The `mkdir` command is used to create a new directory.

### Example:

```bash
root@6cc40d1065f9:/# cd ~
root@6cc40d1065f9:~# mkdir test
```

- `cd ~`: Changes the current directory to the home directory.
- `mkdir test`: Creates a new directory named `test` in the current location.

### Listing the Contents:

```bash
root@6cc40d1065f9:~# ls
test
```

After running `ls`, you can see the newly created `test` directory.

## 2. Moving and Renaming Directories: `mv`

The `mv` command is used to move or rename files and directories.

### Example:

```bash
root@6cc40d1065f9:~# mv test docker
```

- This command renames the `test` directory to `docker`.

### Verifying the Change:

```bash
root@6cc40d1065f9:~# ls
docker
```

The `test` directory has been renamed to `docker`.

## 3. Creating Files: `touch`

The `touch` command is used to create new, empty files.

### Creating a Single File:

```bash
root@6cc40d1065f9:~# cd docker/
root@6cc40d1065f9:~/docker# touch hello.txt
```

- `touch hello.txt`: Creates an empty file named `hello.txt` inside the `docker` directory.

### Verifying the File:

```bash
root@6cc40d1065f9:~/docker# ls
hello.txt
```

The `hello.txt` file is now listed in the directory.

### Creating Multiple Files:

```bash
root@6cc40d1065f9:~/docker# touch file1.txt file2.txt file3.txt
root@6cc40d1065f9:~/docker# ls
file1.txt  file2.txt  file3.txt  hello.txt
```

- `touch file1.txt file2.txt file3.txt`: Creates three new empty files: `file1.txt`, `file2.txt`, and `file3.txt`.

### Detailed Listing of Files: `ls -l`

```bash
root@6cc40d1065f9:~/docker# ls -l
total 0
-rw-r--r-- 1 root root 0 Aug  6 07:14 file1.txt
-rw-r--r-- 1 root root 0 Aug  6 07:14 file2.txt
-rw-r--r-- 1 root root 0 Aug  6 07:14 file3.txt
-rw-r--r-- 1 root root 0 Aug  6 07:13 hello.txt
```

- `ls -l`: Provides a detailed list of files, including file permissions, number of links, owner, group, file size, and modification date.

### Listing Files with One File per Line: `ls -1`

```bash
root@6cc40d1065f9:~/docker# ls -1
file1.txt
file2.txt
file3.txt
hello.txt
```

- `ls -1`: Lists each file on a new line.

## 4. Renaming Files: `mv`

The `mv` command can also be used to rename files.

### Example:

```bash
root@6cc40d1065f9:~/docker# mv hello.txt hello-docker.txt
root@6cc40d1065f9:~/docker# ls
file1.txt  file2.txt  file3.txt  hello-docker.txt
```

- `mv hello.txt hello-docker.txt`: Renames the file `hello.txt` to `hello-docker.txt`.

## 5. Deleting Files: `rm`

The `rm` command is used to delete files.

### Deleting Multiple Files:

```bash
root@6cc40d1065f9:~/docker# touch file4.txt file5.txt file6.txt
root@6cc40d1065f9:~/docker# ls
file1.txt  file2.txt  file3.txt  file4.txt  file5.txt  file6.txt  hello-docker.txt
root@6cc40d1065f9:~/docker# rm file4.txt file5.txt
root@6cc40d1065f9:~/docker# ls
file1.txt  file2.txt  file3.txt  file6.txt  hello-docker.txt
```

- `rm file4.txt file5.txt`: Deletes the files `file4.txt` and `file5.txt`.

### Deleting Files with Wildcards:

```bash
root@6cc40d1065f9:~/docker# rm file*
root@6cc40d1065f9:~/docker# ls
hello-docker.txt
```

- `rm file*`: Deletes all files that start with `file` (e.g., `file1.txt`, `file2.txt`, etc.).

### Deleting Directories: `rm -r`

The `rm -r` command is used to delete directories and their contents.

### Example:

```bash
root@6cc40d1065f9:~/docker# cd ..
root@6cc40d1065f9:~# rm -r docker/
root@6cc40d1065f9:~# ls
```

- `rm -r docker/`: Recursively deletes the `docker` directory and all its contents.

## 6. Summary

In this section, you learned how to:

- Create directories using `mkdir`.
- Move and rename directories and files using `mv`.
- Create files using `touch`.
- Delete files and directories using `rm` and `rm -r`.

These commands are essential for managing files and directories in a Linux environment, providing you with the tools to organize and maintain your file system efficiently.
