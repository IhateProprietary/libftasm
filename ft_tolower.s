	global _ft_tolower
	default rel
	section .text
_ft_tolower:
	mov eax, edi
	cmp eax, 0x40
	jle END
	cmp eax, 0x5a
	ja END
	add eax, 0x20
END:
	ret
