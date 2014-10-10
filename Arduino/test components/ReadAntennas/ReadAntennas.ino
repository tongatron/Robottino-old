/*
Giovanni Bindi
oct. 2014
*/

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int sensorValue1 = analogRead(A5);
  int sensorValue2 = analogRead(A4);  
  // print out the value you read:
  Serial.print("A4: ");
  Serial.print(sensorValue2);
  Serial.print(" A5: ");  
  Serial.println(sensorValue1);
  delay(1);        // delay in between reads for stability
}
