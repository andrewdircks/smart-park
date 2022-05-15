#include <Ethernet.h>
#include <SPI.h>

byte mac[] = { 0xA8, 0x61, 0x0A, 0xAE, 0x6F, 0xA0 };
byte ip[] = { 192, 168, 1, 65 };
char fn_host[] = "us-east4-parkcath.cloudfunctions.net";
String fn_name = "parked";
EthernetClient client;

void setup()
{
  Ethernet.begin(mac, ip);
  Serial.begin(9600);
  delay(1000);

  Serial.println("connecting...");

  if (client.connect(fn_host, 80)) {
    Serial.println("connected");
    client.println("GET /parked?spot_id=1&dist=25 HTTP/1.1");
    client.println("HOST: " + String(fn_host));
    client.println();
  } else {
    Serial.println("connection failed");
  }
}

void loop()
{
  if (client.available()) {
    char c = client.read();
    Serial.print(c);
  }

  if (!client.connected()) {
    Serial.println();
    Serial.println("disconnecting.");
    client.stop();
    for(;;)
      ;
  }
}
