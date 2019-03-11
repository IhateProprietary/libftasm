	extern _ft_isdigit
	extern _ft_isalpha
	global _ft_isalnum
	default rel
	section .text
_ft_isalnum:
	push rbp
	lea rbp, [rsp]
	call _ft_isdigit
	cmp eax, 0
	jnz END
	call _ft_isalpha
END:
	pop rbp
	ret
