double test_data;
double test_data_2;
double time_data = 0;

void setup() {
  Serial.begin(115200);
}

void loop() {
  time_data = micros()/1000000.00;
  test_data = 1.11;
  test_data_2 = test_data + time_data;
  Serial.print("計測時間;");
  Serial.print(time_data,2);
  Serial.print("表面温度;");
  Serial.print(test_data,2);
  Serial.print("裏面温度;");
  Serial.println(test_data_2,2);
  delay(100);
  
} 
