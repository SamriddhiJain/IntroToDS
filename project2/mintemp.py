import pandas
import pandasql

def avg_min_temperature(filename):
    '''
    This function should run a SQL query on a dataframe of
    weather data. More specifically you want to find the average
    minimum temperature (mintempi column of the weather dataframe) on 
    rainy days where the minimum temperature is greater than 55 degrees.
    '''
    weather_data = pandas.read_csv(filename)

    q = """
    SELECT avg(cast(mintempi as integer)) FROM weather_data 
    WHERE (rain==1 AND cast(mintempi as integer)>55)
    """
    
    #Execute your SQL command against the pandas frame
    avg_min_temp_rainy = pandasql.sqldf(q.lower(), locals())
    return avg_min_temp_rainy