import requests
import mysql.connector
from datetime import datetime

# Function to fetch data from the URL
def fetch_data():
    print("called")
    url = "https://12af-14-97-224-214.ngrok-free.app/index"
    response = requests.get(url)
    
    if response.status_code == 200:
        # Assuming the data is returned as JSON
        data = response.json()
        print(data)
        return data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

# Function to store data in the database
def store_data(data):
    try:
        # Replace with your own database credentials
        conn = mysql.connector.connect(
            host='localhost',
            user='sqlalchemy_user@localhost',
            password='root',
            database='marlo'
        )
        cursor = conn.cursor()

        # Assuming data is a dictionary with keys 'field1', 'field2', etc.
        insert_query = """
                   INSERT INTO marlo.data (data_id, name, group_name, date, value) 
                   VALUES (%s, %s, %s, %s, %s) """
        #repare data tuples for insertion
        # Prepare data tuples for insertion
        values = []
        for item in data:
            try:
                # Convert date string to a format that MySQL accepts if necessary
                date_value = item['date']  # Assuming the date format is already compatible
                value_tuple = (item['id'], item['name'], item['group'], date_value, item['value'])
                values.append(value_tuple)
            except KeyError as e:
                print(f"Missing key in data item: {e}")

        # Debug print to verify the structure of the values list
        print("Values to be inserted:", values)

        # Execute the query
        try:
            cursor.executemany(insert_query, values)
            conn.commit()
            print("Data inserted successfully.")
        except mysql.connector.Error as err:
            print("Error: ", err)

        # Close the connection
        cursor.close()
        conn.close()
    except TypeError as e:
        print(f"Type error in data item: {e}")


# Main execution
if __name__ == "__main__":
    data = fetch_data()
    if data:
        store_data(data)

