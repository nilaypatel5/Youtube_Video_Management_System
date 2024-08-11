```markdown
# YouTube Video Manager

This project is a command-line tool developed in Python that allows users to manage YouTube video records using a MySQL database. The tool supports adding, viewing, updating, and deleting video records.

## Features

- Add a new YouTube video record.
- View all YouTube video records.
- Update existing video records.
- Delete video records.
- Connects to a MySQL database using `mysql-connector-python`.

## Requirements

- Python 
- MySQL (via XAMPP or other server)
- `mysql-connector-python` package

## Setup Instructions


### 1. Install the Required Python Packages

Ensure you have Python installed on your system. Then, install the necessary Python package (`mysql-connector-python`) by running:

```bash
pip install mysql-connector-python
```

### 2. Set Up the MySQL Database

1. **Start XAMPP**:
   - Open XAMPP and start the MySQL server.

2. **Create the Database**:
   - Open phpMyAdmin in your web browser (typically `http://localhost/phpmyadmin`).
   - Create a new database named `youtube_manager`.

3. **Import the Database Schema**:
   - In phpMyAdmin, select the `youtube_manager` database.
   - Click on the **Import** tab.
   - Choose the `youtube_manager_db.sql` file (included in this repository) and click **Go** to import the database schema.

### 3. Running the Application

With the database set up, you can now run the Python script to use the YouTube Video Manager.

```bash
python main.py
```

### 4. Using the Application

The application will present you with a menu:

- **1. List all videos**: Display all video records in the database.
- **2. Add a YouTube video**: Add a new video record by entering the video name and time.
- **3. Update a YouTube video**: Update the details of an existing video record by entering its ID.
- **4. Delete a YouTube video**: Delete a video record by entering its ID.
- **5. Exit**: Exit the application.


## Database Schema
Database Name - `youtube_manager`

The MySQL database contains a single table:

- **videos**
  - `id` (INT) - Auto-incremented primary key.
  - `name` (VARCHAR) - The name of the YouTube video.
  - `time` (VARCHAR) - The time duration of the video.


