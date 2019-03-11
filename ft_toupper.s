	global _ft_toupper
	default rel
	section .text
_ft_toupper:
	push rbp
	lea rbp, [rsp]
	mov eax, edi
	cmp eax, 0x60
	jle END
	cmp eax, 0x7a
	ja END
	sub eax, 0x20
END:
	pop rbp
	ret
