def relay_distance_input(distance_miles: float, num_runners: float):
    """Calculates total relay distance in kilometers based on provided inputs."""
    total_miles = (distance_miles) * (num_runners)
    total_km = (miles_to_km(total_miles) * 1.60934)
    return total_km

# 🏃 Example usage:
distance_miles = input("Enter the distance each runner will run (in miles): ")
num_runners = input("Enter the number of runners: ")
total_km = relay_distance_input(distance_miles, num_runners)

print(f"The total relay distance is {total_km:.2f} kilometers.")