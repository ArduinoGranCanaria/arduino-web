void setup()
{
  Serial.begin(9600);
}

void loop()
{
  char buffer[10];
  Serial.readBytesUntil(10, buffer, 10);

  int luz = analogRead(0);
  Serial.println(luz);
}
