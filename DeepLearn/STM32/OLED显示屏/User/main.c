#include "stm32f10x.h"                  // Device header
#include "Delay.h"
#include "OLED.h"

int main(void) {
	
	OLED_Init();
	OLED_ShowChar(1, 1, 'A');
	OLED_ShowString(2, 1, "Hello, World!");
	OLED_ShowNum(3, 1, 12345, 5);
	OLED_ShowSignedNum(3, 2, -12345, 5);
	OLED_ShowBinNum(4, 2, 0x0010, 16);
	OLED_ShowHexNum(4, 1, 0xAA55, 4);
	OLED_Clear();
	OLED_ShowString(1, 1, "Hello, World!");
	OLED_ShowString(2, 1, "Man!");
	OLED_ShowString(3, 1, "What can i say?");
		
	
	while(1) {
		
	}
}

