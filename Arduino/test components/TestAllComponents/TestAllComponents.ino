/*
  A4   photoresistor
  A5   photoresistor
  
  0
  1
  2    SDA - Display
  3  ~ SCL - Display
  4    ultrasonic echo
  5  ~ 
  6  ~ 
  7    ultrasonic trigger  
  8    servo
  9  ~ RGB Blue
  10 ~ RGB Green
  11 ~ Buzzer
  12
  13 ~ RGB Red
*/


// photoresistors
int lightValue1;
int lightValue2;

//Display
#include <Wire.h>
#include <SeeedOLED.h>

// Ultrasonic Distance Sensor
// occhio che forse la libreria è stata modificata per avere max 1mt di distanza massima
#include <NewPing.h>
#include <avr/pgmspace.h>
#define TRIGGER_PIN  7  // Arduino pin tied to trigger pin on the ultrasonic sensor.
#define ECHO_PIN     4  // Arduino pin tied to echo pin on the ultrasonic sensor.
#define MAX_DISTANCE 200 // Maximum distance we want to ping for (in centimeters). Maximum sensor distance is rated at 400-500cm.
NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE); // NewPing setup of pins and maximum distance.

void setup(){
  
  Serial.begin(9600);
  
  //display
  Wire.begin();	
  SeeedOled.init();  //initialze SEEED OLED display
  SeeedOled.clearDisplay();          //clear the screen and set start position to top left corner
  SeeedOled.setNormalDisplay();      //Set display to normal mode (i.e non-inverse mode)
  SeeedOled.setPageMode();           //Set addressing mode to Page Mode
  SeeedOled.setTextXY(0,0);
  SeeedOled.putString("xxxxxxxxxxxxxxxx");
  SeeedOled.setTextXY(1,0);
  SeeedOled.putString("xxxxxxxxxxxxxxxx");
  SeeedOled.setTextXY(2,0);
  SeeedOled.putString("xxxxxxxxxxxxxxxx");
  SeeedOled.setTextXY(3,0);
  SeeedOled.putString("xxxxxxxxxxxxxxxx");
  SeeedOled.setTextXY(4,0);
  SeeedOled.putString("xxxxxxxxxxxxxxxx");
  SeeedOled.setTextXY(5,0);
  SeeedOled.putString("xxxxxxxxxxxxxxxx");
  SeeedOled.setTextXY(6,0);
  SeeedOled.putString("xxxxxxxxxxxxxxxx");
  delay(500);
  
  digitalWrite(9,HIGH);
  digitalWrite(10,LOW);
  digitalWrite(13,LOW);  
  delay(500);
  digitalWrite(9,LOW);
  digitalWrite(10,HIGH);
  digitalWrite(13,LOW);  
  delay(500);
  digitalWrite(9,LOW);
  digitalWrite(10,LOW);
  digitalWrite(13,HIGH);  
  delay(500);  
  
  }

void loop(){
    


    int cm = sonar.ping_cm();
    lightValue1 = analogRead(A5);
    lightValue2 = analogRead(A4);
    
    delay(50); // minumum of 50 suggested by the ultrasonic library

 


 Serial.print ("photoresistor1: ");
 Serial.print (lightValue1);
 Serial.print ("  photoresistor2: ");
 Serial.print (lightValue2);
 Serial.print("    "); 
 Serial.print("distance: ");
 Serial.println(cm);

}



