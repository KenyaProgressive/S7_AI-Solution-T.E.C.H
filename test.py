from joblib import dump, load

flights = load('flights_data.joblib')
print(flights)