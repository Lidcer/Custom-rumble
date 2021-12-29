int x;

int smallMotor = 3;
int largeMotor = 5;

int smallMotorValue = 0;
int largeMotorValue = 0;

void setup()
{
  pinMode(smallMotor, OUTPUT);
  pinMode(largeMotor, OUTPUT);
  Serial.begin(115200);
  Serial.setTimeout(1);
}
void loop()
{
  if (Serial.available() > 1)
  {
    pinMode(LED_BUILTIN, true);
    int smallMotorReceavedValue = Serial.read();
    int largeMotorReceavedValue = Serial.read();
    bool perform = true;
    while (Serial.available())
    {
      Serial.read();
      perform = false;
    }
    if (!perform)
    {
      smallMotorReceavedValue = 0;
      largeMotorReceavedValue = 0;
    }
    if (smallMotorReceavedValue != smallMotorValue)
    {
      analogWrite(smallMotor, smallMotorReceavedValue);
    }
    smallMotorValue = smallMotorReceavedValue;

    if (largeMotorReceavedValue != largeMotorValue)
    {
      analogWrite(largeMotor, largeMotorReceavedValue);
    }
    largeMotorValue = largeMotorReceavedValue;
  }
}
