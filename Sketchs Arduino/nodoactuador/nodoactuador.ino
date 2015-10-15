
#include <Wire.h>
#include <stdlib.h>
#include <SoftwareSerial.h>
#include <OneWire.h>

int BH1750_address = 0x23; // i2c Addresse
byte buff[2];

#define ONE_WIRE_BUS 8
//OneWire oneWire(ONE_WIRE_BUS);
//DallasTemperature sensors(&oneWire);

//#define SSID "LAC"
//#define PASS "HErmes1611$"
//#define IP "184.106.153.149" // thingspeak.com
//String GET = "GET /update?key=0XQXMLQR3CE3R783&field1=";
#define SSID "pepowifi"
#define PASS "clavesegura"
//#define IP "192.168.0.102" // escritorio
#define IP "192.168.0.101" // utrabook
String GET = "";

void setup()
{
  pinMode(9,OUTPUT);
  digitalWrite(9,HIGH);
  pinMode(8,OUTPUT);
  digitalWrite(8,HIGH);
  pinMode(7,OUTPUT);
  digitalWrite(7,HIGH);
  pinMode(6,OUTPUT);
  digitalWrite(6,HIGH);
  Wire.begin();
  //BH1750_Init(BH1750_address);
  Serial.begin(9600);
  Serial.println("AT");
  delay(2000);
  if(Serial.find("OK")){
    connectWiFi();
  }
  delay(2000);
  startServer();
  
}


void loop(){
  int code=0;
  if(Serial.find("+IPD,0,1:"))
  {
  delay(100);
  code = Serial.read()-48;
  //Serial.println(code);
  }
  if(code ==1){
  digitalWrite(9,LOW);
  }
  if(code ==2){
  digitalWrite(9,HIGH);
  }
  if(code ==3){
  digitalWrite(8,LOW);
  }
  if(code ==4){
  digitalWrite(8,HIGH);
  }
  if(code ==5){
  digitalWrite(7,LOW);
  }
  if(code ==6){
  digitalWrite(7,HIGH);
  }
  if(code ==7){
  digitalWrite(6,LOW);
  }
  if(code ==8){
  digitalWrite(6,HIGH);
  }
  if(code ==9){
  digitalWrite(6,HIGH);
  digitalWrite(7,HIGH);
  digitalWrite(8,HIGH);
  digitalWrite(9,HIGH);
  }
  if(code ==10){
  digitalWrite(6,LOW);
  digitalWrite(7,LOW);
  digitalWrite(8,LOW);
  digitalWrite(9,LOW);
  }

  
}

void startServer(){
  String cmd = "AT+CIPMUX=1";
  Serial.println(cmd);
  delay(2000);
  cmd = "AT+CIPSERVER=1,80";
  Serial.println(cmd);
  if(Serial.find("Error")){
    return;
  }
}

void updateTemp(String tenmpF){
  String cmd = "AT+CIPSTART=\"TCP\",\"";
  cmd += IP;
  cmd += "\",80";
  Serial.println(cmd);
  delay(1000);
  if(Serial.find("Error")){
    return;
  }
  cmd = GET;
  cmd += tenmpF;
  cmd += "\r\n";
  Serial.print("AT+CIPSEND=");
  Serial.println(cmd.length());
  if(Serial.find(">")){
    Serial.print(cmd);
  }else{
    Serial.println("AT+CIPCLOSE");
  }
}

 
boolean connectWiFi(){
  Serial.println("AT+CWMODE=1");
  delay(1000);
  String cmd="AT+CWJAP=\"";
  cmd+=SSID;
  cmd+="\",\"";
  cmd+=PASS;
  cmd+="\"";
  Serial.println(cmd);
  delay(5000);
  if(Serial.find("OK")){
    return true;
  }else{
    return false;
  }
}











