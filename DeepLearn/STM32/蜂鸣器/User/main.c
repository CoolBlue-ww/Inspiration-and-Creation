#include "stm32f10x.h"                  // Device header
#include "Delay.h"

int main(void) {
	
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOB, ENABLE);
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA, ENABLE);
	
	GPIO_InitTypeDef GPIO_InitStructure;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP;
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_12;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_Init(GPIOB, &GPIO_InitStructure);
	
	GPIO_InitTypeDef GPIO_Union;
	GPIO_Union.GPIO_Mode = GPIO_Mode_Out_PP;
	GPIO_Union.GPIO_Pin = GPIO_Pin_All;
	GPIO_Union.GPIO_Speed = GPIO_Speed_50MHz;

	GPIO_Init(GPIOA, &GPIO_Union);
//	GPIO_ResetBits(GPIOA, GPIO_Pin_0);
//	GPIO_SetBits(GPIOA, GPIO_Pin_0);
//	GPIO_WriteBit(GPIOA, GPIO_Pin_0, Bit_SET);
//	GPIO_WriteBit(GPIOA, GPIO_Pin_0, Bit_RESET);
	
	
	while(1) {
		GPIO_ResetBits(GPIOA, GPIO_Pin_0);
		GPIO_ResetBits(GPIOB, GPIO_Pin_12);
		Delay_ms(150);
		GPIO_SetBits(GPIOA, GPIO_Pin_0);
		GPIO_SetBits(GPIOB, GPIO_Pin_12);
		Delay_ms(150);
		GPIO_ResetBits(GPIOA, GPIO_Pin_1);
		GPIO_ResetBits(GPIOB, GPIO_Pin_12);
		Delay_ms(150);
		GPIO_SetBits(GPIOA, GPIO_Pin_1);
		GPIO_SetBits(GPIOB, GPIO_Pin_12);
		Delay_ms(150);
		GPIO_ResetBits(GPIOA, GPIO_Pin_2);
		GPIO_ResetBits(GPIOB, GPIO_Pin_12);
		Delay_ms(150);
		GPIO_SetBits(GPIOA, GPIO_Pin_2);
		GPIO_SetBits(GPIOB, GPIO_Pin_12);
		Delay_ms(150);
		GPIO_ResetBits(GPIOA, GPIO_Pin_3);
		GPIO_ResetBits(GPIOB, GPIO_Pin_12);
		Delay_ms(150);
		GPIO_SetBits(GPIOA, GPIO_Pin_3);
		GPIO_SetBits(GPIOB, GPIO_Pin_12);
		Delay_ms(150);
		GPIO_ResetBits(GPIOA, GPIO_Pin_4);
		GPIO_ResetBits(GPIOB, GPIO_Pin_12);
		Delay_ms(150);
		GPIO_SetBits(GPIOA, GPIO_Pin_4);
		GPIO_SetBits(GPIOB, GPIO_Pin_12);
		Delay_ms(150);
		GPIO_ResetBits(GPIOA, GPIO_Pin_5);
		GPIO_ResetBits(GPIOB, GPIO_Pin_12);
		Delay_ms(150);
		GPIO_SetBits(GPIOA, GPIO_Pin_5);
		GPIO_SetBits(GPIOB, GPIO_Pin_12);
		Delay_ms(150);
		GPIO_ResetBits(GPIOA, GPIO_Pin_6);
		GPIO_ResetBits(GPIOB, GPIO_Pin_12);
		Delay_ms(150);
		GPIO_SetBits(GPIOA, GPIO_Pin_6);
		GPIO_SetBits(GPIOB, GPIO_Pin_12);
		Delay_ms(150);
		GPIO_ResetBits(GPIOA, GPIO_Pin_7);
		GPIO_ResetBits(GPIOB, GPIO_Pin_12);
		Delay_ms(150);
		GPIO_SetBits(GPIOA, GPIO_Pin_7);
		GPIO_SetBits(GPIOB, GPIO_Pin_12);
		Delay_ms(150);
	}
}
