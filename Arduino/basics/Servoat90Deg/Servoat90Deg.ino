/*
this sketch move the Robottino to 90 degrees
*/

#include <Servo.h>  
Servo servo; 
int pos = 0;
 
void setup() 
{ 
  servo.attach(8);
} 
 
void loop() 
{        
    servo.write(90);
} 
