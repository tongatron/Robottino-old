
void setup() {
  pinMode(11, OUTPUT);
}

void loop() {
  analogWrite(11, 10);   
  delay(100);            
  digitalWrite(11, LOW);   
  delay(5000);  
}
