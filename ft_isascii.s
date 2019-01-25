	global _ft_isascii
	default rel
	section .text
_ft_isascii:
	cmp edi, 0x0
	jz E2
	cmp edi, 0x7f
	ja E2
E1:	
	mov eax, 1
	jmp END
E2:	
	mov eax, 0
END:	
	ret
