#include "stm32f10x.h"                  // Device header


int main(void) {
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOC, ENABLE);
	GPIO_InitTypeDef GPIO_InitStructure;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP;
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_13;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_Init(GPIOC, &GPIO_InitStructure);
	GPIO_SetBits(GPIOC, GPIO_Pin_13);
//	GPIO_ResetBits(GPIOC, GPIO_Pin_13);
	

	while(1) {
//		GPIO_SetBits(GPIOC, GPIO_Pin_13);   // 输出3.3V (LED灭)
//		for(int i=0; i<100000; i++);       // 简单延时
//		GPIO_ResetBits(GPIOC, GPIO_Pin_13); // 输出0V (LED亮)
//		for(int i=0; i<100000; i++);
	
	}
}
