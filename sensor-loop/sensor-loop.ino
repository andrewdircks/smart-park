#include <Ethernet.h>
#include <SPI.h>

#define echoPin 2
#define trigPin 3

// ethernet init
byte mac[] = { 0xA8, 0x61, 0x0A, 0xAE, 0x6F, 0xA0 };
byte ip[] = { 192, 168, 1, 224 };
char fn_host[] = "us-east4-parkcath.cloudfunctions.net";
String fn_name = "parked";
EthernetClient client;

// sensor init
long duration;
int distance;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Ethernet.begin(mac, ip);

  delay(1000);
  Serial.begin(9600);
}

void write(int spot_id, int distance) {
    if (client.connect(fn_host, 80)) {
        Serial.println("connected");
        client.println("GET /parked?spot_id=" + String(spot_id) + "&dist=" + String(distance) + " HTTP/1.1");
        client.println("HOST: " + String(fn_host));
        client.println();
    } else {
        Serial.println("connection failed");
    }
}

void loop() {
  // Clears the trigPin condition
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
  // Displays the distance on the Serial Monitor
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  // write the distance to the db
  write(1, distance);

 delay(60000);
}
