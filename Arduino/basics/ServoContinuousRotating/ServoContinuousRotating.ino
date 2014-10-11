/*
a different method to move the servo back and forth
taken from Radar sketch

Giovanni Bindi
oct. 2014
*/

#include <Servo.h> 
Servo servo;
int angle = 0;
int dir = 1; // direction of servo movement  -1 = back, 1 = forward

// means -angle .. angle
const int angle_bounds = 80; 
const int angle_step = 1;


void setup() {
  servo.attach(8);  
  delay(100);
}

void loop() {
    servo.write(angle + angle_bounds);
    if (angle >= angle_bounds || angle <= -angle_bounds) {
      dir = -dir;
      }
    angle += (dir * angle_step); 
    delay(20);
}
