/*
 Light Themeremin basics are taken from Arduino Starter Kit example:
 http://arduino.cc/starterKit

*/

// variable to hold sensor value
int Antenna1;
int Antennas;

// variable to calibrate low value
int sensorLow = 1023;
// variable to calibrate high value
int sensorHigh = 0;
// LED pin
const int ledPin = 13;

void setup() {
  // Make the LED pin an output and turn it on
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, HIGH);

  // calibrate for the first five seconds after program runs
  while (millis() < 5000) {
    // record the maximum sensor value
    Antenna1 = analogRead(A5);
    if (Antenna1 > sensorHigh) {
      sensorHigh = Antenna1;
    }
    // record the minimum sensor value
    if (Antenna1 < sensorLow) {
      sensorLow = Antenna1;
    }
  }
  // turn the LED off, signaling the end of the calibration period
  digitalWrite(ledPin, LOW);
}

void loop() {
  //read the input from A0 and store it in a variable
  Antennas = ((analogRead(A5)+analogRead(A5))/2);

  // map the sensor values to a wide range of pitches
  int pitch = map(Antennas, sensorLow, sensorHigh, 50, 4000);

  // play the tone for 20 ms on pin 8
  tone(11, pitch, 20);

  // wait for a moment
  delay(10);
}

