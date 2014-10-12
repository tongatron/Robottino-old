/*

the display shows charatcters * * * continuosly
it seems that the Robottino's mouth is speaking
the sound part is the buzzer responding to light values

Giovanni Bindi
oct. 2014
*/

#include <Wire.h>
#include <SeeedOLED.h>

int sensorValue;
int sensorLow = 1023;
int sensorHigh = 0;
const int led_blue = 9;

void setup() {
  Wire.begin();	
  SeeedOled.init();  //initialze SEEED OLED display
  SeeedOled.clearDisplay();          //clear the screen and set start position to top left corner
  SeeedOled.setNormalDisplay();      //Set display to normal mode (i.e non-inverse mode)
  SeeedOled.setPageMode();           //Set addressing mode to Page Mode
  
  pinMode(led_blue, OUTPUT);
  digitalWrite(led_blue, HIGH);
  while (millis() < 5000) {
    sensorValue = analogRead(A5);
    if (sensorValue > sensorHigh) {
      sensorHigh = sensorValue;
    }
    if (sensorValue < sensorLow) {
      sensorLow = sensorValue;
    }
  }
  digitalWrite(led_blue, LOW);
  
 voice();
 
}


void loop() {
}


void voice(){
   analogWrite(led_blue, 5);  
   for (int i=0; i <= 80; i++){
      sensorValue = analogRead(A5);
      int pitch = map(sensorValue, sensorLow, sensorHigh, 4000, 5000);
      tone(11, pitch, 20);         
      SeeedOled.setTextXY(3,0);
      SeeedOled.putString("   **  **  **  ");
      SeeedOled.setTextXY(4,0);
      SeeedOled.putString(" **  **  **  * ");   
      delay(1);
      SeeedOled.setTextXY(3,0);
      SeeedOled.putString(" **  **  **  **");
      SeeedOled.setTextXY(4,0);
      SeeedOled.putString("   **  **  ** ");
      sensorValue = analogRead(A5);
      pitch = map(sensorValue, sensorLow, sensorHigh, 4000, 5000);
      tone(11, pitch, 20);
      delay(1);   
    }   
  digitalWrite(led_blue, LOW);  
}

