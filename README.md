# Automated WhatsApp Message Scheduler

## Overview  
This project automates the sending of WhatsApp messages on a predefined schedule using **Twilio API** and **Google Cloud VM**.  
It ensures that messages are sent at the correct time every week, with scheduling logic based on **Google Sheets data**.  

## Features  
- **Automated Message Scheduling**: Sends WhatsApp messages at **11 PM every Wednesday and Thursday**.  
- **Google Sheets Integration**: Fetches recipient data dynamically.  
- **24/7 Uptime**: Runs continuously on **Google Cloud Console** using `systemd`.  
- **Error Handling**: Service restarts automatically if it crashes.  

## Technologies Used  
- **Python** (for scheduling and message sending)  
- **Google Apps Script** (to fetch data from Google Sheets)  
- **Twilio API** (for WhatsApp messaging)  
- **Google Cloud VM** (for hosting the script)  
- **Systemd** (for managing the service)  

## Project Structure  
