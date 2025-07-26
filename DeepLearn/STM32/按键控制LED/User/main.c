#include "stm32f10x.h"                  // Device header
#include "Delay.h"
#include "LED.h"
#include "Key.h"

int main(void) {
	
	LED_Init();
	Key_Init();
	
//	GPIO_ResetBits(GPIOA, GPIO_Pin_0);
//	GPIO_SetBits(GPIOA, GPIO_Pin_0);
//	GPIO_WriteBit(GPIOA, GPIO_Pin_0, Bit_SET);
//	GPIO_WriteBit(GPIOA, GPIO_Pin_0, Bit_RESET);
	
	uint8_t KeyNum;
	
	while(1) {
		KeyNum = Key_GetNum();
		if (KeyNum == 1) {
			LED1_Ture();
		}
		if (KeyNum == 2) {
			LED2_Ture();
		}
	}
}
