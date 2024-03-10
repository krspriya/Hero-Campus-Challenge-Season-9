import random
import csv

# Open CSV file for writing
with open('improved_synthetic_dataset.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write header row
    writer.writerow(['Vehicle ID','Speed (km/h)', 'Acceleration (m/s²)', 'Braking intensity (%)',
                     'Cornering speed (km/h)', 'Battery SoC (%)', 'Battery current (A)',
                     'Battery temperature (°C)', 'Motor speed (rpm)', 'Motor torque (Nm)',
                     'Regen braking level (%)', 'Energy consumption (kWh/km)',
                     'Distance traveled (km)', 'Altitude (m)', 'Heading (°)', 'Throttle position (%)',
                     'Regen braking state', 'Trip distance (km)', 'Trip time (min)',
                     'Ambient temperature (°C)', 'Motor fault codes', 'Driver Behavior rating'])

    # Generate 10000 rows of data
    for _ in range(10000):
        # Set the driver behavior rating
        behavior_rating = random.randint(1, 10)
        vehicle_id = f"EV{random.randint(1, 19):03d}"

        # Generate features based on driver behavior
        speed = random.randint(40, 100) + behavior_rating * 3
        acceleration = random.uniform(0, 5) + behavior_rating * 0.5
        braking_intensity = random.randint(60, 100) - behavior_rating * 2
        cornering_speed = random.randint(14, 30) + behavior_rating
        battery_soc = random.randint(70, 100) - behavior_rating
        battery_current = random.uniform(-9, -5)
        battery_temperature = random.randint(30, 80)
        motor_speed = random.randint(2700, 3200) - behavior_rating * 50
        motor_torque = random.randint(60, 100)
        regen_braking_level = random.randint(15, 30) - behavior_rating
        energy_consumption = random.uniform(0.15, 0.25) + behavior_rating * 0.02
        distance_traveled = random.uniform(10, 150) + behavior_rating * 2
        altitude = random.randint(150, 250)
        heading = random.randint(170, 190)
        throttle_position = random.randint(60, 90) - behavior_rating * 2
        regen_braking_state = random.choice(['On', 'Off'])
        trip_distance = random.uniform(0, distance_traveled)
        trip_time = trip_distance / (speed + 1) * 60
        ambient_temperature = random.uniform(22, 30)
        motor_fault_codes = random.choices([0, 101, 102, 103, 104], weights=[0.96, 0.01, 0.01, 0.01, 0.01])[0]

        # Write row to CSV
        writer.writerow([vehicle_id, speed, acceleration, braking_intensity, cornering_speed,
                         battery_soc, battery_current, battery_temperature, motor_speed,
                         motor_torque, regen_braking_level, energy_consumption, distance_traveled,
                         altitude, heading, throttle_position, regen_braking_state, trip_distance,
                         trip_time, ambient_temperature, motor_fault_codes, behavior_rating])
