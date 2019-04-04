	global _ft_isprint
	default rel
	section .text
_ft_isprint:
	push rbp
	lea rbp, [rsp]
	cmp edi, 0x1f
	jle E2
	cmp edi, 0x7f
	jae E2
E1:	
	mov eax, 1
	jmp END
E2:	
	mov eax, 0
END:
	pop rbp
	ret 
