	extern _malloc
	extern _ft_strlen
	extern _ft_memcpy
	global _ft_strdup
	default rel
	section .text
_ft_strdup:
	call _ft_strlen
	push rdi 					;rdi const char*
	add rax, 1					;rdi == rax + 1
	mov rdi, rax
	push rax					;save size
	mov rdi, [rsp]				;get size from stack
	sub rsp, 8					;align
	call _malloc
	cmp rax, 0					;malloc == NULL?
	jz END						;if NULL return NULL
	mov rdi, rax				;put malloc ret in rdi
	mov rsi, [rsp + 16]
	mov rdx, [rsp + 8]
	call _ft_memcpy
END:
	add rsp, 24
	ret
