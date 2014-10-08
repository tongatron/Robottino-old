#include <Bridge.h>
#include <Temboo.h>
#include "TembooAccount.h" // contains Temboo account information

/*** SUBSTITUTE YOUR VALUES BELOW: ***/
// Note that for additional security and reusability, you could
// use #define statements to specify these values in a .h file.
const String TWITTER_ACCESS_TOKEN = "2745340788-KmX9qA2AMLR5YLVq8BqIfCiZnt2RXR1qt4St7gh";
const String TWITTER_ACCESS_TOKEN_SECRET = "m9lnkaWRNv5ksdlDR9N8KMZAvGDdxygU442AJn3FTdm4a";
const String TWITTER_API_KEY = "wvgBITg372lBUB7TMsZOhViA1";
const String TWITTER_API_SECRET = "urTw28x2XiqedJ6hw931b4rk30LdjPDMUOyRw2PG5CwBqAQqQA";

int numRuns = 1;   // execution count, so this doesn't run forever
int maxRuns = 30;   // the max number of times the Twitter HomeTimeline Choreo should run

//display
#include <Wire.h>
#include <SeeedOLED.h>

//servo
#include <Servo.h>  
Servo servo;
int pos = 0;
const int slow = 8;
const int fast = 2;

//output
const int buzzer = 11;
const int led_blue = 9;
const int led_green = 10;
const int led_red = 13;

char tweetchar[112];
char tweetchar_old[112];

void setup() {
  
  //output
  pinMode(buzzer,OUTPUT);
  pinMode(led_blue, OUTPUT);
  pinMode(led_green, OUTPUT);
  pinMode(led_red, OUTPUT);
  
  //display
  Wire.begin();
  SeeedOled.init(); 
  SeeedOled.clearDisplay();
  SeeedOled.setInverseDisplay();
  SeeedOled.setPageMode();  
  SeeedOled.setTextXY(3,0);    
  SeeedOled.putString("   ROBOTTINO   ");
  SeeedOled.setTextXY(5,0);    
  SeeedOled.putString("    v. 0.4.1   ");  

  ledred();
     
  Serial.begin(9600);
  servo.attach(8);
  
  delay(4000);
  //while(!Serial);  // For debugging, wait until a serial console is connected.
  Bridge.begin();
  
  ledgreen();
  
}

void loop()
{
  
  SeeedOled.clearDisplay();
  SeeedOled.setNormalDisplay();     
  SeeedOled.setPageMode();
  SeeedOled.setTextXY(3,0);
  SeeedOled.putString("***************");  
  SeeedOled.setTextXY(4,0);
  SeeedOled.putString("***************");  
  
 // while we haven't reached the max number of runs...
  if (numRuns <= maxRuns) {
    Serial.println("Running ReadATweet - Run #" + String(numRuns++));
    
    TembooChoreo HomeTimelineChoreo;

    // invoke the Temboo client.
    // NOTE that the client must be reinvoked, and repopulated with
    // appropriate arguments, each time its run() method is called.
    HomeTimelineChoreo.begin();
    
    // set Temboo account credentials
    HomeTimelineChoreo.setAccountName(TEMBOO_ACCOUNT);
    HomeTimelineChoreo.setAppKeyName(TEMBOO_APP_KEY_NAME);
    HomeTimelineChoreo.setAppKey(TEMBOO_APP_KEY);

    // tell the Temboo client which Choreo to run (Twitter > Timelines > HomeTimeline)
    HomeTimelineChoreo.setChoreo("/Library/Twitter/Timelines/HomeTimeline");
    
    
    // set the required choreo inputs
    // see https://www.temboo.com/library/Library/Twitter/Timelines/HomeTimeline/
    // for complete details about the inputs for this Choreo

    HomeTimelineChoreo.addInput("Count", "1"); // the max number of Tweets to return from each request
    HomeTimelineChoreo.addInput("AccessToken", TWITTER_ACCESS_TOKEN);
    HomeTimelineChoreo.addInput("AccessTokenSecret", TWITTER_ACCESS_TOKEN_SECRET);
    HomeTimelineChoreo.addInput("ConsumerKey", TWITTER_API_KEY);    
    HomeTimelineChoreo.addInput("ConsumerSecret", TWITTER_API_SECRET);

    // next, we'll define two output filters that let us specify the 
    // elements of the response from Twitter that we want to receive.
    // see the examples at http://www.temboo.com/arduino
    // for more on using output filters
   
    // we want the text of the tweet
    HomeTimelineChoreo.addOutputFilter("tweet", "/[1]/text", "Response");
    
    // and the name of the author
    HomeTimelineChoreo.addOutputFilter("author", "/[1]/user/screen_name", "Response");


    // tell the Process to run and wait for the results. The 
    // return code will tell us whether the Temboo client 
    // was able to send our request to the Temboo servers
    unsigned int returnCode = HomeTimelineChoreo.run();
    
   // a response code of 0 means success; print the API response
    if(returnCode == 0) {
      
      String author; // a String to hold the tweet author's name
      String tweet; // a String to hold the text of the tweet


      // choreo outputs are returned as key/value pairs, delimited with 
      // newlines and record/field terminator characters, for example:
      // Name1\n\x1F
      // Value1\n\x1E
      // Name2\n\x1F
      // Value2\n\x1E      
      
      // see the examples at http://www.temboo.com/arduino for more details
      // we can read this format into separate variables, as follows:
      
      while(HomeTimelineChoreo.available()) {
        
        ledblue();
        
        // read the name of the output item
        String name = HomeTimelineChoreo.readStringUntil('\x1F');
        name.trim();

        // read the value of the output item
        String data = HomeTimelineChoreo.readStringUntil('\x1E');
        data.trim();

        // assign the value to the appropriate String
        if (name == "tweet") {
          tweet = data;
        } else if (name == "author") {
          author = data;
        }
      }
     
      Serial.println("@" + author + " - " + tweet);
      delay(200);

      tweet.toCharArray(tweetchar, sizeof(tweetchar));
           
      
              if (strcmp(tweetchar,tweetchar_old) == 0) {

                ledblue();
                delay(100);
                ledgreen();
                delay(100);
                ledblue();
                delay(100);
                ledgreen();
                delay(100);
                ledblue();
                delay(100);
                ledgreen();
                delay(100);
                ledblue();
                delay(100);
                ledgreen();
                delay(100);
                
      	      }
      
              else {
	      SeeedOled.clearDisplay();          
	      SeeedOled.setHorizontalMode();     
	      SeeedOled.putString(tweetchar);
	      analogWrite(13, 50);
	      delay(400);
	      analogWrite(13, 0);
              rotate();
	      delay(3000);	      
              
              Serial.println(tweetchar);
              Serial.println(tweetchar_old);
              
              //tweetchar_old [112] = tweetchar [112];
              tweet.toCharArray(tweetchar_old, sizeof(tweetchar_old));
              }

        
    } else {
      // there was an error
      // print the raw output from the choreo
      while(HomeTimelineChoreo.available()) {
        char c = HomeTimelineChoreo.read();
        Serial.print(c);
        
        SeeedOled.clearDisplay();
        SeeedOled.setPageMode();  
        SeeedOled.setTextXY(3,0);    
        SeeedOled.putString("   errore   ");
        ledred();
        
      }
    }

    HomeTimelineChoreo.close();

  }

  Serial.println("Waiting...");
  ledgreen();
  SeeedOled.clearDisplay();
  SeeedOled.setTextXY(3,0);
  SeeedOled.putString("***************");  
  SeeedOled.setTextXY(4,0);
  SeeedOled.putString("***************");
  SeeedOled.setTextXY(6,0);
  SeeedOled.putString("waiting...45secs");   
  delay(45000); // wait 90 seconds between HomeTimeline calls  
}


// **************************** ****************************  ****************************

void rotate(){
  
  for(pos = 90; pos <= 130; pos += 1)  {
  ledred();    
  servo.write(pos);           
  delay(slow);                    
  } 
 
  for(pos = 130; pos>=40; pos-=1){
  ledblue();    
  servo.write(pos);         
  delay(fast);            
  }
 
  for(pos = 40; pos <= 90; pos += 1)  {
  ledred();
  servo.write(pos);           
  delay(slow);                    
  }

  servo.write(90);
  delay(100);
}

// **************************** ****************************  ****************************

void ledred(){
  digitalWrite(led_blue, LOW);
  digitalWrite(led_green, LOW);
  digitalWrite(led_red, HIGH);
}

void ledblue(){
  digitalWrite(led_blue, HIGH);
  digitalWrite(led_green, LOW);
  digitalWrite(led_red, LOW);  
}

void ledgreen(){
  digitalWrite(led_blue, LOW);
  digitalWrite(led_green, HIGH);
  digitalWrite(led_red, LOW);  
}

void ledoff(){
    digitalWrite(led_blue, LOW);
  digitalWrite(led_green, LOW);
  digitalWrite(led_red, LOW);  
}
