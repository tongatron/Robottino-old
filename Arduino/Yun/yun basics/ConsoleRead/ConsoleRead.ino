/*
  Console Read example

 Read data coming from bridge using the Console.read() function
 and store it in a string.

 To see the Console, pick your Yún's name and IP address in the Port menu
 then open the Port Monitor. You can also see it by opening a terminal window
 and typing:
 ssh root@ yourYunsName.local 'telnet localhost 6571'
 then pressing enter. When prompted for the password, enter it.

 created 13 Jun 2013
 by Angelo Scialabba
 modified 16 June 2013
 by Tom Igoe

 This example code is in the public domain.

 http://arduino.cc/en/Tutorial/ConsoleRead

 */

#include <Wire.h>
#include <SeeedOLED.h>
#include <Console.h>

String name;

void setup() {
  // Initialize Console and wait for port to open:
  Bridge.begin();
  Console.begin();

  Wire.begin();
  SeeedOled.init();  //initialze SEEED OLED display
  SeeedOled.clearDisplay();           //clear the screen and set start position to top left corner
  SeeedOled.setNormalDisplay();       //Set display to Normal mode
  
  // Wait for Console port to connect
  while (!Console);

  Console.println("Hi, what's your name?");
  SeeedOled.setTextXY(3,0);
  SeeedOled.putString("Hi, what's your name?");
  
}

void loop() {
  if (Console.available() > 0) {
    char c = Console.read(); // read the next char received
    // look for the newline character, this is the last character in the string
    if (c == '\n') {
      //print text with the name received
      Console.print("Hi ");
      Console.print(name);
      Console.println("! Nice to meet you!");
      Console.println();
      
      SeeedOled.clearDisplay();             
      SeeedOled.setHorizontalMode();       
      
      /*
      char your_name[17];
      name.toCharArray(your_name, sizeof(your_name));
      SeeedOled.putString("kkkkkkkkkkkk");
      delay(1000);     
      */
      
      // Ask again for name and clear the old name
      Console.println("Hi, what's your name?");
      name = "";  // clear the name string
    }
    else {  	 // if the buffer is empty Cosole.read() returns -1
      name += c; // append the read char from Console to the name string
    }
  }
}


