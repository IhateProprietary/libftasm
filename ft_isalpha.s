	global _ft_isalpha
	default rel
	section .text
_ft_isalpha:
	push rbp
	lea rbp, [rsp]

	cmp edi, 0x40
	jle L2
L1:
	cmp edi, 0x5a
	jle E1
L2:
	cmp edi, 0x60
	jle E2
L3:
	cmp edi, 0x7a
	ja E2
E1:
	mov eax, 1
	jmp END
E2:
	mov eax, 0
END:
	pop rbp
	ret
