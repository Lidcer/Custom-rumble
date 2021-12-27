int x;

int smallMotor = 3;
int largeMotor = 5;

int smallMotorValue = 0;
int largeMotorValue = 0;

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(smallMotor, OUTPUT);
  pinMode(largeMotor, OUTPUT);

  Serial.begin(115200);
  Serial.setTimeout(1);
}
void loop()
{
  if (!Serial.available())
    return;
  // Small motor = 1;
  // Big motor = 2;
  // value 250 = ;
  String data = Serial.readString();

  int value1 = getValue(data, ':', 0).toInt();
  int value2 = getValue(data, ':', 1).toInt();
  if (value != smallMotorValue)
  {
    analogWrite(smallMotor, value);
  }
  smallMotorValue = value

  if (value != largeMotorValue)
  {
    analogWrite(largeMotor, value);
  }
  largeMotorValue = value
}

int clamp(int value, int min, int max)
{
  if (value > max)
  {
    return max;
  }
  else if (value < min)
  {
    return min;
  }
  return value;
}

String getValue(String data, char separator, int index)
{
  int found = 0;
  int strIndex[] = {0, -1};
  int maxIndex = data.length() - 1;

  for (int i = 0; i <= maxIndex && found <= index; i++)
  {
    if (data.charAt(i) == separator || i == maxIndex)
    {
      found++;
      strIndex[0] = strIndex[1] + 1;
      strIndex[1] = (i == maxIndex) ? i + 1 : i;
    }
  }
  return found > index ? data.substring(strIndex[0], strIndex[1]) : "";
}