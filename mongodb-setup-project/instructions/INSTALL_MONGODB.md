# INSTALL_MONGODB.md

# Installation Instructions for MongoDB

This document provides step-by-step instructions to install a local MongoDB server for development purposes.

## Prerequisites

Before you begin, ensure you have the following:

- A compatible operating system (Windows, macOS, or Linux).
- Administrative privileges on your machine.
- Basic knowledge of command line usage.

## Step 1: Download MongoDB

1. Go to the [MongoDB Download Center](https://www.mongodb.com/try/download/community).
2. Select your operating system.
3. Choose the version you want to install (the latest stable version is recommended).
4. Click on the "Download" button.

## Step 2: Install MongoDB

### For Windows:

1. Run the downloaded `.msi` installer.
2. Follow the installation prompts.
3. Choose "Complete" when prompted for the setup type.
4. Ensure that "Install MongoDB as a Service" is checked.
5. Click "Finish" to complete the installation.

### For macOS:

1. Open the Terminal.
2. Use Homebrew to install MongoDB by running the following command:
   ```
   brew tap mongodb/brew
   brew install mongodb-community
   ```

### For Linux:

1. Open the terminal.
2. Import the public key used by the package management system:
   ```
   wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
   ```
3. Create a list file for MongoDB:
   ```
   echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/multiverse amd64 mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
   ```
4. Reload the local package database:
   ```
   sudo apt-get update
   ```
5. Install the MongoDB packages:
   ```
   sudo apt-get install -y mongodb-org
   ```

## Step 3: Start MongoDB

- **Windows**: MongoDB should start automatically as a service. If not, you can start it manually from the Services application.
- **macOS/Linux**: Start MongoDB by running the following command in the terminal:
  ```
  brew services start mongodb/brew/mongodb-community
  ```
  or
  ```
  sudo systemctl start mongod
  ```

## Step 4: Verify the Installation

To verify that MongoDB is running, open a terminal or command prompt and run the following command:

```
mongo
```

If you see the MongoDB shell prompt, the installation was successful.

## Step 5: List Collections

To list the collections in your MongoDB database, run the following command:

```
sh scripts/list-collections.sh
```

This will connect to your local MongoDB server and display the collections, confirming that the service is active and working.