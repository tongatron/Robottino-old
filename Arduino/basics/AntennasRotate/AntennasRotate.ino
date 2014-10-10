/*

with ambient light: 90'
more light > 180
less light > 0

Giovanni Bindi
oct 2014
*/

const int led_blue = 9;
const int led_green = 10;
const int led_red = 13;


int antennas = 0;     
int sensorMin = 1023;       
int sensorMax = 0;
int average = 0;
int fork = 200; //max difference form average

#include <Servo.h> 
Servo servo;
int pos = 90;

void setup() {
 
   servo.attach(8);
   servo.write(pos);
   delay(10);
   
   //Serial.begin(9600);
  
    for (int i=0; i <= 500; i++){
     
      int antenna1 = analogRead(A5);
      int antenna2 = analogRead(A4);
      delay(5);
      antennas = ((antenna1 + antenna1)/2);
    
      if (antennas > sensorMax) {
        sensorMax = antennas;
      }
      if (antennas < sensorMin) {
        sensorMin = antennas;
      }
    }
    
    average = ((sensorMin + sensorMax)/2);

  
}

void loop() {
  
  int antenna1 = analogRead(A5);
  int antenna2 = analogRead(A4);
  delay(2);
  antennas = ((antenna1 + antenna1)/2);  
  
  pos = map(antennas, (average-fork), (average+fork), 0, 180);

  servo.write(pos);
 

  
  delay(1);        
  
  /*
  Serial.print("A5: ");
  Serial.print(antenna1);
  Serial.print(" A4: ");  
  Serial.print(antenna2);
  Serial.print(" average: ");  
  Serial.print(average);  
  Serial.print(" antennas: ");  
  Serial.println(antennas);
  */

}
