/*
https://gist.github.com/biokys/6846527
https://learn.sparkfun.com/tutorials/connecting-arduino-to-processing/to-processing

Giovanni Bindi
oct. 2014

*/

//display
#include <Wire.h>
#include <SeeedOLED.h>
#include <avr/pgmspace.h>

const int buzzer = 11;
const int led_blue = 9;
const int led_green = 10;
const int led_red = 13;

#include <NewPing.h>
#include <Servo.h> 

#define TRIGGER_PIN  7 
#define ECHO_PIN     4 
#define MAX_DISTANCE 100 // Maximum distance we want to ping for (in centimeters). Maximum sensor distance is rated at 400-500cm.
#define SERVO_PWM_PIN 8         
NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE); 

// means -angle .. angle
#define ANGLE_BOUNDS 80
#define ANGLE_STEP 1

Servo myservo;
int angle = 0;
int dir = 1; // direction of servo movement  -1 = back, 1 = forward 


// funzione per neutralizzare i falsi positivi isoltati
const int numReadings = 3; 
int readings[numReadings];                // the readings from the analog input
int index = 0;                  // the index of the current reading
int total = 0;                  // the running total
int cm_ignora_posit = 0;                // the cm_ignora_posit


void setup() {
  
  for (int thisReading = 0; thisReading < numReadings; thisReading++) // 0, 1, 2
   readings[thisReading] = 0;  
  
    //output
  pinMode(buzzer,OUTPUT);
  pinMode(led_blue, OUTPUT);
  pinMode(led_green, OUTPUT);
  pinMode(led_red, OUTPUT);
  digitalWrite(led_red, HIGH);
  digitalWrite(led_green, LOW);
  digitalWrite(led_blue, LOW);
  
  //display
  Wire.begin();
  SeeedOled.init(); 
  SeeedOled.clearDisplay();
  delay(200);

  
  Serial.begin(9600); 
  
  myservo.attach(SERVO_PWM_PIN);  
  delay(200);
  digitalWrite (led_red, LOW);
}

void loop() {
  
  // we must renormalize to positive values, because angle is from -ANGLE_BOUNDS .. ANGLE_BOUNDS
  // and servo value must be positive
  
  myservo.write(angle + ANGLE_BOUNDS);
  
  // read distance from sensor and send to serial
  getDistanceAndSend2Serial(angle);
  
  digitalWrite (led_blue, HIGH);
  digitalWrite (led_green, LOW);
  analogWrite (buzzer, 0);
  
  // calculate angle
  if (angle >= ANGLE_BOUNDS || angle <= -ANGLE_BOUNDS) {
    dir = -dir;
  }
  angle += (dir * ANGLE_STEP);  
  
}

int getDistanceAndSend2Serial(int angle) {
  delay(10);
  int cm = sonar.ping_cm();
  
  Serial.print(angle, DEC);
  Serial.print(",");
  Serial.println(cm, DEC);
  

  readings[index] = cm;
  cm_ignora_posit = (readings[0] * readings[1] * readings[2]);
  index = index + 1;
  if (index>=numReadings)
	index = 0;
  
  //Serial.print("cm_ignora_posit: ");
  //Serial.println(cm_ignora_posit);  
  
  // while the object is detected, the motor will spin slowly: delay 
  if (cm_ignora_posit != 0) {
      digitalWrite (led_blue, LOW);      
      digitalWrite (led_green, HIGH); // da 0 a 250
      int pitch = map(cm, 0, 99, 50, 0);  // 50 per avere n tono piezo non fastidioso
      //analogWrite (led_green, pitch * 5); // da 0 a 250
      analogWrite (buzzer, pitch);
      delay(10); 
    }
    
}
