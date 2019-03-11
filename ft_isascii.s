	global _ft_isascii
	default rel
	section .text
_ft_isascii:
	push rbp
	lea rbp, [rsp]
	test edi, edi
	jz E2
	cmp edi, 0x7f
	ja E2
E1:	
	mov eax, 1
	jmp END
E2:	
	mov eax, 0
END:
	pop rbp
	ret
