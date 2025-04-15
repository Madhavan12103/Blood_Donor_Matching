# Blood Group WhatsApp Notifier

This project helps to automatically send WhatsApp messages to people matching a specific blood group and pin code using Python. It's useful for emergency blood donation alerts.

## Features

- Reads data from an Excel file (`blood_groups.xlsx`)
- Filters recipients based on pin code and blood group
- Automatically sends personalized WhatsApp messages using `pywhatkit`

## Tools & Libraries Used

- Python
- pandas
- pywhatkit
- Excel (.xlsx) as data source

## Sample Use Case

A hospital or NGO needs to find blood donors from a specific location with a specific blood group. Instead of manually calling each person, this script automates the message-sending process.

## File Structure

```
blood_groups.xlsx         # Input Excel file with dummy data
blood_groups_updated.xlsx # Output file with formatted phone numbers
blood_alert.py            # Python script
README.md                 # Project documentation
```

## How to Use

1. Clone the repository:

```bash
git clone https://github.com/your-username/blood-group-notifier.git
cd blood-group-notifier
```

2. Install required packages:

```bash
pip install pandas pywhatkit openpyxl
```

3. Update `blood_groups.xlsx` with real or dummy contact data. Sample columns:
   - `name`
   - `phone`
   - `pin`
   - `blood`

4. Run the script:

```bash
python blood_alert.py
```

5. Input the pin code and blood group when prompted. The script will send messages instantly to matched recipients on WhatsApp.

## Example Message

> "We found a potential match for your blood group. Please contact us if you are interested."

## Disclaimer

This project is for educational/demo purposes. Please ensure user consent before sending messages to real recipients.