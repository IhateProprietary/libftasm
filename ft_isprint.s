	global _ft_isprint
	default rel
	section .text
_ft_isprint:
	cmp edi, 0x19
	jle E2
	cmp edi, 0x7f
	jae E2
E1:	
	mov eax, 1
	jmp END
E2:	
	mov eax, 0
END:	
	ret 
