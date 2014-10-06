/*******************************************************************
  Adafruit Animal - Sound testing module
 
  Works on Arduino Uno, Leonardo, Mega, Menta, etc.
  can work on Trinket with right pin mapping and no Serial port
  
  https://learn.adafruit.com/adafruit-trinket-modded-stuffed-animal/animal-sounds
 *******************************************************************/

const int Buzzer = 11;
const int Potentiometer = A5;
 
void setup() {

   Serial.begin(9600);

  pinMode(Buzzer,OUTPUT);  // important to set pin as output
}
 
void loop()  {
//  varyFrequency();  // uncomment to search for correct tone value
  
// the sounds below are defined - comment out those you do not want or
//   comment out if using varyFrequency() to select play with tones
 
  meow();
  delay(2000);  
  meow2();
  mew();
  delay(2000);    
  ruff();
  delay(2000);  
  arf();
  delay(2000);
  
// scale();  // if you would like to hear the whole frequency
             //   range, you can use this function
}
 


void meow() {  // cat meow (emphasis ow "me")
  uint16_t i;
  playTone(5100,50);        // "m" (short)
  playTone(394,180);        // "eee" (long)
  for(i=990; i<1022; i+=2)  // vary "ooo" down
     playTone(i,8);
  playTone(5100,40);        // "w" (short)
}

void meow2() {  // cat meow (emphasis on "ow")
  uint16_t i;
  playTone(5100,55);       // "m" (short)
  playTone(394,170);       // "eee" (long)
  delay(30);               // wait a tiny bit
  for(i=330; i<360; i+=2)  // vary "ooo" down
     playTone(i,10);
  playTone(5100,40);       // "w" (short)
}

void mew() {  // cat mew
  uint16_t i;
  playTone(5100,55);       // "m"   (short)
  playTone(394,130);       // "eee" (long)
  playTone(384,35);        // "eee" (up a tiny bit on end)
  playTone(5100,40);       // "w"   (short)
}

void ruff() {   // dog ruff
  uint16_t i;
  for(i=890; i<910; i+=2)     // "rrr"  (vary down)
     playTone(i,3);
  playTone(1664,150);         // "uuu" (hard to do)
  playTone(12200,70);         // "ff"  (long, hard to do)
}

void arf() {    // dog arf
  uint16_t i;
  playTone(890,25);          // "a"    (short)
  for(i=890; i<910; i+=2)    // "rrr"  (vary down)
     playTone(i,5);
  playTone(4545,80);         // intermediate
  playTone(12200,70);        // "ff"   (shorter, hard to do)
}

// play tone on a piezo Buzzer: tone shorter values produce higher frequencies
//  which is opposite beep() but avoids some math delay - similar to code by Erin Robotgrrl

void playTone(uint16_t tone1, uint16_t duration) {
  if(tone1 < 50 || tone1 > 15000) return;  // these do not play on a piezo
  for (long i = 0; i < duration * 1000L; i += tone1 * 2) {
     digitalWrite(Buzzer, HIGH);
     delayMicroseconds(tone1);
     digitalWrite(Buzzer, LOW);
     delayMicroseconds(tone1);
  }     
}

// another sound producing function similar to http://web.media.mit.edu/~leah/LilyPad/07_sound_code.html
void beep (int16_t frequencyInHertz, long timeInMilliseconds) {
    long x;	 
    long delayAmount = (long)(1000000/frequencyInHertz);
    long loopTime = (long)((timeInMilliseconds*1000)/(delayAmount*2));
    for (x=0;x<loopTime;x++) {	 
       digitalWrite(Buzzer,HIGH);
       delayMicroseconds(delayAmount);
       digitalWrite(Buzzer,LOW);
       delayMicroseconds(delayAmount);
    }	 
}

void scale() {
  for(uint16_t i=50; i<15000; i++)  {
     playTone(i,20);
  }
}
