import pywhatkit
import pandas as pd
# Load the Excel sheet into a Pandas
df = pd.read_excel('blood_groups.xlsx')
# Define a function to add '+91' before a phone number
df['phone'] = '+91' + df['phone'].astype(str)
# Load the edited Excel sheet into a Pandas
df.to_excel('blood_groups_updated.xlsx', index=False)
# Ask the user for a pin code to search
pin_code = input('Enter the pin code you want to search for: ')
# Ask the user for a blood group to search
blood_group = input("What blood group do you want to search for? ")
# Filter the dataframe based on user input
filter_df = df[(df['pin'].astype(str) == pin_code) & (df['blood'] == blood_group)]

# Loop through the filtered dataframe and send a message to each recipient
for index, row in filter_df.iterrows(): 
    recipient_number = row['phone']
    message = "we found a potential match for your blood group. Please contact us if you are interested." 
    pywhatkit.sendwhatmsg_instantly(recipient_number, message)
print(f"Sent messages to {len(filter_df)} recipients.")