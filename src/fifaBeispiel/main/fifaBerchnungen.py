"""
I took the rough structure of the file from the example in the lecture and adapted it to my needs.
Additionally I used the following sources to find out how to use the functions:
PySpark Functions https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/functions.html"""


# This function is called from the main.py file
def runSpark():
    # Importiere die SparkSession aus pyspark.sql
    from pyspark.sql import SparkSession

    # Create a SparkSession and name it fifacalculations and save it in the variable spark
    spark = SparkSession.builder \
        .appName("fifacalculations") \
        .getOrCreate()

    # Read input data from the fifa dataset (data/clean_fifa_worldcup_matches.csv)
    fifa_file = spark.read.csv("../../data/clean_fifa_worldcup_matches.csv", header=True, sep=",")

    # Test if the data is read correctly. Is not necessary for the calculations but good for debugging
    # fifa_file.show()

    """
        Now that the csv file is read, we can start with the calculations
        First we want to calculate, which team/nation has won the most games at home
        For this we need to filter the data for the home team and then count the wins
        The result is then sorted in descending order and the first entry is printed
    """

    # Filter the data for the home team. If the HomeTeam has exactly more goals than the AwayTeam, the HomeTeam has won
    # Then we can add the game to the home_wins dataframe
    home_wins = fifa_file.filter(fifa_file["HomeGoals"] > fifa_file["AwayGoals"])

    # Now that we have all the winning home teams, we can group them by their name and count the wins
    home_wins = home_wins.groupBy("HomeTeam").count()

    # Now we have to sort the data in descending order, so that the team with the most wins is at the top
    home_wins = home_wins.sort("count", ascending=False)

    # Print the first 3 entries of the dataframe
    print("The team with the most home wins is: ")
    home_wins.show(3)

    """
        Now we want to calculate, which team/nation has won the most games away
        For this we need to filter the data for the away team and then count the wins
        The result is then sorted in descending order and the first entry is printed
        It is the same procedure as for the home wins calculation
    """

    # Filter the data for the away team. If the AwayTeam has exactly more goals than the HomeTeam, the AwayTeam has won
    # Then we can add the game to the away_wins dataframe
    away_wins = fifa_file.filter(fifa_file["AwayGoals"] > fifa_file["HomeGoals"])

    # Now that we have all the winning away teams, we can group them by their name and count the wins
    away_wins = away_wins.groupBy("AwayTeam").count()

    # Now we have to sort the data in descending order, so that the team with the most wins is at the top
    away_wins = away_wins.sort("count", ascending=False)

    # Print the first 3 entries of the dataframe
    print("The team with the most away wins is: ")
    away_wins.show(3)

    """
    The next task is to find out the most successful team/nation of the last 10 years
    For this task we need to find out which team/nation has won the most games in the last 10 years
    For this we need to filter the data for the last 10 years and then count the wins    
    """

    # The dataset is from 2022, so we can filter the data for the last 10 years by filtering for the year > 2011
    mostsuccessful = fifa_file.filter(fifa_file["Year"] > 2011)
    # Delete all the games which ended in a draw
    mostsuccessful = mostsuccessful.filter(mostsuccessful["HomeGoals"] != mostsuccessful["AwayGoals"])

    # Now we need a new columns to determine the winner of the game
    # We can use the when function to create a new column with the winner of the game. When function is imported from pyspark.sql.functions
    from pyspark.sql.functions import when
    mostsuccessful = mostsuccessful.withColumn("Winner", when(mostsuccessful["HomeGoals"] > mostsuccessful["AwayGoals"],
                                                              mostsuccessful["HomeTeam"]).otherwise(
        mostsuccessful["AwayTeam"]))

    # Now we can group the data by the winner and count the wins
    mostsuccessful = mostsuccessful.groupBy("Winner").count()

    # Sort the data in descending order
    mostsuccessful = mostsuccessful.sort("count", ascending=False)

    # Print the first 3 entries of mostsuccessful
    print("The most successful team of the last 10 years is: ")
    mostsuccessful.show(3)

    """ 
    As requested in the task, the results should be saved. For this we have to write the data to a file
    For this we can use the write function from Spark and write it to the folder data/output.
    The data is saved as a csv file and the data is overwritten if the file already exists.
    We do this for all 3 dataframes.
    """

    mostsuccessful.write \
        .mode("overwrite") \
        .csv("../../data/fifa_results_mostsuccessful.csv")

    home_wins.write \
        .mode("overwrite") \
        .csv("../../data/fifa_results_homewins.csv")

    away_wins.write \
        .mode("overwrite") \
        .csv("../../data/fifa_results_awaywins.csv")

    # End the SparkSession, so that the program can be closed properly
    spark.stop()
