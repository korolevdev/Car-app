#include <SoftwareSerial.h>
#include <URMSerial.h>

URMSerial urm;

int value; // This value will be populated
int prev = -1;
int getMeasurement()
{
    // Request a distance reading from the URM37
    switch(urm.requestMeasurementOrTimeout(DISTANCE, value)) // Find out the type of request
    {
        case DISTANCE: // Double check the reading we recieve is of DISTANCE type
            //    Serial.println(value); // Fetch the distance in centimeters from the URM37
            prev = value;
            return value;
            break;
        case TEMPERATURE:
            return value;
            break;
        case ERROR:
            //Serial.println("Error");
            return prev;
            break;
        case NOTREADY:
            //Serial.println("Not Ready");
            return prev;
            break;
        case TIMEOUT:
            //Serial.println("Timeout");
            return prev;
            break;
    } 

    return prev;
}

#define LEFT 0
#define RIGHT 1

long coder[2] = {
  0,0};
int lastSpeed[2] = {
  0,0};  


void setup() {
    Serial.begin(9600);                  
    urm.begin(8,9,9600);              
    prev = getMeasurement();
    while (prev < 0)
    {
      prev = getMeasurement();
    }
    
    attachInterrupt(LEFT, LwheelSpeed, CHANGE);    //init the interrupt mode for the digital pin 2
    attachInterrupt(RIGHT, RwheelSpeed, CHANGE);   //init the interrupt mode for the digital pin 3
}

void loop()
{
    delay(50);
    static unsigned long timer = 0;                //print manager timer
  if(millis() - timer > 100){                   
    lastSpeed[LEFT] = coder[LEFT];   //record the latest speed value
    lastSpeed[RIGHT] = coder[RIGHT];
    coder[LEFT] = 0;                 //clear the data buffer
    coder[RIGHT] = 0;
    timer = millis();
  }
  int data[3];
  data[0] = getMeasurement();
  data[1] = lastSpeed[LEFT];
  data[2] = lastSpeed[RIGHT]; 
  Serial.println(encode(data[1], data[2], data[0]));
}

unsigned long encode(byte lv, byte rv, int dist) {
  return (unsigned long)lv << 24 | (unsigned long)rv << 16 | dist & 0xffff;
}

void LwheelSpeed()
{
  coder[LEFT] ++;  //count the left wheel encoder interrupts
}


void RwheelSpeed()
{
  coder[RIGHT] ++; //count the right wheel encoder interrupts
}
