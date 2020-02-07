import os

# Running on Azure? If True will display the "Fork Me On GitHub" banner
AZURE = False

# Enable or disable Flask debug mode
DEBUG = True

# Google Analytics Code to monitor dashboard usage
GOOGLE_ANALYTICS = None

# Connection string to SSISDB
CONNECTION_STRING = {
    "main": os.getenv(
        "CONNECTION_STRING",
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=SSISDB;UID=;PWD="
    ),
}

# Set to 'NOW' to show current data or any valid date to show data for a fixed date only
AS_OF_DATE = 'NOW'

# Time range to display. Data will be shown from AS_OF_DATE - HOUR_SPAN value to AS_OF_DATE.
HOUR_SPAN = 360

# How many of the past executions should we show on the dashboard?
EXECUTION_COUNT=1000
