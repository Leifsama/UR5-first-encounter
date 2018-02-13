int zelena = 13; 
int cervena = 12;  
int kontrola = 8;
char rxChar= 0;
 
void setup() 
{ 
  pinMode(zelena, OUTPUT);
  pinMode(cervena, OUTPUT);
  pinMode(kontrola, OUTPUT);
  Serial.begin(9600);
  while (! Serial);
   Serial.flush();
} 
 
 
void loop() 

{ 
  if (Serial.available()>0)
 
  {  
    rxChar = Serial.read();            // Save character received. 
    Serial.flush();                    // Clear receive buffer.

  switch (rxChar){
  
case 'a':{
   
   digitalWrite(cervena,LOW);
   digitalWrite(zelena,HIGH);
   digitalWrite(kontrola,HIGH);
}
       break;
case 'd':{
   digitalWrite(cervena,HIGH);
   digitalWrite(zelena,LOW);
   digitalWrite(kontrola,LOW);  
   
    }
     break;
   default:                           
      Serial.print("'");
      Serial.print((char)rxChar);
      Serial.println("' is not a command!");
  }  }} 
