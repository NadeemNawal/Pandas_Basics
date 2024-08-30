import pandas

data = pandas.read_csv("weather_data.csv")   #reads data in columns and rows
print(data)

data_dict = data.to_dict()
#to make dictionary of data JSON format
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)


#getting mean temperature regular code
list_len = len(temp_list)
average = sum(temp_list)/(list_len)
print(average)


#getting mean temperature with pandas
print(data["temp"].mean())

#getting max temperature with pandas
print(data["temp"].max())

#get data from a specific column

print(data["condition"])



# get data in a row: use keyword of row
print(data[data.day=="Monday"])

print(data[data.temp==data.temp.max()])

# read pandas documentation

# getting a specific value from a row
Monday = (data[data.day=="Monday"])
print(Monday.condition)


# converting temperature to celcius

monday_temp  = Monday.temp[0]
monday_temp_f = monday_temp*9/5 + 32
print(monday_temp_f)


# Data set= data frame, data column in set = Data Series
# to turn a dictionary into a data frame
data_dict = {
    "students" : ["Amy", "James", "Max", "Cindy"],
    "scores": [76, 56, 65, 45]
}

data_frame = pandas.DataFrame(data_dict)
print(data_frame)

data_frame.to_csv("new_data.csv")  # to create a csv file with data
