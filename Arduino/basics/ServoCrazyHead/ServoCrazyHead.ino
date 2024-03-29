/*
without delay between servo positions, the head will shake

Giovanni Bindi
oct 2014
*/



#include <Servo.h> 
 
Servo servo;  // create servo object to control a servo 
                // twelve servo objects can be created on most boards
 
int pos = 0;    // variable to store the servo position 
 
void setup() 
{ 
  servo.attach(8);
  servo.write(90);
 delay(100);
 
  for (int i=0; i <= 90; i++){ 
    for(pos = 0; pos <= 180; pos += 1) // goes from 0 degrees to 180 degrees 
    {                                  // in steps of 1 degree 
      servo.write(pos);              // tell servo to g to position in variable 'pos' 
    } 
    for(pos = 180; pos>=0; pos-=1)     // goes from 180 degrees to 0 degrees 
    {                                
      servo.write(pos);              // tell servo to go to position in variable 'pos' 
    }
 }
 servo.write(90);
} 
 
void loop() 
{ 

} 
