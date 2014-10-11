/*
the mouth-display shows the light values from antennas

Giovanni Bindi
oct. 2014

*/

#include <Wire.h>
#include <SeeedOLED.h>

int Antenna1 = 0;
int Antenna2 = 0;

void setup() {

  Wire.begin();
  SeeedOled.init();  //initialze SEEED OLED display
      SeeedOled.clearDisplay();          
      SeeedOled.setNormalDisplay();     
      SeeedOled.setHorizontalMode();
}

void loop() {
  
  Antenna1 = analogRead(A5);
  Antenna2 = analogRead(A4);  
  delay(10);
       
      SeeedOled.setTextXY(2,0);
      SeeedOled.putString("ANTENNA 1:");
      SeeedOled.setTextXY(3,0);
      SeeedOled.putNumber(Antenna1);
      
      SeeedOled.setTextXY(5,0);
      SeeedOled.putString("ANTENNA 2:");
      SeeedOled.setTextXY(6,0);
      SeeedOled.putNumber(Antenna2);
  
  delay(50);

}
