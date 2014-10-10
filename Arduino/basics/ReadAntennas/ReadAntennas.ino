/*
read light values fromt antennas

Giovanni Bindi
oct. 2014
*/

void setup() {  
  Serial.begin(9600);
}

void loop() {
  int Antenna1 = analogRead(A5);
  int Antenna2 = analogRead(A4);  
  
  Serial.print("A4: ");
  Serial.print(Antenna1);
  Serial.print(" A5: ");  
  Serial.println(Antenna2);
  delay(1);        
}
