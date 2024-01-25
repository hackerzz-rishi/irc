#define pwm 26
#define dir 27


void setup() {


  //rover
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);

  Serial.begin(115200);
  Serial.setTimeout(100);


  //Arm 
  pinMode(22, OUTPUT);
  pinMode(23, OUTPUT);  
  pinMode(24, OUTPUT);
  pinMode(25, OUTPUT);
  pinMode(pwm, OUTPUT);
  pinMode(dir, OUTPUT);

  pinMode(28,INPUT_PULLUP);
  pinMode(29,INPUT_PULLUP);
  pinMode(30,OUTPUT);
  pinMode(31,OUTPUT);
  pinMode(32,OUTPUT);
  pinMode(33,OUTPUT);
  digitalWrite(pwm, HIGH);
  digitalWrite(dir, HIGH);

}

//motor
void back(int a) {
  analogWrite(2, a);
  analogWrite(3, 0);
  analogWrite(4, a);
  analogWrite(5, 0);
  analogWrite(6, a);
  analogWrite(7, 0);

  analogWrite(8, a);
  analogWrite(9, 0);
  analogWrite(10, a);
  analogWrite(11, 0);
  analogWrite(12, a);
  analogWrite(13, 0);
}

void forward(int a) {
  analogWrite(2, 0);
  analogWrite(3, a);
  analogWrite(4, 0);
  analogWrite(5, a);
  analogWrite(6, 0);
  analogWrite(7, a);

  analogWrite(8, 0);
  analogWrite(9, a);
  analogWrite(10, 0);
  analogWrite(11, a);
  analogWrite(12, 0);
  analogWrite(13, a);
}

void left(int a) {
  analogWrite(2, 0);
  analogWrite(3, a);
  analogWrite(4, 0);
  analogWrite(5, a);
  analogWrite(6, 0);
  analogWrite(7, a);

  analogWrite(8, a);
  analogWrite(9, 0);
  analogWrite(10, a);
  analogWrite(11, 0);
  analogWrite(12, a);
  analogWrite(13, 0);
}

void right(int a) {
  analogWrite(2, a);
  analogWrite(3, 0);
  analogWrite(4, a);
  analogWrite(5, 0);
  analogWrite(6, a);
  analogWrite(7, 0);

  analogWrite(8, 0);
  analogWrite(9, a);
  analogWrite(10, 0);
  analogWrite(11, a);
  analogWrite(12, 0);
  analogWrite(13, a);
}

void stopMotors() {
  analogWrite(2, 0);
  analogWrite(3, 0);
  analogWrite(4, 0);
  analogWrite(5, 0);
  analogWrite(6, 0);
  analogWrite(7, 0);

  analogWrite(8, 0);
  analogWrite(9, 0);
  analogWrite(10, 0);
  analogWrite(11, 0);
  analogWrite(12, 0);
  analogWrite(13, 0);
}

//Arm
void down1() {
  digitalWrite(22, LOW);
  digitalWrite(23, HIGH);
}

void up1() {
  digitalWrite(22, HIGH);
  digitalWrite(23, LOW);
}

void down2() {
  digitalWrite(24, LOW);
  digitalWrite(25, HIGH);
}

void up2() {
  digitalWrite(24, HIGH);
  digitalWrite(25, LOW);
}

void down() {
  down1();
  down2();
}

void up() {
  up1();
  up2();
}
void baseright(){
  digitalWrite(pwm, 0);
  digitalWrite(dir, 0);
}
void baseleft(){
  digitalWrite(pwm, 0);
  digitalWrite(dir, 1);
}
void stop(){
  digitalWrite(pwm, 1);
  digitalWrite(dir, 1);
  digitalWrite(22, LOW);
  digitalWrite(23, LOW);
  digitalWrite(24, LOW);
  digitalWrite(25, LOW);

  digitalWrite(30, LOW);
  digitalWrite(31, LOW);
  digitalWrite(32, LOW);
  digitalWrite(33, LOW);

}
void wristup(){
  digitalWrite(30, LOW);
  digitalWrite(31, HIGH);
}
void wristdown(){
  digitalWrite(30, HIGH);
  digitalWrite(31, LOW);
}
void gripup(){
  digitalWrite(32, LOW);
  digitalWrite(33, HIGH);
}
void gripdown(){
  digitalWrite(32, HIGH);
  digitalWrite(33, LOW);
}

char rover = 's', arm ='s';
int speed = 0,a, b;


void loop() {
  // put your main code here, to run repeatedly:
  a = digitalRead(28);
  b = digitalRead(29);
 Serial.print(rover);
 Serial.print(",");
 Serial.print(speed);
 Serial.print(",");
 Serial.print(arm);
 Serial.print(",");
 Serial.print(a);
 Serial.print(",");
 Serial.println(b);
 if (Serial.available() > 0) {
  //Read the incoming string until a newline character is received
    String inputString = Serial.readStringUntil('\n');
    Serial.println(inputString);
  // Parse the string
  // Use sscanf to parse the string
    sscanf(inputString.c_str(), "%c,%d,%c", &rover, &speed , &arm);
 }
      if(rover=='f'){
        forward(speed);
      }
      else if(rover=='b'){
        back(speed);
      }
      else if(rover=='l'){
        left(speed);
      }
      else if(rover=='r'){
        right(speed);
      }
    
      else{
        stopMotors();
      }

      if(arm=='l'){
        baseleft();
      }
      else if(arm=='r'){
        baseright();
      }
      else if(arm=='u' && a == 1){
        up();
      }
      else if(arm=='d' && b == 1){
        down();
      }
      else if(arm == 'z'){
        gripup();
      }
      else if(arm == 'x'){
        gripdown();
      }
      else if(arm == 'c'){
        wristup();
      }
      else if(arm == 'v'){
        wristdown();
      }
      else{
        stop();
      }


}
