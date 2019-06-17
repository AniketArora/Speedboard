#include <SoftwareServo.h> 
int potentiometer=1;
int potval;
int potvalmap;
int curval;
String bericht;


SoftwareServo ESC;

void setup() {
  
  pinMode(potentiometer, INPUT);
  ESC.attach(9);    
  Serial.begin(9600);  
  curval=0;
  ESC.setMinimumPulse(800);
  ESC.setMaximumPulse(2000);
}

void loop() {
  if (Serial.available() > 0) {
    bericht = Serial.readString();
  }

  if(bericht == "Start") {
    potval = 512;
    potvalmap = map(potval,0, 1023, 0, 180);

    while(true) {
      bericht = Serial.readString();

    while(curval < potval) {
      if(bericht == "Forward") {
        potval = potval + 10;
      }
      potvalmap = map(potval, 0 , 1023 , 0 , 180);
      curval=curval+1;
      ESC.write(curval);
      SoftwareServo::refresh();
      delay(100);
    }

     while(curval>potval){
      if(bericht == "Backward") {
        potval = potval -10;
      }
      potvalmap=map(potval,0,1023,0,180);
      curval=curval-1;
      ESC.write(curval);
      SoftwareServo::refresh();
      Serial.println(curval);
      delay(50);
     }

     bericht = "123";
     
    }

    
  } else {
    
    potval=analogRead(potentiometer);
    potval=map(potval,0,1023,0,180);
  
    while(curval<potval){
      potval=analogRead(potentiometer);
      potval=map(potval,0,1023,0,180);
      curval=curval+1;
      ESC.write(curval);
      SoftwareServo::refresh();
      Serial.println(curval);
      delay(100);
    }

    while(curval>potval){
      potval=analogRead(potentiometer);
      potval=map(potval,0,1023,0,180);
      curval=curval-1;
      ESC.write(curval);
      SoftwareServo::refresh();
      Serial.println(curval);
      delay(50);
    }

    ESC.write(curval);
    SoftwareServo::refresh();
    Serial.println(curval);
  }
}
