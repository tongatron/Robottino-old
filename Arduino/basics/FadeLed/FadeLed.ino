int led = 9;
int brightness = 0;    // how bright the LED is
int fadeAmount = 5;    // how many points to fade the LED by

void setup()  { 
  pinMode(led, OUTPUT);
} 

void loop()  {
  analogWrite(led, brightness);    
  brightness = brightness + fadeAmount;
  // reverse the direction of the fading at the ends of the fade: 
  if (brightness == 0 || brightness == 255) {
    fadeAmount = -fadeAmount ; 
  }     
  // wait to see the dimming effect    
  delay(15);                            
}

