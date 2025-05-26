# MongoDB Setup Project

## Overview
This project provides a simple setup for using a local MongoDB server for development purposes. It includes scripts to help you verify that the MongoDB service is running and instructions on how to install MongoDB on your local machine.

## Project Structure
- `scripts/list-collections.sh`: A script to connect to the local MongoDB server and list the collections in the database.
- `instructions/INSTALL_MONGODB.md`: Detailed instructions on how to install a local MongoDB server.
- `package.json`: Configuration file for npm, listing dependencies and scripts.

## Getting Started

### Prerequisites
Before you begin, ensure you have the following installed:
- Node.js
- npm (Node Package Manager)

### Installation
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the necessary dependencies by running:
   ```
   npm install
   ```

### Running the Scripts
To verify that your MongoDB server is running, execute the following command in your terminal:
```
bash scripts/list-collections.sh
```

This will connect to your local MongoDB server and list the collections in the database.

## Additional Information
For detailed instructions on installing MongoDB, please refer to the `instructions/INSTALL_MONGODB.md` file. 

If you encounter any issues, please check the documentation or reach out for help.