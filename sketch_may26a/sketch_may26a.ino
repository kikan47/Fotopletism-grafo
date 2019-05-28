int rojo = 11;
int verde = 10;
int azul = 9;

int option;

void setup(){
  Serial.begin(9600);
  pinMode(rojo, OUTPUT);
  pinMode(verde, OUTPUT);
  pinMode(azul, OUTPUT); 
}
 
void loop(){
  //si existe datos disponibles los leemos
  if (Serial.available()>0){
    //leemos la opcion enviada
    option=Serial.read();
    if(option=='r') {
      analogWrite(rojo, 255);
      analogWrite(verde, 0);
      analogWrite(azul, 0);
      //Serial.println("Rojo");
    }
    if(option=='v') {
      analogWrite(verde, 255);
      analogWrite(rojo, 0);
      analogWrite(azul, 0);
      //Serial.println("Verde");
    }
    if(option=='a') {
      analogWrite(azul, 255);
      analogWrite(rojo, 0);
      analogWrite(verde, 0);
      //Serial.println("Azul");
    }
  }
}
