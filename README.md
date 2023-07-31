# Google Drive File Mover
# Google Drive File Downloader

## Description
This Python script allows you to download all files from your Google Drive into a local directory. The script uses the Google Drive API to authenticate with your Google account and obtain access to the necessary permissions. It then fetches the file metadata and downloads each file to your local machine.

## Prerequisites
- Python 3.x
- `google-api-python-client`, `google-auth-httplib2`, and `google-auth-oauthlib` libraries (can be installed using `pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib`)

## Setup
Step 1: Set up the Google Drive API
1. Go to the Google Developer Console: https://console.developers.google.com/
2. Click on "Select a project" at the top left corner and then click on "New Project."
3. Give your project a name and click "Create."
4. Once the project is created, click on "Enable APIs and Services."
5. Search for "Google Drive API" and click on it.
6. Click on the "Enable" button to enable the Google Drive API for your project.

Step 2: Create credentials for your project
1. In the Google Drive API dashboard, click on "Create Credentials."
2. Choose "OAuth client ID."
3. Select "Desktop app" as the application type.
4. Give your OAuth client ID a name (e.g., "Google Drive Downloader") and click "Create."
5. Click on "Download" to download the credentials in JSON format. Save the file as `credentials.json`.

Step 3: Install required Python packages
1. Open your terminal or command prompt.
2. Install the necessary Python packages by running the following command:
```python pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib```

## Usage
1. Create a new Python file (e.g., `download_google_drive.py`) and paste the provided code in it.
2. Place the `credentials.json` file in the same directory as your Python script.
3. Run the script by executing the following command in your terminal or command prompt:

Step 4: Creating python download_google_drive.py

## Authentication
1. After running the script, it will open a web browser to authenticate with your Google account.
2. Follow the on-screen instructions to grant permissions to the application.
3. Once authenticated, close the web browser.

## Downloading Files
1. The script will start downloading all the files from your Google Drive into a directory named `downloaded_files` in the same location as the script.
2. The script will display the names of the files as they are being downloaded.

## Completion
Once the script finishes, it will print "All files downloaded successfully." All your Google Drive files will be available in the `downloaded_files` directory.

## Note
Downloading all files from your Google Drive might take a long time, depending on the number and size of files you have. Ensure you have enough free disk space to accommodate all the downloaded files.


