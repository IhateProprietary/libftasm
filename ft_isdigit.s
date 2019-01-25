	global _ft_isdigit
	default rel
	section .text
_ft_isdigit:
	cmp edi, 0x29
	jle E2
L1:
	cmp edi, 0x39
	ja E2
E1:
	mov eax, 1
	jmp END
E2:
	mov eax, 0
END:
	ret
