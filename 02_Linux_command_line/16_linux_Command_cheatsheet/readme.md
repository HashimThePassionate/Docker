### **Linux Command Line Cheat Sheet**

---

#### **🚀 Managing Packages**
- **Update package list:**  
  ```bash
  apt update
  ```
  *# Refreshes the list of available packages and their versions.*

- **List installed packages:**  
  ```bash
  apt list
  ```
  *# Displays a list of all installed packages.*

- **Install a package:**  
  ```bash
  apt install nano
  ```
  *# Installs the 'nano' text editor package.*

- **Remove a package:**  
  ```bash
  apt remove nano
  ```
  *# Uninstalls the 'nano' text editor package.*

---

#### **📂 Navigating the File System**
- **Print working directory:**  
  ```bash
  pwd
  ```
  *# Displays the current directory path.*

- **List files and directories:**  
  ```bash
  ls
  ```
  *# Shows the files and directories in the current directory.*

- **List with detailed information:**  
  ```bash
  ls -l
  ```
  *# Displays files and directories with details like permissions, owner, size, and modification date.*

- **Go to the root directory:**  
  ```bash
  cd /
  ```
  *# Changes the current directory to the root directory.*

- **Go to the bin directory:**  
  ```bash
  cd bin
  ```
  *# Changes the current directory to the 'bin' directory.*

- **Go one level up:**  
  ```bash
  cd ..
  ```
  *# Moves up one directory level.*

- **Go to the home directory:**  
  ```bash
  cd ~
  ```
  *# Changes the current directory to the user's home directory.*

---

#### **🛠️ Manipulating Files and Directories**
- **Create a directory:**  
  ```bash
  mkdir test
  ```
  *# Creates a new directory named 'test'.*

- **Rename a directory:**  
  ```bash
  mv test docker
  ```
  *# Renames the 'test' directory to 'docker'.*

- **Create a file:**  
  ```bash
  touch file.txt
  ```
  *# Creates an empty file named 'file.txt'.*

- **Rename a file:**  
  ```bash
  mv file.txt hello.txt
  ```
  *# Renames 'file.txt' to 'hello.txt'.*

- **Remove a file:**  
  ```bash
  rm hello.txt
  ```
  *# Deletes the file 'hello.txt'.*

- **Recursively remove a directory:**  
  ```bash
  rm -r docker
  ```
  *# Deletes the 'docker' directory and its contents.*

---

#### **📝 Editing and Viewing Files**
- **Edit a file:**  
  ```bash
  nano file.txt
  ```
  *# Opens 'file.txt' in the Nano text editor.*

- **View file contents:**  
  ```bash
  cat file.txt
  ```
  *# Displays the entire content of 'file.txt'.*

- **View file with scrolling:**  
  ```bash
  less file.txt
  ```
  *# Opens 'file.txt' with the ability to scroll through the content.*

- **View the first 10 lines:**  
  ```bash
  head file.txt
  ```
  *# Shows the first 10 lines of 'file.txt'.*

- **View the first 5 lines:**  
  ```bash
  head -n 5 file.txt
  ```
  *# Shows the first 5 lines of 'file.txt'.*

- **View the last 10 lines:**  
  ```bash
  tail file.txt
  ```
  *# Displays the last 10 lines of 'file.txt'.*

- **View the last 5 lines:**  
  ```bash
  tail -n 5 file.txt
  ```
  *# Displays the last 5 lines of 'file.txt'.*

---

#### **🔍 Searching for Text**
- **Search for text in a file:**  
  ```bash
  grep hello file.txt
  ```
  *# Searches for the word 'hello' in 'file.txt'.*

- **Case-insensitive search:**  
  ```bash
  grep -i hello file.txt
  ```
  *# Searches for 'hello' in 'file.txt', ignoring case.*

- **Search in files with a pattern:**  
  ```bash
  grep -i hello file*.txt
  ```
  *# Searches for 'hello' in all files that match the pattern 'file*.txt'.*

- **Search in the current directory:**  
  ```bash
  grep -i -r hello .
  ```
  *# Recursively searches for 'hello' in all files within the current directory.*

---

#### **🗂️ Finding Files and Directories**
- **List all files and directories:**  
  ```bash
  find
  ```
  *# Lists all files and directories starting from the current directory.*

- **List directories only:**  
  ```bash
  find -type d
  ```
  *# Filters the list to show directories only.*

- **List files only:**  
  ```bash
  find -type f
  ```
  *# Filters the list to show files only.*

- **Filter by name using a pattern:**  
  ```bash
  find -name "f*"
  ```
  *# Finds all files and directories that match the pattern 'f*'.*

---

#### **🌐 Managing Environment Variables**
- **List all variables and their values:**  
  ```bash
  printenv
  ```
  *# Displays all environment variables and their values.*

- **View the value of PATH:**  
  ```bash
  printenv PATH
  ```
  *# Shows the value of the PATH environment variable.*

- **View the value of PATH using echo:**  
  ```bash
  echo $PATH
  ```
  *# Another way to display the value of the PATH environment variable.*

- **Set a variable in the current session:**  
  ```bash
  export name=bob
  ```
  *# Sets a new environment variable 'name' with the value 'bob' for the current session.*

---

#### **🔧 Managing Processes**
- **List running processes:**  
  ```bash
  ps
  ```
  *# Displays a snapshot of the current running processes.*

- **Kill a process by ID:**  
  ```bash
  kill 37
  ```
  *# Terminates the process with ID 37.*

---

#### **👥 Managing Users and Groups**
- **Create a user with a home directory:**  
  ```bash
  useradd -m john
  ```
  *# Creates a new user 'john' with a home directory.*

- **Add a user interactively:**  
  ```bash
  adduser john
  ```
  *# Interactively creates a new user 'john'.*

- **Modify a user:**  
  ```bash
  usermod
  ```
  *# Modifies a user's account (requires additional options).*

- **Delete a user:**  
  ```bash
  userdel
  ```
  *# Deletes a user's account.*

- **Create a group:**  
  ```bash
  groupadd devs
  ```
  *# Creates a new group named 'devs'.*

- **View groups for a user:**  
  ```bash
  groups john
  ```
  *# Lists all groups that user 'john' belongs to.*

- **Modify a group:**  
  ```bash
  groupmod
  ```
  *# Modifies a group (requires additional options).*

- **Delete a group:**  
  ```bash
  groupdel
  ```
  *# Deletes a group.*

---

#### **🔐 File Permissions**
- **Give the owning user execute permission:**  
  ```bash
  chmod u+x deploy.sh
  ```
  *# Adds execute permission for the file owner.*

- **Give the owning group execute permission:**  
  ```bash
  chmod g+x deploy.sh
  ```
  *# Adds execute permission for the group.*

- **Give everyone else execute permission:**  
  ```bash
  chmod o+x deploy.sh
  ```
  *# Adds execute permission for others.*

- **Give the owning user and group execute permission:**  
  ```bash
  chmod ug+x deploy.sh
  ```
  *# Adds execute permission for the owner and group.*

- **Remove execute permission from owning user and group:**  
  ```bash
  chmod ug-x deploy.sh
  ```
  *# Removes execute permission from the owner and group.*

