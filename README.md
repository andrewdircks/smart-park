# Smart Parking

This simple, efficient, and inexpensive smart parking application uses an 
ultrasonic distance sensor, an Arduino, and Google Cloud Platform to
provide real-time detection of spot availability. For a full description of the 
hardware and software system, see the presentation attached in `summary.pdf`. 
Two weeks of recorded data is available in `data.csv`.

## parked
This GCP Serverless Function is the main endpoint called by the Arduino every minute.
With a simple GET request, the Arduino sends the API two parameters: 
`spot_id` and `dist`, the parking spot identifier and the recorded distance 
(via ultrasonic sensor) to the nearest object. This information is written
to a PostgreSQL database (record and view tables). A sample deploy script is 
included.

## frontend
This *very* simple GCP Function reads the most recent parking data from the 
PostgreSQL database, implements an `is_available` function, and serves
simple HTML text depending on the determined availability. A sample deploy script is 
included.

## sensor-loop
This is the code run by the Arduino continually. From a high level, it initializes
an ethernet connection (via the *Ethernet Shield 2*), then calculates a distance
by controlling the sensor, then uploads the data to the `parked` endpoint described 
above, then repeats every minute.

