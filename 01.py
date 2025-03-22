import pandas

data = pandas.read_csv("/Users/alisultan/Desktop/python/State_Guessing_Game/squirrel_data_2018.csv")

#we have to make two columns, one for the three primary colors, and one for the numnber of those squirerels


#count and print the each color of squirrels from the Primary Fur Color Column

squirrels = data["Primary Fur Color"]


len_of_gray = len(squirrels[squirrels == "Gray"])
len_of_cinnamon = len(squirrels[squirrels == "Cinnamon"])
len_of_red = len(squirrels[squirrels == "Black"])

data_dict = len_of_gray, len_of_cinnamon, len_of_red
print(data_dict)

#now we have to show them in a csv format
#we have to make a dictionary for the squirrel colors and their counts
squirrel_data = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [len_of_gray, len_of_cinnamon, len_of_red]
}


data = pandas.DataFrame(squirrel_data)
data.to_csv("State_Guessing_Game/squirrel_count.csv")