/*
the display shows charatcters * * * continuosly
it seems that the Robottino's mouth is speaking

Giovanni Bindi
oct 2014
*/

//display
#include <Wire.h>
#include <SeeedOLED.h>

void setup() {
  
  //display
  Wire.begin();
  SeeedOled.init(); 
  SeeedOled.clearDisplay();

}

void loop() { 
      SeeedOled.setTextXY(3,0);
      SeeedOled.putString("   **  **  **  ");
      SeeedOled.setTextXY(4,0);
      SeeedOled.putString(" **  **  **  * ");  
      delay(1);
      SeeedOled.setTextXY(3,0);
      SeeedOled.putString(" **  **  **  **");
      SeeedOled.setTextXY(4,0);
      SeeedOled.putString("   **  **  ** ");
      delay(1);   
}

