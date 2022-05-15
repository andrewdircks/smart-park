#include <Ethernet.h>

// ethernet init
byte mac[] = { 0xA8, 0x61, 0x0A, 0xAE, 0x6F, 0xA0 };
byte ip[] = { 192, 168, 1, 224 };
char fn_host[] = "us-east4-parkcath.cloudfunctions.net";
String fn_name = "parked";
EthernetClient client;

void setup() {
  // ...
  Ethernet.begin(mac, ip);
  // ...
}

void write(int spot_id, int distance) {
    if (client.connect(fn_host, 80)) {
        client.println("GET /parked?dist=" + String(distance) + " HTTP/1.1");
        client.println();
    } else {
        Serial.println("connection failed");
    }
}

void loop() {
  // calculate distance
  // ...
  write(distance);
  // ...
  // wait
}
