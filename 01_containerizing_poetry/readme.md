# Getting Started with Docker
1. Create a file Dockerfile inside in your project and Write
```docker
FROM python:alpine3.10
COPY . /app
WORKDIR /app
RUN pip install poetry \
&& poetry config virtualenvs.create false\
&& poetry install
CMD ["poetry", "run", "uvicorn", "test_poetry.main:app","--host","0.0.0.0","--port","8000"]
``` 
2. FROM python (means find python from docker hub and download)
3. COPY ./app (means copy everything from current dir and paste it to app directory)
4. WORKDIR /app (means we are already in working directory which is /app)
5. CMD pip install poetry  (means run pip install python)
6. poetry config virtualenvs.create false (tell explicity poetry not to create virtual environment as we already in docker isolated environment)
7. poetry install (finally poetry install all the required packages)
8. CMD ["poetry", "run", "uvicorn", "test_poetry.main:app","--host","0.0.0.0","--port","8000"] (simple with this command we can start a server)

# Now we need to build docker file but with dev container 
1. install dev container extension in vs code extension section
2. After install Extension click on remote explorer 
3. Click on open current folder in container
4. Add configuration to workplace
5. Select From Docker file
6. It will build image and run container in remote server and your vs code will be open to remote server
7. to move back to local simple click on dev_container under your project folder right click on local 

# Advantages of Dev Containers in VS Code

Development Containers (Dev Containers) are a feature in Visual Studio Code (VS Code) that allow developers to create consistent and reproducible development environments. These environments are defined using container technology, typically Docker, and can be shared across different machines, teams, or projects. This README outlines the key advantages of using Dev Containers in VS Code.

## 1. Consistent Development Environments
Dev Containers ensure that the development environment is consistent across different machines and platforms. By defining the environment in a Dockerfile or `devcontainer.json`, you eliminate the "it works on my machine" problem. This consistency helps developers collaborate more effectively, reducing issues related to differences in development setups.

## 2. Reproducibility
With Dev Containers, the entire development environment can be reproduced from scratch with a single command. This reproducibility is crucial when setting up new developer machines, onboarding new team members, or switching between projects. It also aids in maintaining stable development environments across multiple development cycles.

## 3. Simplified Onboarding
Dev Containers simplify the onboarding process for new developers. Instead of manually installing dependencies, configuring environments, and resolving version conflicts, new team members can simply open a project in VS Code and let the Dev Container do the work. This speeds up the onboarding process and reduces the potential for setup errors.

## 4. Isolation and Cleanliness
Dev Containers offer an isolated environment for each project. This isolation prevents conflicts between different projects and ensures a clean development setup. Developers can work on multiple projects simultaneously without worrying about interfering dependencies or configurations.

## 5. Portability
Dev Containers are portable across different platforms and cloud environments. This portability allows developers to work on a project locally and then deploy it to a cloud-based environment without modifying the development setup. It also facilitates cross-platform development and testing.

## 6. Consistent Tooling
Using Dev Containers, developers can ensure that the same tools, libraries, and versions are used across the entire team. This consistency in tooling reduces compatibility issues and ensures that code can be built and tested reliably.

## 7. Improved Collaboration
Dev Containers improve collaboration among developers and teams. Since the environment is defined in code, it can be version-controlled, shared, and reviewed just like any other piece of code. This approach allows teams to collaborate on environment setups, making it easier to share best practices and troubleshoot issues.

## 8. Integration with CI/CD Pipelines
Dev Containers can be integrated with Continuous Integration and Continuous Deployment (CI/CD) pipelines. This integration allows developers to test code in a consistent environment during the CI/CD process, ensuring that build and test results are reliable. It also enables the use of the same container environment for both development and deployment, reducing discrepancies between development and production.

## Conclusion
Dev Containers in VS Code provide a range of advantages, including consistent environments, reproducibility, simplified onboarding, isolation, portability, consistent tooling, improved collaboration, and integration with CI/CD pipelines. By adopting Dev Containers, developers and teams can improve productivity, collaboration, and reliability in their development processes.
