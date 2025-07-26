#include "stm32f10x.h"                  // Device header
#include "Delay.h"
#include "LED.h"
#include "Key.h"
#include "Buzzer.h"
#include "LightSensor.h"

void main(void){
	
	Buzzer_Init();
	LightSensor_Init();
//	GPIO_ResetBits(GPIOA, GPIO_Pin_0);
//	GPIO_SetBits(GPIOA, GPIO_Pin_0);
//	GPIO_WriteBit(GPIOA, GPIO_Pin_0, Bit_SET);
//	GPIO_WriteBit(GPIOA, GPIO_Pin_0, Bit_RESET);
	
	
	while(1) {
			if (LightSensor_Get() == 0) {
				Buzzer_ON();
		}else {
			Buzzer_OFF();
		}
	}
}
