// Free RAM
void setup() {
  // put your setup code here, to run once:

}

void loop() {
  
  int freeRam () 
{
  extern int __heap_start, *__brkval; 
  int v; 
  return (int) &v - (__brkval == 0 ? (int) &__heap_start : (int) __brkval); 
}
}
