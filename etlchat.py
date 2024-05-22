import pandas as pd

# Initialize empty lists to store person and message data
persons = []
messages = []

# Open the text file and read its contents line by line
with open('_chat.txt', 'r', encoding='utf-8') as file:
    for line in file:
        # Split each line by "] " to separate date/time from the rest of the message
        parts = line.strip().split("] ", 1)
        if len(parts) == 2:
            _, rest = parts
            # Split the rest of the line by the colon to separate person and message
            sub_parts = rest.split(': ', 1)
            if len(sub_parts) == 2:
                person, message = sub_parts
                persons.append(person)
                messages.append(message)

# Create a pandas DataFrame from the lists
df = pd.DataFrame({'Person': persons, 'Message': messages})

# Display the DataFrame
print(df)
