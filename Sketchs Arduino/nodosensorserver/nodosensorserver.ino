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
//#define PASS "JUanito1611$"
//#define IP "184.106.153.149" // thingspeak.com
//String GET = "GET /update?key=0XQXMLQR3CE3R783&field1=";
#define SSID "pepowifi"
#define PASS "clavesegura"
//#define IP "192.168.0.102" // escritorio
#define IP "192.168.0.222" // utrabook
String GET = "";

void setup()
{
  pinMode(2,INPUT);
  Wire.begin();
  BH1750_Init(BH1750_address);
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
  int sensorValue = digitalRead(2);
  float valf=0;
  if(BH1750_Read(BH1750_address)==2){
    
    valf=((buff[0]<<8)|buff[1])/1.2;
    
    //if(valf<0)Serial.print("> 65535");
    //else Serial.print((int)valf,DEC); 
    
    //Serial.println(" lx"); 
  }
 
  char buffer[10];
  String tempF = dtostrf(valf,4, 1, buffer);
  
    int code=0;
  if(Serial.find("+IPD,0,1:"))
  {
  delay(100);
  code = Serial.read()-48;
  //Serial.println(code);
  }
  if(code ==1){
  //updateTemp(tempF,sensorValue);
  }
  
  delay(100);
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

void updateTemp(String tenmpF, int sensorValue){
  /*
  String cmd = "AT+CIPSTART=\"TCP\",\"";
  cmd += IP;
  cmd += "\",80";
  Serial.println(cmd);
  delay(1000);
  if(Serial.find("Error")){
    return;
  }
  */
  String cmd = GET;
  cmd += tenmpF;
  cmd += "\r\n";
  Serial.print("AT+CIPSEND=");
  Serial.println(cmd.length());
  if(Serial.find(">")){
    Serial.print(cmd);
  }else{
    //Serial.println("AT+CIPCLOSE");
  }
}

 
boolean connectWiFi(){
  Serial.println("AT+CWMODE=1");
  delay(2000);
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


void BH1750_Init(int address){
  
  Wire.beginTransmission(address);
  Wire.write(0x10); // 1 [lux] aufloesung
  Wire.endTransmission();
}

byte BH1750_Read(int address){
  
  byte i=0;
  Wire.beginTransmission(address);
  Wire.requestFrom(address, 2);
  while(Wire.available()){
    buff[i] = Wire.read(); 
    i++;
  }
  Wire.endTransmission();  
  return i;
}

